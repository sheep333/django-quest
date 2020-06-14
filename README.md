# 作成途中のため、未完成

## このリポジトリについて
- [Djangoのチュートリアル](https://docs.djangoproject.com/ja/3.0/intro/tutorial01/)をやってみた後に自分で書けるようになっているか試したい人向けのコンテンツ
- チュートリアルで学んでいないことについても[公式ドキュメント](https://docs.djangoproject.com/ja/3.0/)内で検索してDjangoを自分で作れる力をつけましょう
- ※がついている問題はDjangoのドキュメントの中に回答がない場合があります

## Djangoローカル開発環境の構築
python実行のためのローカル環境を構築する

### pyenvのインストール
- https://github.com/pyenv/pyenv#installation

### pipenvのインストール
- https://github.com/pypa/pipenv#installation

### バージョンを指定してpythonをインストール

```
# pyenvでインストールできるpythonを確認
pyenv install --list

# pythonの3.7.6をインストール
pyenv install 3.7.6

# このリポジトリをclone
git clone https://github.com/sheep333/xxxxxx.git

# Pipfileの内容にしたがって仮想環境を構築する
pipenv install --python 3.7.6
```

## Django学習

1. Djangoに「universe」という名前のプロジェクトを作成せよ

1. Djangoのサーバーを起動し、'http://127.0.0.1:8000/'でDjangoの初期画面が表示されることを確認せよ

1. Djangoの管理者用のユーザを作成せよ

1. Djangoの「earth」という名前のアプリを作成せよ

1. 'http://127.0.0.1:8000/earth/'というURLを叩いた時に'Hello, World!!'を表示せよ
  - URLルーティング
  - views.pyの書き方

1. 名前、生年月日、身長(小数点第1位まで)、体重(整数)、血液型(A,B,O,AB)の情報を持つHumanモデルを作成せよ
  - Modelの書き方

1. Q4で作成したHumanモデルを基にデータベースにテーブルを作成せよ
  - makemigrationsコマンド
  - migrateコマンド

1. Humanモデルの全ての情報を入力できるフォームを作成し、'http://127.0.0.1:8000/earth/create_human'というURLでフォームを表示せよ
  - urls.py
  - Formの作成
  - templateへの値の引き渡し

1. 'http://127.0.0.1:8000/earth/create_human'ページからフォームに以下の情報を入力し、データベースにデータを登録せよ
  - 名前: 佐藤太郎、生年月日: 1960/1/1、身長: 178.1cm、体重: 72kg、血液型: A型
  - Createの処理

1. 上記で作成した「佐藤太郎」さんのデータがearth_humanテーブルに作成されていることをsqlite3から確認せよ ※SQL問題

1. 管理画面からHumanモデルに下記のデータを追加せよ
  - 名前: 鈴木花子、生年月日: 1970/1/1、身長: 158.1cm、体重: 53kg、血液型: B型

1. Humanモデルの名前を全て表示する一覧ページを'http://127.0.0.1:8000/earth/humans'として作成せよ

1. 'http://127.0.0.1:8000/earth/human/<user_id>/'のURLで、そのuser_idをもつユーザの情報を全て表示せよ




