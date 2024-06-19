## Contorollerの登録

Window▶ControllerでConrollerウィンドウが起動します。  
Contollerウィンドウでは、接続しているMayaSceneのコントローラーリグを登録することができます。

FCSでは顔のパーツ区分のことをRegionと呼びます。  
アニメーション解析のため、upper、eyelid、gaze、lowerにそれぞれコントローラーリグを１つ以上登録してください。  

また、コントローラーリグの登録時にRegionの最大値最小値も登録できます。
![](images/C001.png)


```{note}
最大値最小値は自動で入力されますが、値があまりにも大きすぎる場合は調整を行って下さい  
```
```{warning}
数値ではない(True/False)アトリビュートがあると正常に動作しないため、登録から除外してください。
```

![](images/C002.png)

一覧  
all▼：all/upper//eyelid/gaze/lower/null　指定した項目（部位の区分）を絞り込んで表示  

Maya  
Add selected：選択したコントローラーを登録  
Sync：✅数値操作をMayaと連動する/✅解除しない  

Selected  
upper/eyelid/gaze/lower：Region　部位の区分ごとにコントローラーを登録します  
Remove：✅を入れたコントローラーを削除する  
select All/Unselect All：controller上に表示されているコントローラーすべてに✅/✅解除 

▼Advanced  
Remove empty：Regionが登録されていないコントローラー(null)を削除する  
Delete all：追加・登録したコントローラー情報をすべて削除する  
Reset：Saveされているデータの状態に戻す

 save：controller Infoを登録。

### controllerの登録

#### upperの登録方法 

Mayaでupperに登録したいコントローラーを選択し
![](images/image36.png)

FCSに戻り  
・Add selected
![](images/C003.png)


Mayaで選択したコントローラーが「controller」に表示されるので  
・select All（=全選択）でupperに登録したいコントローラーを選択  
※null＝Regionが未指定
![](images/C004.png)

今回はupperに登録したいので  
・upperを選択  
Regionにupperと表示されたら登録完了！
![](images/C005.png)

#### eyelidの登録方法

Mayaで  
・eyelidに登録したいコントローラーを選択し
![](images/image49.png)

・Add selected  
Upperの下にAdd selectedで追加したコントローラーが表示されます
![](images/C006.png)

・右上のall▼のタブを選択し、null▼に変更する  
　upperに登録したものを非表示にし、先程追加したコントローラーのみ表示させる
![](images/C007.png)

```{note}
★allのままだとupperも表示されているためselect Allするとupperも選択される。  
間違って全選択してしまった場合はUnselect Allで選択解除可能。
```

nullにすることで登録されていない項目が絞り込まれるのでupperと同様に  
・select All（=全選択）で✅を入れます  
※手動でも✅できますが、数が多い時には手間になります
![](images/C008.png)

・eyelid  
※対応するRegionを登録
![](images/C009.png)
```{note}
★ nullで絞り込んでいるのでRegionを登録すると非表示になります
```


allに戻すとすべて表示されます
![](images/C010.png)


```{note}
再表示したい場合の例なので、すべて登録するまでnullのままでも問題ありません。  
また、登録したRegionで絞り込むこともできます。
```

#### gazeの登録方法

同様に  
・gazeに登録したいコントローラーを選択し
![](images/image47.png)

・Add selected
登録済みのコントローラーの下に追加したコントローラーが表示されます
![](images/C011.png)

・右上のall▼のタブを選択し、null▼に変更する
```{note}
★nullから変更していない場合はこの手順はスキップ
```
![](images/C012.png)

・select All
![](images/C013.png)

・gaze
![](images/C014.png)
```{note}
★ nullで絞り込んでいるのでRegionを登録すると非表示になります
```

#### lowerの登録方法

同様に  
Mayaでlowerに登録したいコントローラーを選択し  
![](images/image60.png)

・Add selected
```{note}
★ 前段でnullで絞り込んでいるのでnullのみが表示されます
```
![](images/C015.png)

・select All
![](images/C016.png)

・lower
![](images/C017.png)
```{note}
★ nullで絞り込んでいるのでRegionを登録すると非表示になります
```

Upper/Lower/Gaze/Eyelidをすべて登録し終えたら  
・save
![](images/C018.png)

```{warning}
※未登録状態のものがあるとSave出来ません
```

```{note}
★セーブできない場合
```
登録すべきものか確認後  
・削除したい項目に✅→Remove  
![](images/C019.png)
・nullのままのコントローラーを一括削除
![](images/C020.png)
で削除

### トラブルシューティング

#### マニュアル以外のコントローラーを登録したい場合
本マニュアルでは、UnrealEngineのMetahumanを使用していますが、  
別の3DCG作成ソフトで作成したものでも、各部位に連携できるコントローラーリグがあれば対応可能です。  
また、必要最低限のコントローラーのみを登録していますので、  
任意で登録するコントローラーを増やすことができます。


#### Add selectでコントローラーの追加ができない場合
```{warning} 
設定したMayaバージョンとsceneを作成したMayaバージョンが一致しているか確認してください。
```
#### コントローラーの登録順番を変えたい場合

例：L/R　blinkが離れていて不便なのでblinkを上下（隣接するよう）に並べたい
```{note}
並び替えたいコントローラーをドラッグしドロップで順番を変更できます。  
ドラッグしたままコントローラー名の上でドロップ
```
#### コントローラーの登録順番を変えたい場合
 
・Reset  
controller info登録時の順番に戻る
![](images/C021.png)

作業しやすいように並び替えたら  
・Save
![](images/C018.png)
