## Contorol Infoの登録方法

コントローラーやRegion、最大値最小値を登録します

```{note}
★最大値最小値は自動で入力されますが、値があまりにも大きすぎる場合は調整を行って下さい
★数値表記ではなく　True/False表記のものが紛れ込んでいると正常に動作しなくなるためRemoveをしてください
```

![](images/image37.png)
一覧  
all▼：all/upper/lower/gaze/eyelid/null　指定した項目（部位の区分）を絞り込んで表示  
Add selected：選択したコントローラーを登録  
Sync：✅数値操作をMayaと連動する/✅解除しない  
(入力項目)/select：コントローラー名を入力し、selectを選択するとMaya上で対応するコントローラーが選択される  

Upper/…/eyelid：Region　部位の区分ごとにコントローラーを登録します  
Remove：☑を入れたコントローラーを削除する  
select All/Unselect All：controller上に表示されているコントローラーすべてに☑/☑解除 

▼Advanced　Remove empty：Regionが登録されていないコントローラー(null)を削除する  
▼Advanced　Delete all：追加・登録したコントローラー情報をすべて削除する  
▼Advanced　Reset：Saveされているデータの状態に戻す
  
  save：controller Infoを登録。Regionが4項目登録されていないと実行できない。

## controllerの登録

```{warning}
★！！必須！！ 
・全てのRegionの登録
例：upper→gaze→eyelid→Lower 
※Lowerは設定数が多いので今回の例では後回しにしています

upper：眉を動かすコントローラー（赤）
gaze：眼球・目線を動かすコントローラー（緑）
eyelid：まぶたを動かすコントローラー（黄）
lower：口・顎・頬等を動かすコントローラー（青）

★一例ですが頬の動きと共にまぶたが動く仕組みの3Dモデルもあるので、
その場合
・eyelidに登録するのか 
・lowerに登録するのか 
規則を固めてから登録を行うと後々楽です。  
![](images/image64.jpg)
```

### Upperの登録方法 

Mayaでupperに登録したいコントローラーを選択し
![](images/image36.png)

FCSに戻り  
・Add selected

```{warning}
★ Add selectedを押しても何も表示されない場合、モジュールのインストールを行っていない可能性があります。
```

![](images/image38.png)


Mayaで選択したコントローラーが「controller」に表示されるので  
・select All（=全選択）でupperに登録したいコントローラーを選択  
※null＝Regionが未指定
![](images/image46.png)

今回はupperに登録したいので  
・Upperを選択
![](images/image44.png)

Regionにupperと表示されたら登録完了！


### Gazeの登録方法

Mayaで  
・gazeに登録したいコントローラーを選択し
![](images/image47.png)

・Add selected
Upperの下にAdd selectedで追加したコントローラーが表示されます
![](images/image42.png)

・右上のall▼のタブを選択し、null▼に変更する  
Upperに登録したものを非表示にし、先程追加したコントローラーのみ表示させる
![](images/image43.png)

```{note}
★ allのままだと　upperも表示されているためselect Allするとupperも選択される。
間違って全選択してしまった場合はUnselect Allで選択解除可能。
```

nullにすることで登録されていない項目が絞り込まれるのでUpperと同様に  
・select All（=全選択）で✅を入れます  
※手動でも✅できますが、数が多い時には手間になります
![](images/image51.png)

・gaze  
※対応するRegionを登録
```{note}
★ nullで絞り込んでいるのでRegionを登録すると非表示になります
```
![](images/image48.png)


allに戻すとすべて表示されます

```{note}
再表示したい場合の例なので、すべて登録するまでnullのままでも問題ありません。また、登録したRegionで絞り込むこともできます。
```

### Eyelidの登録方法

同様に  
・ eyelidに登録したいコントローラーを選択し
![](images/image49.png)

・ Add selected
登録済みのコントローラーの下に追加したコントローラーが表示されます
![](images/image69.png)

・ 右上のall▼のタブを選択し、null▼に変更する
```{note}
★nullから変更していない場合はこの手順はスキップ
```
![](images/image53.png)

・ select All
![](images/image51.png)

・ eyelid
![](images/image52.png)

### Lowerの登録方法

Mayaでupperに登録したい コントローラーを選択し  
lowerに登録したいコントローラーをAdd selected→All select→lower
![](images/image60.png)

・Add selected
登録済みのコントローラーの下に追加したコントローラーが表示されます
![](images/image61.png)

・select All
![](images/image58.png)

・Lower
![](images/image54.png)

Upper/Lower/Gaze/Eyelidをすべて登録し終えたら  
・save
![](images/image63.png)

```{warning}
※未登録状態のものがあるとSave出来ません
```

```{note}
★セーブできない場合
登録すべきものか確認後
・削除したい項目に✅→Remove
![](images/image66.png)
・▼Advenced　Remove empty
![](images/image65.png)
で削除
```

### トラブルシューティング

```{warning}
・Add selectでコントローラーの追加ができない　
SyncでMayaと連動しない

モジュールのインストールが行われていない場合
このような現象が起こります。

・モジュールのインストールを行ったか
・インストールしたバージョンがMayaシーンと一致しているか確認してください。
```

### コントローラーの登録順番を変える場合
SyncでMayaと連動しない  
L/R　blinkが離れていて不便なのでblinkを上下（隣接するよう）に並べたい

・並び替えたいコントローラーをドラッグ
![](images/image55.png)

ドラッグしたまま
・コントローラー名の上でドロップ

blinkが隣接
![](images/image59.png)

変更内容をSaveした状態まで戻したい場合は  
・Reset  
controller info登録時の順番に戻る
![](images/image76.png)

作業しやすいように並び替えたら  
・Save
![](images/image68.png)
