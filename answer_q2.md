## Q2の解説

1. Q2はdjangoのmanage.pyでrunserverコマンドを実行できるかの問題です。
  - https://docs.djangoproject.com/ja/3.0/ref/django-admin/#runserver

2. `cd ./universe` をターミナルで叩きます。
  - この`cd`コマンドはディレクトリを移動するコマンドです。
  - `manage.py`が存在する`universe`ディレクトリまで移動しています。

3. `python manage.py runserver` をコマンドで叩きます。
  - `python manage.py`は通常のpythonファイルの実行です。
  - `manage.py`というファイルに`runserver`という引数を与えて実行しています。

4. `http://127.0.0.1:8000/` にアクセスしてロケットの画面が表示されていれば正解です。
  - これはDjangoを自分のパソコンの8000番ポートで起動していることを意味しています。
  - `python manage.py runserver 8001`を実行すると8001番ポートで起動します。
  - ポートについては[この記事](https://wa3.i-3-i.info/word1774.html)を参考にしてみてください。今は、8000番のドアをノックするとDjangoからの返事がもらえるということになりますね。
