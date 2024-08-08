import os
import yaml
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FCS Manual'
copyright = 'TOEI Zukun'
author = 'Zukun'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx_rtd_theme']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


# -- sphinx-intl -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/advanced/intl.html
locale_dirs = ['locale/']
gettext_compact = False

# get the environment variable build_all_docs and pages_root
build_all_docs = os.environ.get("build_all_docs")
pages_root = os.environ.get("pages_root", "")

# if not there, we dont call this
if build_all_docs is not None:
    # we get the current language and version
    current_language = os.environ.get("current_language")
    current_version = os.environ.get("current_version")

    # we set the html_context wit current language and version 
    # and empty languages and versions for now
    html_context = {
        'current_language' : current_language,
        'languages' : ['ja', 'en'],
        'current_version' : current_version,
        'versions' : ['24.07'],
    }


    # and we append all versions and langauges accordingly 
    # we treat t he main branch as latest 
    if (current_language == 'en'):
        html_context['versions'].append(['latest', pages_root + '/en'])
    if (current_language == 'jp'):
        html_context['versions'].append(['latest', pages_root])

    # and loop over all other versions from our yaml file
    # to set versions and languages
    with open("versions.yaml", "r") as yaml_file:
        docs = yaml.safe_load(yaml_file)

    if (current_version != 'latest'):
        for language in docs[current_version].get('languages', []):
            html_context['languages'].append([language, pages_root+'/'+current_version+'/'+language])

    for version, details in docs.items():
        html_context['versions'].append([version, pages_root+'/'+version+'/'+current_language])