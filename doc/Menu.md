# File

Session(セッション)ファイルに関連したメニューです。
セッションを開く、設定の変更、新規セッションの作成などを実行することができます。
## Session
### ・New…
セッションを新規で作成します。Create new Sessionウィンドウを開きます。

#### Create new Sessionウィンドウ
![CreateNewSession](https://github.com/user-attachments/assets/0aa461c3-0db5-4335-85a0-d930d7da465e)

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

##### Create new Sessionで作成されるフォルダ構造  

| 色 | 内容 | 
|:-------------:|:--------------:|
| 赤枠      | Project Folderで作成されるフォルダ           |
| 青枠      | Actorで作成されるフォルダ           |
| 緑枠      | Characterで作成されるフォルダ             |

![folder](doc/images/folder.jpg)

| フォルダ | 子フォルダ | 説明 | 
|:-------------:|:--------------:|:--------------:|
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

### ・Open▶
#### Open…
ダイアログから.yamlファイルを選択してセッションを開きます。
#### [パス]
最近使用したセッションのパスが表示されます。

<BR>

### ・Info
Session Dataウィンドウが開きます。
<img width="1151" height="478" alt="image" src="https://github.com/user-attachments/assets/d30863da-b3c2-4971-8b30-108ca4043546" />
#### Session Dataウィンドウ
右クリックメニューから内容のコピーや編集を行うことができます。

| 項目 | 説明 | 右クリックメニュー| 
|:-------------:|:--------------:|:--------------:|
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

### ・Save ▶
#### Session
*セッションを保存するとは?*
#### Profiles
Editウィンドウのプロファイルを保存します。
#### Controller
コントローラーウィンドウの表を保存します。

<BR>

### ・Export
Export Sessionウィンドウが開きます。
<img width="795" height="322" alt="image" src="https://github.com/user-attachments/assets/00fb49e7-d1f5-47d7-9478-7120e0ddf660" />
| 項目 |プルダウン内容| 説明 | 
|:-------------:|:--------------:|:--------------:|
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
### ▼ UI
Global
Font Size　10 - 50　文字の大きさ　設定変更後はFCS再起動で切り替え
Language　en / jp　言語設定　設定変更後はFCS再起動で切り替え
Gallery
	Thumbnail width　ギャラリーに表示されるプロファイル画像の横幅
Default Cols　ギャラリーのデフォルトの列数
Video Player
	Cache Frame Max　メモリにキャッシュするフレームの最大値
note
Cache Frame Maxは数値を上げるほど多くのメモリ容量を消費します。
FullHDサイズだと10000fごとに約64GB使用される目安です。
-1を指定すると無制限にキャッシュを保存します。これは十分なメモリがある場合のみ使用してください。
	Default Tags　デフォルトで付与するタグ名
Video Library
☑ Skip rotation prompt　Videoインポートで回転処理の設定画面を表示するかどうか
	Default Rotation　Videoインポートの際のデフォルトの回転値（0で回転しない）
▼Output
Default	 output options
	Default Folder　デフォルトの出力先フォルダ
Default Filename　デフォルトのファイル名
Default Filename (Batch)　バッチ出力時のデフォルトファイル名
Default Maya scene format　デフォルトのMaya保存形式
Playblast
	Encoder　プレイブラストのエンコード設定
	Width　プレイブラストの横幅
	Height　プレイブラストの立幅
	Quality　プレイブラストの画質
	Percent　プレイブラストの解像度
▼Keyboard Shortcuts
同時押しはキー1種+修飾キー2種の3ボタンまで登録可能です
・Timeline
Next Frame　次のフレームへ　デフォルト「.+Alt」
Previous Frame　前のフレームへ　デフォルト「,+Alt」
Next ROM　次のプロファイルへ　デフォルト「.」
Previous ROM　前のプロファイルへ　デフォルト「,」
Play / Pause Timeline　タイムラインの再生 / 一時停止　デフォルト「v+Alt」
Add current frame to ROM　現在のフレームをプロファイルとして追加　デフォルト「Q」
Open profile on timeline　タイムラインのプロファイルを開く？　デフォルト「E」
・Editor
Save ROM edits　プロファイルの保存　デフォルト「S+Ctrl」
From Maya　表情の値をMayaから読み込み　デフォルト「V+Ctrl」
To Maya　表情の値をMayaへ送信　デフォルト「C+Ctrl」
・Layout
Active Pickup　Pickupのレイアウトに変更　デフォルト「1+Ctrl」
Active Process　Processのレイアウトに変更　デフォルト「2+Ctrl」
Active Register　Registerのレイアウトに変更　デフォルト「3+Ctrl」
Active Retarget　Retargetのレイアウトに変更　デフォルト「4+Ctrl」
▼Maya
CommandPort　Mayaとの接続に使用するコマンドポート
SliderSyncPort　Mayaのタイムラインを取得するコマンドポート
☑ Open maya scene at launch　Launch Maya時に登録したMayaシーンも開く
☑ Use gallery character preview　
Image Plane　イメージプレーン名
Camera　カメラ名
Install path　Mayaのインストール先
▼Misk
Keep max N video in memory
Backend　cpu / cuda
Update Channel　All / Patch / None　
☑ Use Beta　ベータ版機能を使用する

Save　設定を保存する（設定によってはFCSの再起動で反映されます）
Restore　設定をデフォルトに戻す
Import　
Quit
FCSを終了します。「.Lockファイル」を削除します。
