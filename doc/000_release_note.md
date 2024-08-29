# FCS 24.10.01 Release Note
## 新機能
### マニュアル関連
1. 24.07, 24.10など、バージョンごとマニュアルが確認できるようになりました
2. [English manual](https://zukunfcs.github.io/fcs-doc/24.10/en/index.html) (draft) now available

### セットアップ
1. インストーラーができるようになりました
2. ffmpegがシステムにインストールされていない場合、自動的にダウンロードできるようになりました

### Auto Pickup α
[動画から特定のフレームを自動的にGalleryに追加する機能を実装しました。](https://zukunfcs.github.io/fcs-doc/latest/en/012_auto_pickup.html)

### Rocky Linux対応
実験的に、Rocky Linuxのビルドを作成いたしました。
ご興味のある方はご連絡ください。

## 主な修正点
1. ビデオ名をダブルクリックで開けるようになりました
2. タイムラインのドラッグする際に、範囲からカーソルをずらしても動くようになりました
3. FCS初回起動時レイアウトを整理しました
4. 一部のUI設定がFCSを閉じても保存されるようになりました。