# Release Note
## FCS 24.10.06
- Date: 2024/10/16
- Version: 24.10.06
- Stage: Stable

### ！Cannot be downgraded！
** Once opened in this version, your FCS session will not be abled to downgraded to a previous version of FCS, including FCS 24.10.05.** We strongly recommend you to backup your files before using the update.


### Overview
1. Fixed animation timeline off by 1 frame
2. Optimized launch spped
3. Improved logging 

#### Fixed animation timeline off by 1 frame
Fixed a bug where the first frame of a video is used twice (i.e., the 99th frame is presented as the 100th frame). All previously created profiles are all off by one frame, which will be fixed once imported using the new version of FCS. However, it also means that it will be incorrect if the fixed profile is imported back to a previous version of FCS. Therefore, once imported to the new version, it is not possible to downgrade to use the previous version. 


### ！ダウングレードできません！
**このバージョンで作成または開いたセッションを24.10.05を含む、以前のバージョンを開くことができません。
ご注意ください。**
アップデートされる前に、プロジェクトフォルダーをバックアップすることを強く推奨いたします。


### 概要
1. 動画表示が１フレームずれていることを修正しました
2. ソフト起動時の最適化
3. ログ方式の改善

#### 動画表示が１フレームずれていることを修正しました
Video/Playerの０フレームが重複して出力されていたことを修正いたしました。 （１００フレーム目が９９フレーム目として表示されていました）  
Profileのフレームカウントも1フレームずれていました。
そのため、以前のバージョンンで作成されたセッションについては、現バージョンで開くことにより、自動的に修正されるようになります。
ただし、修正されたものに関しては、以前のバージョン（24.10.05を含む）で開くことができなるなりました。
お手数をおかけしまして、大変申し訳ございません。


## FCS 24.10.05
- Date: 2024/10/11
- Version: 24.10.05
- Stage: Stable

### Overview
1. Fixed a bug where video is not cached when opened for viewing
2. Fixed a bug where the auto profile assigns the wrong name to the profile in ROM mode 
3. Added a new feature for exported solver for real-time use
4. Added a warning sign for invalid controller info.

### 概要
1. 動画開く際に、キャッシュされるはずのデータがキャッシュされていないことを修正しました
2. Auto　Profileのプロファイルの出力番号がずれていることを修正
3. リアルタイムアプリへの出力するソルバーの形式を修正
4. コントローラーの可動域が正しくない場合、エラーが表示されるように修正

## FCS 24.10.04
- Date: 2024/10/07
- Version: 24.10.04
- Stage: Stable

### Overview
1. Fixed a bug where landmark frame output crashes the application under specific circumstances.

### 概要
1. 特定の場合において、ランドマーク画像の出力時にアプリケーションがクラッシュするバグを修正しました。


## FCS 24.10.03
- Date: 2024/09/25
- Version: 24.10.03
- Stage: Stable

### Overview
1. Fixed gallery issues
2. Fixed installer issues
3. Misc.

### Detail
#### Fixed gallery issues
1. Fixed an issue where reset on FCS UI doesn't get send to Maya
2. Fixed a bug where disabled regions' values are still sent to Maya

#### Fixed installer issues
1. Changed the default install path to C drive
2. Updated the installer icon
3. Added Japanese support

#### Misc 
1. Fixed a bug where controller rename triggers app crashes
2. Fixed a bug where smoothing is not applied （Fixed in 24.10.01）
3. Fixed Prioritize Profile

### 概要
1. Gallery機能修正
2. インストーラ修正
3. その他修正

### 詳細
#### Gallery機能修正
1. Syncにチェックが入っている状態でResetボタンを押すとMayaにも反映されるようになりました
2. Editorにて、To Mayaなどの際にDisabledになっているリージョンの値は送信しないようになりました

#### インストーラ修正
1. デフォルトのインストール先をCドライブに変更しました
2. インストーラのアイコンを変更しました
3. インストーラが日本語・英語両方に対応しました

#### その他
1. コントローラーをリネームする際にアプリが落ちてしまう問題を修正しました
2. スムージングが適用されていない問題を修正しました（24.10.01）
3. Prioritize Profileの動作を修正しました  

## FCS 24.10.02
- Date: 2024/09/09
- Version: 24.10.02
- Stage: Beta

### Overview
1. Improved filtering feature in Gallery, allowing batch edit/delete  
2. Fixed a bug where editor landmark preview is turned off when opening a new profile.
3. Fixed a bug where the cursor position does not exactly move to 
4. Optimized gallery render speed
5. Added Prioritize Profile
6. Added a feature to batch rename all controllers
7. Improved video playback speed

### Detail
#### Improved filtering feature in Gallery, allowing batch edit/delete  
1. Add filtering by region, video name etc.

#### Fixed a bug where the cursor position does not exactly move to 
1. Ctrl + Left mouse button click to enter value directly 
2. Cursor position will translate to the value of the slider
   
#### Prioritize Profile
1. Added a feature to match the output animation with the defined profiles. 
2. Enabled by checking Solver/Post-processing/Prioritize Profile

#### Batch rename controller
1. Select controllers in Controller Info to rename, useful for adding prefix/suffix etc. 
2. The change will propagate to the profiles previously created.

#### Improved video playback speed
1. Added a feature to use RAM to speed up video playback, mostly useful for legacy computers.
2. Default to enabled. 
3. You are store a maximum of 5 videos to your memory if it allows.

#### Added a solver export feature for real time use 
1. Export a solver file using Solver/Export.
2. Import the file into the real time application (WIP) for view your character moving in real-time



### 概要
1. Galleryのフィルタリング機能強化  
    プロフィールの一括変更や削除ができるようになりました  
2. EditorのLMの表示がONの場合、別のプロフィールを開いてもONの状態のままにしました（計算済みの場合のみ）  
3. Editorのコントローラー値を変更する箇所の表示方式を変更しました
4. Galleryの表示方式を改善しました
5. プロフィール優先機能(Prioritize Profile)を追加しました
6. コントローラーの名前を一括変更する機能を追加しました
7. ビデオ再生の速度を向上させました
8. リアルタイム版への出力機能を追加しました

### 詳細
#### Galleryのフィルタリング
1. 動画名、各Regionの状態などでフィルタリングする機能、一括リージョンON/OFF・一括削除などの機能を追加しました

#### Editorのコントローラー値の表示方式
1. Ctrl＋クリックで数値を入力
2. カーソルに合わせて数値が設定されるようになりました
   
#### プロフィール優先機能
1. FCSから出力されたアニメーションに関して、プロファイルが存在するフレームにおいて表情を厳密に一致させる機能を追加しました
2. 有効化するにはSolver/Post-processing/Prioritize ProfileをONにしてください

#### コントローラーの名前を一括変更
1. Controller Infoでコントローラーを選択し、Renameを押すと、コントローラーのリネームができるようになりました
2. 名前の変更に伴い、Galleryで登録された情報も変更されます

#### ビデオ再生の速度を向上させました
1. 動画をメモリーにコピーすることにより、HDDなどのストレージ媒体より早く再生できるようになります
2. デフォルトで有効になります
3. メモリーに余裕があれば開いた動画（5本まで）をメモリーに保存することができます、複数の動画を同時に編集してもメモリーにキャッシュするようになります

#### リアルタイム版への出力機能
1. Solver/ExportでFCSで作成されたソルバーが出力されます
2. リアルタイムサーバ（準備中）に読み込むとFCSでオフライン出力に近いクオリティーのアニメーションがリアルタイムで出力できるようになります  

## FCS 24.10.01
- Date: 2024/08/29
- Version: 24.10.01
- Stage: Beta

### Overview
1. Added a language and version switcher for the manual (left bottom)
1. [English manual](https://zukunfcs.github.io/fcs-doc/24.10/en/index.html) (draft) now available
2. Added experimental linux support
3. Added an installer for FCS
4. Added a feature to download ffmpeg if it doesn't exist on the user system.
5. [Added a feature to automatically generate profile from video](https://zukunfcs.github.io/fcs-doc/latest/en/012_auto_pickup.html)
6. Added UI elements and download for the new version. 

### Info for upgrading from a previous version
You can safely open your session from 24.07.
    

### Detail

#### Installer
1. Changed build method to Themida. Using virtual machine and debugger together with FCS is unsupported. If you need to allow these for specific reason please contact us.
2. Added installer, default installation path is C:\FCS. Please ensure the program has write access to the folder.

#### FFMPEG
1. Pull ffmpeg directly from [github](https://github.com/BtbN/FFmpeg-Builds/) if it doesn't exist in the user system.
2. If you cannot connect to github please directly install ffmpeg and add it to path.   

#### UI
1. You can now open and view a video using double click
2. Fixed a bug where the layout is not retained  
3. Fixed the initial layout of FCS when first launch in a new computer
4. Added timeline drag
5. Added a feature to retain user interface states so it persist between program launches. 
6. Updated japanese translations
7. Added support for modifier keys
8. Added support for shortcut keys
   - Save profile
   - Open Profile from video
   - Send value from Editor to Maya (To Maya) 
   - Receive controller value from Maya (From Maya)
   - Change layout 
9. Renamed Enforce Annotation to Prioritize Profile

#### Maya
1. Disabled region values are not sent from FCS to maya

#### Updater
1. Added a new feature to check for new updates 
2. Update settings are as follow
   1. Update channel: All | Patch | None  
    Decide what kind of updates are checked for. 
   2. Use Beta
    Use the unstable build.

#### Linux Support
FCS supports Fedora 8 now, please contact us if you are interested.

#### Misc.
1. Program data location is changed from `$USER/.fcs/Cortado` to `$USER/.fcs/Cortado/$version`.


### 概要
#### マニュアル関連
1. 24.07, 24.10など、バージョンごとのマニュアルが確認できるようになりました
2. [English manual](https://zukunfcs.github.io/fcs-doc/24.10/en/index.html) (draft) now available

#### セットアップ
1. インストーラーからインストールができるようになりました
2. ffmpegがシステムにインストールされていない場合、自動的にダウンロードできるようになりました

#### Auto Pickup α
[動画から特定のフレームを自動的にGalleryに追加する機能を実装しました。](https://zukunfcs.github.io/fcs-doc/latest/en/012_auto_pickup.html)

#### 自動更新
新しいバージョンが発行された際に、FCSのUIから更新内容の表示およびダウンロードができるようになりました

#### Linuxサポート
実験的にLinux対応を始めました

### アップデート注意
以下のバージョンを使用しこれからアップデートする方は以下の事項に注意していただければと思います

1. 24.07  
    特になし 

### 詳細
#### マニュアル
1. マニュアルサイトが日本語・英語に対応しました。左下で切り替えられます
2. FCSソフトから開く際にはソフトに対応するバージョンが自動で開くようになります

#### インストール
1. ビルド方式をThemidaに変更しました。その際に、バーチャルマシン（VM）やデバッガーとの共同使用が対象外になりました。環境によって利用できなくなった方はご連絡ください。
2. インストーラーを追加しました。デフォルトではC:\FCSで作成されるようになります。インストール先フォルダの書き込み権限が必要になりますので、書き込み権限のないフォルダに入れると問題が発生します。

#### FFMPEG
1. 起動時に、ffmpegがシステムパスに存在しないとき、自動的に[github](https://github.com/BtbN/FFmpeg-Builds/)からダウンロードするようになっています。
2. Githubへの接続ができないお客様は手動でffmpegをインストールし、pathに追加するようにお願いいたします。

#### ユーザインタフェース  
1. ビデオ名をダブルクリックで開けるようになりました  
2. プログラム終了時のタブのレイアウトが保存されるようになりました  
3. FCS初回起動時のタブのレイアウトを整理しました  
4. タイムラインをドラッグする際に、範囲からカーソルをずらしても動くようになりました  
5. 一部のUIから選択できる項目がプログラムを終了しても保存されるようになりました
6. UIの日本語訳を更新しました
7. キーボードショートカットを修飾キーに対応させました
8. 一部の機能にキーボードショートカットを対応させました　　
   - Profile保存
   - Profileから動画を開く
   - Editorの値をMayaへ送信 (To Maya) 
   - Mayaからリグの値を受信 (From Maya)
   - レイアウトの変更 
9. Enforce AnnotationをPrioritize Profileへ名称変更しました

#### Maya
1. FCSからmayaへ送信する際に、Disabledされたリージョンを送信しなくなりました 

#### 自動更新
1. プログラム起動時に、新しいアップデータを検出するようになりました
2. アップデートに関しては以下の設定がSettingsウィンドウから変更できます
   1. Update channel: All | Patch | None  
    すべてをアップデートする、もしくはバグ修正（保守アップデート）のみ、またはアップデートしないことが選択できます
   2. Use Beta
    安定しない機能を含めたベータ版の利用ができるようになります

#### Linuxサポート
FCSがFedora 8に対応しました。ご興味のある方はご連絡ください。

#### その他
1. プログラムデータの保存先を`$USER/.fcs/Cortado`から`$USER/.fcs/Cortado/$version`に変更しました
