## Q3の回答

1. Q3はアプリの作成コマンドを叩けるかの問題です。
  - https://docs.djangoproject.com/ja/3.0/intro/tutorial01/#creating-the-polls-app

2. `cd ./universe` をターミナルで叩きます。
  - この`cd`コマンドはディレクトリを移動するコマンドです。
  - `manage.py`が存在する`universe`ディレクトリまで移動しています。

3. `python manage.py startapp earth` をコマンドで叩きます。
  - `python manage.py`は通常のpythonファイルの実行です。
  - `manage.py`というファイルに`startapp earth`という引数を与えて実行しています。
  - こうすることで`earth`という名前のアプリが作成されます。
  - `ls -la`を叩いて`earth`というディレクトリが作成されていることを確認してください。



## Tips
プロジェクトの中にアプリケーションを作っていきます。
プロジェクトとアプリケーションの関係はこちらのブログのご参考という箇所の図がわかりやすいです。
https://tiero.jp/magazine/django-project-init/
ここにあるように、プロジェクトの中にアプリが複数存在する形になります。
今回であればuniverseプロジェクトの中にearthアプリがある、という形になります。

universeプロジェクトの中にあるuniverseディレクトリの中を見てみてください。ここにはDjangoのプロジェクト全体の設定ファイルと大元となるurls.pyなどが存在します。
次に、universeプロジェクトの中にあるearthアプリを見てください。views.pyやapps.pyが存在していますね。
実際の機能はこちらのアプリの中に書いていきます。

さて、次の問題にうつりましょう！！
