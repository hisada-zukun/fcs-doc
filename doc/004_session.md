## FCS使用して作業
### 新規sessionの作成/オープン
FCS起動後、「session」と呼ばれるプロジェクトファイルにアクセスするため
「New...（新規作成）またはOpen（開く）」を実行します。


#### メニューバー：FCSの作業データを置きたい場所を指定 

File -> Session  
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


Settingを変更できます

```{warning}
変更したsettingsは、FCS再起動後に反映されます
```

