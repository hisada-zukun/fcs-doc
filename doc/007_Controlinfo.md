## Contorol Infoの登録方法
コントローラーやRegion、最大値最小値を登録します
★ 最大値最小値は自動で入力されますが、値があまりにも大きすぎる場合は調整を行って下さい
★数値表記ではなく　True/False表記のものが紛れ込んでいると正常に動作しなくなるためRemoveをしてください

一覧
- all▼：all/upper/lower/gaze/eyelid/null　指定した項目（部位の区分）を絞り込んで表示
- Add selected：選択したコントローラーを登録
- Sync：✅数値操作をMayaと連動する/✅解除　しない
- （入力項目）/select：コントローラー名を入力し、selectを選択するとMaya上で対応するコントローラーが選択される
- Upper/…/eyelid：Region　部位の区分ごとにコントローラーを登録します
- Remove：☑を入れたコントローラーを削除する
- select All/Unselect All：controller上に表示されているコントローラーすべてに☑/☑解除
- ▼Advanced　Remove empty：Regionが登録されていないコントローラー(null)を削除する
- ▼Advanced　Delete all：追加・登録したコントローラー情報をすべて削除する
- ▼Advanced　Reset：Saveされているデータの状態に戻す

- save：controller Infoを登録。Regionが4項目登録されていないと実行できない。

controllerの登録
★！！必須！！ ・全てのRegionの登録
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


### Upperの登録方法 
Mayaでupperに登録したいコントローラーを選択し

FCSに戻り
・Add selected
★ Add selectedを押しても何も表示されない場合、モジュールのインストールを行っていない可能性があります。

Mayaで選択したコントローラーが「controller」に表示されるので
・select All（=全選択）でupperに登録したいコントローラーを選択
※null＝Regionが未指定

今回はupperに登録したいので
・Upper
を選択

Regionにupperと表示されたら登録完了！

### Gazeの登録方法
Mayaで
・gazeに登録したいコントローラーを選択し

・Add selected

Upperの下にAdd selectedで追加したコントローラーが表示されます

・右上のall▼のタブを選択し、null▼に変更する
Upperに登録したものを非表示にし、先程追加したコントローラーのみ表示させる

★ allのままだと　upperも表示されているためselect Allするとupperも選択される。
間違って全選択してしまった場合はUnselect Allで選択解除可能。

nullにすることで登録されていない項目が絞り込まれるのでUpperと同様に
・select All（=全選択）
で✅を入れ
※手動でも✅できますが、数が多い時には手間になります

・gaze
※対応するRegionを登録
★ nullで絞り込んでいるのでRegionを登録すると非表示になります

allに戻すとすべて表示されます
 再表示したい場合の例なので、すべて登録するまでnullのままでも問題ありません。また、登録したRegionで絞り込むこともできます。


### Eyelidの登録方法
同様に
・ eyelidに登録したいコントローラーを選択し

・ Add selected

登録済みのコントローラーの下に追加したコントローラーが表示されます

・ 右上のall▼のタブを選択し、null▼に変更する
★nullから変更していない場合はこの手順はスキップ

・ select All

・ eyelid


### Lowerの登録方法
Mayaでupperに登録したい コントローラーを選択し
lowerに登録したいコントローラーをAdd selected→All select→lower

・Add selected
登録済みのコントローラーの下に追加したコントローラーが表示されます

・select All

・Lower

Upper/Lower/Gaze/Eyelidをすべて登録し終えたら
・save

※未登録状態のものがあるとSave出来ません

★セーブできない場合
登録すべきものか確認後
・削除したい項目に✅→Remove
・▼Advenced　Remove empty
で削除

### トラブルシューティング
・Add selectでコントローラーの追加ができない　
SyncでMayaと連動しない

モジュールのインストールが行われていない場合
このような現象が起こります。

・モジュールのインストールを行ったか
・インストールしたバージョンがMayaシーンと一致しているか
確認してください。

### コントローラーの登録順番を変える場合
SyncでMayaと連動しない
L/R　blinkが離れていて不便なので
blinkを上下（隣接するよう）に並べたい

・並び替えたいコントローラーをドラッグ

ドラッグしたまま
・コントローラー名の上でドロップ

blinkが隣接

変更内容をSaveした状態まで戻したい場合は
・Reset
controller info登録時の順番に戻る

作業しやすいように並び替えたら
・Save

