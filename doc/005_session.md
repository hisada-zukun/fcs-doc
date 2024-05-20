## Session作成もしくはオープン
FCS起動後、「session」と呼ばれるプロジェクトファイルにアクセスするため
「New...（新規作成）またはOpen（開く）」を実行します。

### 新規sessionの作成の場合
#### メニューバー：FCSの作業データを置きたい場所を指定 

File -> Session -> New
1. Project Folder：FCSの作業データを置きたい場所を指定 
2. Actor：モーションキャプチャアクター名 
3. character：3Dモデルのキャラクター名
4. Maya scene：3DモデルのMayaシーンへのパス
5. Maya Base：Assets、workspace.melがあるフォルダへのパス


##### Project Folderの設定
Browse ボタンでFCSの作業データフォルダを格納する場所
＝Project Folder
を指定するためウィンドウを起動

##### Drive　ボタンで
1. 作業者PC環境のローカルネットワークドライブを表示  
2. Project Folderを作成したい場所を選択
3. OK  
Project Folderに指定した場所が反映されていたら
Create
問題なく作成できたら画像のポップアップが出ます

close

- New...：sessionの新規作成  
- Open：作成済みのsessionを開く  
- Info：
- Save：
- Advanced：開いたsessionのキャッシュを全て削除する
- Setting：UIやMayaでの出力物等の設定を確認・変更する。詳細は後述
- Quit：FCSを終了する

#### Create new Sessionで作成されるフォルダ構造
赤枠：Project Folderで作成されるフォルダ  
青枠：Actorで作成されるフォルダ  
緑枠：Characterで作成されるフォルダ  
.lock：共同作業を防止するロックファイル
fcs_session.yaml：sessionをSaveした後に作成されるファイル  


#### 既存のSessionを開く

Settingを変更できます

```{warning}
変更したsettingsは、FCS再起動後に反映されます
```
きどうが終わりました。

テストを開始します。