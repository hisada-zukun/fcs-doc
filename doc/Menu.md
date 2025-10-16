# File

Session(セッション)ファイルに関連したメニューです。
セッションを開く、設定の変更、新規セッションの作成などを実行することができます。
## Session
### New…
セッションを新規で作成します。Create new Sessionウィンドウを開きます。

![CreateNewSession](https://github.com/user-attachments/assets/0aa461c3-0db5-4335-85a0-d930d7da465e)

#### Create new Sessionウィンドウ

| 項目 | ボタン |説明| 
|:-------------:|:--------------:|:--------------|
|Project Folder||FCSの作業データを置きたい場所（Root）のパス入力欄|
||Browse...|ダイアログを開いてプロジェクトフォルダの作成先を入力します。|
||Create|FCSのプロジェクトフォルダを作成します。|
|Actor||解析する動画のアクター（演技者）名入力欄<BR>既に該当アクターのフォルダが存在する場合、プルダウンから選択できます。|
||+|「Create new actor」ウィンドウを起動して、アクター名のフォルダを作成します。<BR>アクター名はプルダウンに追加されます。|
|Character||3Dモデルのキャラクター名入力欄|
||+|「Create new character folder」ウィンドウを起動して、キャラクター名のフォルダを作成します。<BR>キャラクター名はプルダウンに追加されます。|
|Maya Scene||3DモデルのMayaシーンのパス入力欄|
||Browse...|ダイアログを開いてパスを入力します。|
|Maya Base||「workspace.mel」があるフォルダのパス入力欄|
||Browse...|ダイアログを開いてパスを入力します。|
|Maya Ver||3Dモデルに対応するMayaのバージョン入力欄|
||▼|2018 - 2026の範囲のバージョンを選択できます。|
|Save||入力した内容で新規Session(セッション)を作成します。|
||Save|characterフォルダ直下にfcs_session.yaml(FCSファイル)が作成されます。<BR>*現時点のセッション作成後の正式な挙動確認　プロジェクトが開く？*|

#### Create new Sessionで作成されるフォルダ構造  

| 色 | 内容 | 
|:-------------:|:--------------:|
| 赤枠      | Project Folderで作成されるフォルダ           |
| 青枠      | Actorで作成されるフォルダ           |
| 緑枠      | Characterで作成されるフォルダ             |

![folder](doc/images/folder.jpg)

| フォルダ | 子フォルダ | 説明 | 
|:-------------:|:--------------:|:--------------|
| Facial |       | 動画やMayaシーンデータ等の素材を保存するフォルダ           |
|     | Assets  |モデル・テクスチャなど、Mayaのプロジェクトファイル(Assets以下)を保存するフォルダ |
|     | RecData | ROM動画やFCSで解析・出力したい動画を保存するフォルダ |
|     | Scene   |  FCSでアニメーションを出力する際のMayaシーンのデフォルト出力先  |
|     | SetData | FCSでアニメーションを出力する際のwavファイルや連番画像の出力先    |
| FCS |          | Project Folderで作成したフォルダ<BR>解析に使用するデータが保存されるプロジェクトフォルダ            |
|     | Actor    | Actorで作成したフォルダ<BR>Actorで入力した名前がフォルダ名になる   |
|     | Character| Characterで作成したフォルダ<BR>Characterで入力した名前がフォルダ名になる |
|     | RetargetData（IMG/PARAM）| 作成したProfileの編集データ（画像や数値情報）が保存されるフォルダ  |
|     | VideoData| 解析する動画のキャッシュファイルが保存されるフォルダ |
|     | VideoData \ .lock      | 作業の競合を防ぐためのロックファイル<BR>セッションの起動・終了時に、自動で作成・消去される   |
|     | VideoData \ fcs_session.yaml      | セッション情報を保存しているファイル |

<BR>

### Open▶
#### Open…
ダイアログから.yamlファイルを選択してセッションを開きます。
#### [パス]
最近使用したセッションのパスが表示されます。

<BR>

### Info
Session Dataウィンドウが開きます。
<img width="1151" height="478" alt="image" src="https://github.com/user-attachments/assets/d30863da-b3c2-4971-8b30-108ca4043546" />
#### Session Dataウィンドウ
右クリックメニューから内容のコピーや編集を行うことができます。

| 項目 | 説明 | 右クリックメニュー| 
|:-------------:|:--------------|:--------------|
|Project Folder|プロジェクトフォルダのパス|パスのコピー|
|Actor|アクター名|リネーム・コピー|
|Character|キャラクター名|リネーム・コピー |
|Maya Scene|Mayaシーンパス| パスのコピー・変更|
|Maya Base|workspace.melのパス| パスのコピー・変更|
|Maya version| Mayaバージョン|コピー・変更|
|Profile Count|セッション内のプロファイルの数|コピー|
|Video Count|セッションにインポートした動画の数 | コピー|
|Created at| セッション作成日時| コピー|
|Created by| セッション作成者| コピー|
|Last saved at| 最終保存日時| コピー|
|Last saved by| 最終保存者| コピー|

<BR>

### Save ▶
#### Session
*セッションを保存するとは?*
#### Profiles
Editウィンドウのプロファイルを保存します。
#### Controller
コントローラーウィンドウの表を保存します。

<BR>

### Export
Export Sessionウィンドウが開きます。
<img width="795" height="322" alt="image" src="https://github.com/user-attachments/assets/00fb49e7-d1f5-47d7-9478-7120e0ddf660" />
#### Export Sessionウィンドウ
| 項目 |プルダウン内容| 説明 | 
|:-------------:|:--------------:|:--------------|
|Project Folder||エクスポート先のフォルダパス入力欄（フルパスで指定）|
|Actor||エクスポート後のアクター名入力欄|
|Character||エクスポート後のキャラクター名入力欄|
|Profile ☑||プロファイルを含めて出力するかどうかを指定|
|Videos|▼|出力先に動画ファイルをコピーするかを指定|
||No video|動画データをコピーしない|
||Associated video|関連する動画のみコピー|
||All files|Recdata内のすべての動画データをコピー|
|Facial/Assets Folder ☑||出力先にFacial/Assets以下のフォルダー・ファイルをコピーするかを指定|

<BR><BR>

## Settings
FCS全般の設定メニューです。
### ▼ UI
<img width="781" height="458" alt="image" src="https://github.com/user-attachments/assets/4654b5ab-ff4e-4148-9caf-66d6e3059fd2" />

#### Settings > UI

|対象| 項目 |デフォルト| 説明 |要 再起動| 
|:--------------|:--------------|:--------------:|:--------------|:--------------:|
|Global|Font Size|25|文字の大きさ|〇|
||Language|en|言語設定|〇|
|Gallery|Thumbnail width|200|ギャラリーに表示されるプロファイル画像の横幅||
||Default Cols|3|ギャラリーのデフォルトの列数||
|Video Player|Cache Frame Max|2000|メモリにキャッシュするフレームの最大値||
||Default Tags||デフォルトで付与するタグ名||
|Video Library| Skip rotation prompt|☐|Videoインポートで回転処理の設定画面を表示するかどうか||
||Default Rotation|0|Videoインポートの際のデフォルトの回転値（0で回転しない）||

```{note}
Cache Frame Maxは数値を上げるほど多くのメモリ容量を消費します。
FullHDサイズだと10000fごとに約64GB使用される目安です。
-1を指定すると無制限にキャッシュを保存します。この設定は十分なメモリがある場合のみ使用してください。
```
### ▼Output
<img width="1091" height="421" alt="image" src="https://github.com/user-attachments/assets/0618dda2-88c4-4a0f-85ea-7c88bef60d93" />

#### Settings > Output

|対象| 項目 |デフォルト| 説明 |再起動| 
|:--------------|:--------------|:--------------:|:--------------|:--------------:|
|Default output options|Default Folder|Facial/Scenes/_Outputs/<BR>%Y%m%d_%H%M%S_{user}|デフォルトの出力先フォルダ||
||Default Filename|{video}|デフォルトのファイル名|||
||Default Filename (Batch)|{video}|バッチ出力時のデフォルトファイル名|||
||Default Maya scene format|.mb|デフォルトのMaya保存形式|||
|Playblast|Encoder|H.265/HEVC|プレイブラストのエンコード設定||
||Width|1920|プレイブラストの横幅||
||Height|1080|プレイブラストの立幅||
||Quality|100|プレイブラストの画質||
||Percent|100|プレイブラストの解像度||

### ▼Keyboard Shortcuts
同時押しはキー1種+修飾キー2種の3ボタンまで登録可能です。

<img width="928" height="668" alt="image" src="https://github.com/user-attachments/assets/4374192f-be47-4b9f-a8e2-b00092e35d1e" />

#### Settings > Keyboard Shortcuts
|対象|項目 | デフォルト |説明|
|:--------------|:--------------|:--------------:|:--------------|
|・Timeline|Next Frame|.+Alt|次のフレームへ|
||Previous Frame|,+Alt|前のフレームへ|
||Next ROM|.|次のプロファイルへ|
||Previous ROM|,|前のプロファイルへ|
||Play / Pause Timeline|v+Alt|タイムラインの再生 / 一時停止|
||Add current frame to ROM|Q|現在のフレームをプロファイルとして追加|
||Open profile on timeline|E|*タイムラインのプロファイルを開く？*|
|・Editor|Save ROM edits|S+Ctrl|プロファイルの保存|
||From Maya|V+Ctrl|表情の値をMayaから読み込み|
||To Maya|C+Ctrl|表情の値をMayaへ送信|
|・Layout|Active Pickup|1+Ctrl|Pickupのプリセットレイアウトに変更|
||Active Process|2+Ctrl|Processのプリセットレイアウトに変更|
||Active Register|3+Ctrl|Registerのプリセットレイアウトに変更|
||Active Retarget|4+Ctrl|Retargetのプリセットレイアウトに変更|

### ▼Maya
<img width="938" height="280" alt="image" src="https://github.com/user-attachments/assets/f96e06e8-7fb1-4828-a06d-e62b1b09318c" />

#### Settings > Maya
|項目| デフォルト |説明|
|:--------------|:--------------:|:--------------|
|CommandPort|42069|Mayaとの接続に使用するコマンドポート|
|SliderSyncPort|42070|Mayaのタイムラインを取得するコマンドポート|
|Open maya scene at launch|☑|Launch Maya時に登録したMayaシーンも開く|
|Use gallery character preview|☑|*確認*
|Image Plane|imagePlane|イメージプレーン名|
|Camera|fcs_cam|カメラ名|
|Install path||C:/Program Files/Autodesk/|Mayaのインストール先|

### ▼Misk
<img width="783" height="178" alt="image" src="https://github.com/user-attachments/assets/0bd70e1e-8fba-4116-962f-8fba63743aab" />

#### Settings > Misk
|項目| デフォルト |説明|
|:--------------|:--------------:|:--------------|
|Keep max N video in memory|1|*確認*|
|Backend|cpu|データの処理方法|
|Update Channel|Patch|アップデート*確認*|
||All||
||Patch||
||None||
|Use Beta|☐|ベータ版機能を使用する|

### Save

設定を保存します。設定によってはFCSを再起動することで反映されます。

### Restore　

設定をデフォルトに戻し、FCSを再起動します。

### Import　
*確認*

## Quit

FCSを終了します。「.Lockファイル」を削除します。

<BR><BR><BR>

# Window
ウィンドウを表示するメニューです。ここでは各ウィンドウの説明を行います。

## Videos
Videosウィンドウが開きます。<BR>
Videosウィンドウでは読み込んだHMC動画を一覧で表示します。読み込んだ動画に対しての処理も右クリックから可能です。

![videos](https://github.com/user-attachments/assets/9efd43b0-5951-4b55-9050-0449e1ee2d33)

① Filter入力欄<BR>
動画名を文字列でフィルターします。

② Importボタン<BR>
ダイアログを開いて新しい動画をインポートします。シフトキーで複数選択が可能です。

③ Video表見出し<BR>
右クリックメニューで表示する内容を変更することができます。

④ 選択ON/OFF切り替え<BR>
バッチ処理の対象にするかどうか切り替えます。

⑤ 動画名<BR>
動画名を右クリックでメニューが表示されます。メニューから単体のアニメーション出力を行うことができます。

⑥ 全選択ON/OFF切り替え<BR>

⑦*確認*<BR>
⑧Removeボタン<BR>

### Videos 右クリックメニュー
<img width="207" height="183" alt="image" src="https://github.com/user-attachments/assets/f8394235-8334-430d-b575-39d0daf818f0" />

- 動画名
- Open  
  動画を開く（PlayerとTimelineに表示されます）
- Remove  
  Remove Videos and Sequencesウィンドウを表示します。

#### Remove Videos and Sequencesウィンドウ
オプションを指定して動画をFCSから削除します。
Video：動画名
Delete caches option：
☑ SetData
☑ Tracking Sequence
Profiles▼
Keep　削除する動画のプロファイルはそのまま維持します
Keep but unlink　削除する動画のプロファイルは維持しますが、動画との
Delete


## Processer
## Controllers
## Profiles
### Gallery
### Editor
## Solver
## Log
```{info}
以下のウィンドウは初めから表示されており、メニューの中に含まれません。
```
## Player
## Timeline

<BR><BR><BR>

# Maya
## Status
Mayaとの接続状況を確認、クリックで接続をテストします。
## OpenScene
セッションに登録しているMayaシーンを開きます。
## Remove Animation
配布版には無し？

## Launch
	2018 - 2026　セッションに登録しているバージョンのMayaを新規で開きます。
	SettingsでOpen maya scene at launchをONにしている場合、Mayaシーンも開きます。
  
## GenerateMesh for Tracking Edits

<BR><BR><BR>

#View
## ☑ Fullscreen
全画面表示

## ☑ VSync　
## Scale
UI表示の拡大率

## ☑ Always on Top
FCSを常に最前面に表示する

## Layout▶
プリセットのレイアウトに切り替えます。

### Pickup
### Process
### Register
### Retarget
### Savecurrent 
現在のレイアウトに名前をつけて保存します。

### (Layout名)▶
#### Apply
保存したレイアウトに変更します。

#### Delete
保存したレイアウトを削除します。


<BR><BR><BR>

# Explore
Windowsエクスプローラーを開きます。

## Project
## FCS
### Actor
### Character
### Retarget Folder
### Video Data
## Facial
### Actor
### Assets
### Scenes
### RecData
### SetData
### Output Scene
## tmp
Logなどが格納されているフォルダ

<BR><BR><BR>

# Info
## License
ライセンスの管理

## About
FCSについて

## Help
FCSマニュアルの表示

## 3rd party licenses
サードパーティーライセンスについて

