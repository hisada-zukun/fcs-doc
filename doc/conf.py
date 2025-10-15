import os
from pathlib import Path
import yaml

# -- Project info -----------------------------------------------------------
project = 'FCS Docs'
copyright = 'TOEI Zukun'
author = 'Zukun'

# Environment flags
build_all_docs = os.environ.get("build_all_docs", False)
pages_root = os.environ.get("pages_root", "")
build_pdf = os.environ.get("build_pdf", "False")
current_language = os.environ.get("current_language", "jp")
current_version = os.environ.get("current_version", "latest")

version = current_version
release = current_version

# -- General configuration -------------------------------------------------
extensions = ['myst_parser', 'sphinx_rtd_theme']
if build_pdf == "True":
    extensions.append('rst2pdf.pdfbuilder')
    extensions.append('sphinx.ext.autodoc')

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output -----------------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- PDF output ------------------------------------------------------------
# latex_engine = 'pdflatex'
latex_engine = 'lualatex'

latex_documents = [
    ('index', 'fcs_manual.tex', f'FCS Manual {current_version}', 'TOEI Zukun', f'manual'),
]

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '12pt',
    'preamble': r'''
\usepackage{graphicx}
\usepackage{float}
\usepackage{sphinx}
\usepackage{luatexja-fontspec}
\setmainjfont{IPAexMincho}
''',
    'inputenc': '',
    'utf8extra': '',
}

# -- sphinx-intl -----------------------------------------------------------
locale_dirs = ['locale/']
gettext_compact = False

# -- rst2pdf image fix -----------------------------------------------------
if 'rst2pdf.pdfbuilder' in extensions:
    from rst2pdf.createpdf import MyImage as Image
    from reportlab.lib.units import cm

    _orig_wrap = Image.wrap

    def wrap_all_images(self, availWidth, availHeight):
        """Automatically scale all images to fit frame/page."""
        try:
            # fallback width/height if missing
            width = getattr(self, 'width', None)
            height = getattr(self, 'height', None)

            max_width = min(availWidth, 15*cm)
            max_height = min(availHeight, 25*cm)

            # if missing, assign defaults
            if not width or not height:
                self.width = max_width
                self.height = self.width * 0.75  # fallback aspect ratio
            else:
                scale_w = max_width / width if width > max_width else 1
                scale_h = max_height / height if height > max_height else 1
                scale = min(scale_w, scale_h)
                self.width *= scale
                self.height *= scale
        except Exception:
            # fallback in case anything fails
            self.width = min(getattr(self, 'width', availWidth), availWidth)
            self.height = min(getattr(self, 'height', availHeight), availHeight)
        return _orig_wrap(self, availWidth, availHeight)

    Image.wrap = wrap_all_images
