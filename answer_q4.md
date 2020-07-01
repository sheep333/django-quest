## Q4の回答

1. Q4はルーティングの設定とviewでの表示が行えるかの問題です。
  - https://docs.djangoproject.com/ja/3.0/intro/tutorial01/#write-your-first-view

2. 画面を表示するためには3つのSTEPを踏みます。
  1. アプリをプロジェクトに追加する
  2. プロジェクトのurls.pyからアプリのurls.pyを呼ぶ
  3. アプリのurls.pyからviewを呼ぶ
  4. viewの中で何らかのHTTPレスポンスを返す

3. まずは「アプリをプロジェクトに追加」します。
  - プロジェクトのsettings.pyにあるINSTALLED_APPSにearthアプリの設定を追加します。
  - 具体的には`earth.apps.EarthConfig`をINSTALLED_APPSに追加するのですが、これはearthアプリのapps.pyのEarthConfigクラスを指しています。

## Tips
### WebサイトのURLを叩いた時に何が起こるのか。
皆さんが普段どこかのWebサイトのURLにアクセスした時に何が起こっているのでしょうか。
ざっくりいうと「HTTPSという約束事で遠くにあるパソコンから指定したファイルをもらい、そのファイルを自分のブラウザ上で表示」しています。
下記のページがわかりやすいので、読んでみてください。

参考: [URLとは(「分かりそう」で「分からない」でも「分かった」気になれるIT用語辞典)](https://wa3.i-3-i.info/word114.html)
参考: [WEBサーバとは(「分かりそう」で「分からない」でも「分かった」気になれるIT用語辞典)](https://wa3.i-3-i.info/word1128.html)

逆にいうとWEBのシステムは、「アクセスされたURLに応じて特定のアクションを行ってファイルを返す」のが基本となります。
つまり、URLごとにどんな処理を行うかを作っていくことになります。

Djangoでは、urls.pyでURLと対応するviewを設定していきます。
viewというのがデータを呼び出したり、データの保存をおこなったりといろんな処理を行う部分です。
今回はこのview部分でHttpResponseを返したり、renderでテンプレートを返したりする処理を行ったわけです。
