## Mayaの起動

・FCS起動時にMayaを起動/別作業を行っていた場合は終了させるを実行後、FCSからMayaを起動します。

```{warning}
※上記作業を実行しなかった場合、正常に動作しない可能性があります。
```

![](images/M001.png)  
OpenScene：Mayaシーンを起動  
Launch：Mayaを起動   
Sync：✅Mayaと連動させる   


・Maya▶Launch▶Mayaバージョンの選択でMayaを起動  
例：マニュアルでキャラクターデータを作成したMayaのバージョンはMaya2020なので2020を選択
![](images/M002.png)

```{note}
・Launchをクリックすることでsession作成時に設定したMayaSceneが自動で起動します  
・OpenSceneをクリックすると、設定したMayaSceneを開き直すことができます  
・Mayaバージョンの誤クリックを防ぐため、session作成時に設定したMayaVersion以外はクリックできないように、ブラックアウトしています
```

```{warning}
Launchで指定したMayaバージョンが開けない場合は…
```
session作成時に設定した項目は File▶Session▶info で確認することができます  
![](images/S014.png)

New Sessionで設定したMaya Verがinfoで反映されていない場合は、info画面のMaya versionを右クリックし、Editから変更ができます
![](images/S015.png)
![](images/S016.png)

