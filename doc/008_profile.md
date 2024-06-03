## Profileの作成

### Profileの作成の前に...
・解析したい動画を Facial\RecDataフォルダに移動する  
![](images/image62.png)

![](images/image77.png)
```{note}
★デフォルトでは create sessionで作成されたProject Folder が開かれるのでFacial\RecDataフォルダに解析したい動画を保存しておくことを推奨します （必須ではありません）
```

#### 解析動画を開く方法
Videosウィンドウを表示し
・import
![](images/image71.png)

select Videoウィンドウが出るので
・動画が保存されているフォルダを選択
例：D:\sample\MetaNagaki\Facial\RecDataに保存しているので Facial　を選択
![](images/image75.png)

```{note}
★create sessionで作成されたProject Folder内に解析したい動画を保存していない場合はDrivesからパスをたどってください
```

・解析したい動画を選択し
![](images/image67.png)

```{note}
★ Shift+クリックで複数同時にimportできます
```
・OK

Videosウィンドウに解析したい動画が表示されます
![](images/image72.png)

#### Timelineの画面説明

![](images/image74.png)
- Timeline：バーを左右に動かし、ビデオを手動で再生させる
- |< />|：1フレーム前/次に移動する
- >/||：動画再生/一時停止（再生すると一時停止ボタンが表示される）
- +：現在のフレームのデータを　 Galleryに追加する。
- [0]：現在のフレーム数。ダブルクリックで数値入力が可能。指定のフレームへの移動も可能。
- LM：
- Sync：✅でTimeline操作状況をMayaのTimeSliderと一致させる。
- Scale：が小さくなるほどプレビューが鮮明に、が大きくなるほど荒くなります
- Video：Video playerに表示されている動画名

#### Edit Profileの画面説明

![](images/image79.png)
- Sync：✅Mayaと連動させる
- Neutral：✅デフォルトの表情として必ず1つ登録する。
- Enabled：✅解析する素材として使用する\☐ 使用しない  

▼Region
- Upper/Lower/Gaze/Eyelid：✅調整した情報を登録する  

▼Utils
- To Maya：FCS上で操作した値（情報）をMayaへ送る
- From Maya：Mayaで操作した値（情報）をFCSへ送る
- Predict：画像から表情を解析し　Mayaの3Dモデルに反映する機能
- □Landmark：部位の頂点情報  

▼Filter　all/upper/lower/gaze/eyelid：選択した項目でコントローラーを絞り込む
- []：入力した文字でコントローラーを絞り込む  

▼Reset：入力した情報を削除する
- Name：Profileとして登録する名前
- Save：変更した情報を保存する
- 画像部分：Timelineから+で追加した画像（ GalleryからEditしたもの）が表示される
- Name（コントローラー）：Controller Infoで登録したコントローラーが表示される
- Value：コントローラーをどれくらい動かしたか数値として表示される。ドラックスクロールやダブルクリックで調整可能。

### Profileの作成
様々な表情のプロファイルが増えると解析の精度があがります
![](images/image81.png)

解析したい動画を読み込み
・開いた動画(ファイル名)の上で右クリックし
・Open
![](images/image88.png)

Video playerに動画が表示される
![](images/image78.png)



#### Neutralの登録方法
VideoTimelineウィンドウの
・スライダーを動かし
表情の登録を行いたいフレームで止め
・+を押す

![](images/image80.png)

Galleryに指定したフレームの画像が追加される

```{note}
★ 値が0（未登録）のProfileは赤枠
```

Neutral＝3Dモデルのデフォルトの表情なので数値の変更は行わず
・Neutralに✅
・任意の名前に変更し
・Save
![](images/image87.png)

```{note}
★ Neutralの登録が完了すると緑になります
```

#### Mayaで表情を登録する場合
【Neutral以外の表情】
VideoTimelineウィンドウのスライダーを動かし表情の登録を行いたいフレームで止め+を押す
Galleryに指定したフレームの画像が追加される

![](images/image94.png)
```{note}
★ 値が0（未登録）のProfileは赤枠
```

プロファイルの画像を左クリックでEditerを開けます

・Mayaで表情を調節し
![](images/image90.png)

・FromMaya　でMaya上で調整した値を抽出
![](images/image91.png)
 
Mayaでの調整情報がFCSに反映される

```{note}
★ コントローラーの登録忘れがあった場合は再度開いたときに作成した表情と異なる場合があります
その際は、再度登録し忘れたコントローラーを登録しプロファイルの再登録を行ってください
```
 
・Nameを任意の名前に変更し
![](images/image86.png)
```{note}
★名前は必ずしも変更する必要はありません。
```

・Save
![](images/image87.png)

```{warning}
Neutral以外の表情の場合はNeutralの✅をはずす
```

#### FCS上で表情を登録する場合

VideoTimelineウィンドウの
・スライダーを動かし 表情の登録を行いたいフレームで止め
・+を押す
![](images/image85.png)

Editorウインドウに選択した画像が表示される
![](images/image92.png)


```{warning}
Syncに✅を入れていない場合はProfileの自動情報共有が行われないためMaya上は1つ前に登録した表情のままになっている
```
![](images/image83.png)

```{note}
★Syncに✅を入れた状態で開きなおすと デフォルトの表情(登録されている表情)に
★既に✅している場合はスキップ
```

・To Maya　で現在のProfileの数値情報をMayaに送る
![](images/image96.png)

全て0なのでデフォルトの表情に
![](images/image99.png)

絞り込みたい項目（文字含む）のみ表示される
![](images/image93.png)

![](images/image106.png)

#### SyncでFCSとMayaを連動させて登録する場合

Syncに✅を入れ　Mayaと連動させる
![](images/image102.png)

```{note}
★既に✅している場合はスキップ
```

・ダブルクリックで入力モードに切り替え　数値を入力
・ドラッグスクロールで値を調整
![](images/image106.png)

Maya上でリアルタイムに表情を調整することができる
![](images/image111.png)

```{note}
目を閉じる、薄目のプロファイルで黒目が見えないものは登録する際にGazeの✅を外してください
```

```{warning}
解析結果の精度が低下してしまう可能性があります
```

他の部位も同様に
・▼Filterを　all▼→絞り込みたい項目　に変更
![](images/image93.png)

例：今回は眉のぎゅっと絞る動きを作りたいのでupperを選択
目線の動きを付けたい場合は　Gaze
口や鼻などの動きを付けたい場合は　Lower
で絞り込む
![](images/image102.png)

該当するコントローラーの数値を調整する
Maya上で表情が作られる
思い通りの表情が完成したら
Name　を任意の名前に変更し
![](images/image86.png)
```{note}
★名前は必ずしも変更する必要はありません。
```

Save
★赤枠が消えれば登録完了
![](images/image87.png)

#### 作成したProfileをコピー＆ペーストする場合

・コピー元のProfileを作成し
・Save
![](images/image87.png)

Mayaの調整データ例
![](images/image95.png)

コピー先の作成
・スライダーを動かし 表情の登録を行いたいフレームで止め
・+を押す

Editorウィンドウにコピー先の情報を表示した状態に
![](images/image94.png)

※数値が入っていないのでMaya側はデフォルトの表情
![](images/image99.png)

・コピー元の画像上で右クリック
・Override
でコピー元の数値が入力され
![](images/image208.png)

Maya上でも表情が反映される
![](images/image108.png)

調整が必要であれば調整を行い
![](images/image103.png)

・任意の名前に変更し
・Save
![](images/image87.png)

#### PredictでProfileを作成する場合

Galleryの情報を基にProfileの表情を解析してくれる機能。
動画全体を解析するわけではないので注意。

いくつかProfileを登録したら
・SolverでTrain/Load
![](images/image195.png)

```{note}
★Profileの変更や追加を行った場合はTrain
Profileの変更がない場合はLoad
```

VideoTimelineウィンドウの
・スライダーを動かし 表情の登録を行いたいフレームで止め
・+を押す
Galleryに指定したフレームの画像が追加され
Editorウインドウに選択した画像が表示される
![](images/image211.png)

```{note}
★追加してからTrainでも可能 必ずTrain/Loadを行ってから実行
```

・Predict実行
valueの数値が変動し
![](images/image212.png)

MayaにPredict結果が出る
調整し、登録できる内容になったら
![](images/image129.png)


・Save
![](images/image203.png)