## Contorol Infoの登録方法
コントローラーやRegion、最大値最小値を登録します
★ 最大値最小値は自動で入力されますが、値があまりにも大きすぎる場合は調整を行って下さい
★数値表記ではなく　True/False表記のものが紛れ込んでいると正常に動作しなくなるためRemoveをしてください

一覧
・all▼：all/upper/lower/gaze/eyelid/null　指定した項目（部位の区分）を絞り込んで表示
・Add selected：選択したコントローラーを登録
・Sync：✅数値操作をMayaと連動する/✅解除　しない
・（入力項目）/select：コントローラー名を入力し、selectを選択するとMaya上で対応するコントローラーが選択される
・Upper/…/eyelid：Region　部位の区分ごとにコントローラーを登録します
・Remove：☑を入れたコントローラーを削除する
・select All/Unselect All：controller上に表示されているコントローラーすべてに☑/☑解除
・▼Advanced　Remove empty：Regionが登録されていないコントローラー(null)を削除する
・▼Advanced　Delete all：追加・登録したコントローラー情報をすべて削除する
・▼Advanced　Reset：Saveされているデータの状態に戻す

・save：controller Infoを登録。Regionが4項目登録されていないと実行できない。

controllerの登録
★！！必須！！ ・全てのRegionの登録
例：upper→gaze→eyelid→Lower ※Lowerは設定数が多いので今回の例では後回しにしています
upper：眉を動かすコントローラー（赤） gaze：眼球・目線を動かすコントローラー（緑） eyelid：まぶたを動かすコントローラー（黄） lower：口・顎・頬等を動かすコントローラー（青）
★一例ですが頬の動きと共にまぶたが動く仕組みの3Dモデルもあるので、 その場合 ・eyelidに登録するのか ・lowerに登録するのか 規則を固めてから登録を行うと後々楽です。


### Upperの登録方法 

### Gazeの登録方法

### Eyelidの登録方法

### Lowerの登録方法

### トラブルシューティング

### コントローラーの登録順番を変える場合