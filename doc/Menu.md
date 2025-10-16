# File

Session(セッション)ファイルに関連したメニューです。
セッションを開く、設定の変更、新規セッションの作成などを実行することができます。
## Session
### New…
セッションを新規で作成します。Create new Sessionウィンドウを開きます。

#### Create new Sessionウィンドウ
![CreateNewSession](https://github.com/user-attachments/assets/0aa461c3-0db5-4335-85a0-d930d7da465e)

- Project Folder：FCSの作業データを置きたい場所(Root)のパス入力欄
  - 「Browse...」ボタン：ダイアログを開いてプロジェクトフォルダの作成先を入力します。
  - 「Create」ボタン：FCSのプロジェクトフォルダを作成します。
- Actor：解析する動画のアクター(演技者)名入力欄<BR>既に該当アクターのフォルダが存在する場合、プルダウンから選択できます。
  - 「+」ボタン：「Create new actor」ウィンドウを起動して、アクター名のフォルダを作成します。<BR>アクター名はプルダウンに追加されます。
- Character：3Dモデルのキャラクター名入力欄
  - 「+」ボタン：「Create new character folder」ウィンドウを起動して、キャラクター名のフォルダを作成します。<BR>キャラクター名はプルダウンに追加されます。
- Maya Scene：3DモデルのMayaシーンのパス入力欄
  - 「Browse...」ボタン：ダイアログを開いてパスを入力します。
- Maya Base　「workspace.melがあるフォルダのパス入力欄
  - 「Browse...」ボタン：ダイアログを開いてパスを入力します。
- Maya Ver　3Dモデルに対応するMayaのバージョン入力欄
  - プルダウン：2018 - 2026の範囲のバージョンを選択できます。
- Save　：入力した内容でSession(セッション)を作成します。
  - 「Save」ボタン：characterフォルダ直下にfcs_session.yaml(FCSファイル)が作成されます。<BR>*現時点のセッション作成後の正式な挙動確認　プロジェクトが開く？*

##### Create new Sessionで作成されるフォルダ構造  

| 色 | 内容 | 
|:-------------|:--------------:|
| 赤枠      | Project Folderで作成されるフォルダ           |
| 青枠      | Actorで作成されるフォルダ           |
| 緑枠      | Characterで作成されるフォルダ             |

![folder](doc/images/folder.jpg)

| フォルダ | 内容| 説明 | 
|:-------------|:--------------:|:--------------:|
| Facial |       | 動画やMayaシーンデータ等素材を保存するフォルダ           |
|     | Assets           |モデル・テクスチャなど、Mayaのプロジェクトファイル（Assets以下）を保存するフォルダ |
|     | RecData             | ROM動画やFCSで解析・出力したい動画を保存するフォルダ |
|     | Scene             |  FCSでアニメーションを出力する際のMayaシーンのデフォルト出力先  |
|     | SetData             | FCSでアニメーションを出力する際のwavファイルや連番画像の出力先    |
| FCS |       | Project Folderで作成したフォルダ<BR>解析に使用するデータが保存されるプロジェクトフォルダ            |
|     | Actor| Actorで作成したフォルダ<BR>Actorで入力した名前がフォルダ名になる   |
|     | Character| Characterで作成したフォルダ<BR>Characterで入力した名前がフォルダ名になる |
|     | RetargetData（IMG/PARAM）| 作成したProfileの編集データ（画像や数値情報）が保存されるフォルダ  |
|     | VideoData| 解析する動画のキャッシュファイルが保存されるフォルダ |
|     | .lock      | 作業の競合を防ぐためのロックファイル<BR>セッションの起動・終了時に、自動で作成・消去される   |
|     | fcs_session.yaml      | セッション情報を保存しているファイル |
