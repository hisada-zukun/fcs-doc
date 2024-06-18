## Solverの設定方法（プロ向け仕様）
当ページはプロ向けとなります  
アニメーション出力する際に調整できる機能です  
使用しなくてもFCSの機能を使うことができるため、初期値から変更する必要はありません

### Solverの画面説明
![](images/Sol001.png)

▼Global
- ✅Fisheye：魚眼レンズでの撮影の際は✅/広角レンズでの撮影の場合は外す  

▼smoothing：出力するアニメーションキーを滑らかにする機能
- Smoothing：滑らかにする方法。基本的に変更しない。
- Weight：強さ。値が+になるほど強く（滑らかに）、-になるほど弱く（荒く）なる。
- Reps：回数。回数が多いほど滑らかに、少ないほど荒くなる。

▼Post processing
- ✅Enforce annotation：出力アニメーションのうち、Galleryで指定されたフレームを上書きする。
- No Clamp mode：クランプなし
- Hard Clamp mode：最大最小値でアニメーションをクランプする
- Soft Clamp mdoe：最大最小値でアニメーションをクランプした上、スムージングかける

Train：作成したProfileを解析する  
Delete cache：キャッシュ削除
