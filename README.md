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

2. Djangoのサーバーを起動し、'http://127.0.0.1:8000/'でDjangoの初期画面が表示されることを確認せよ

3. Djangoの管理者用のユーザを作成せよ

4. Djangoの「earth」という名前のアプリを作成せよ

5. 'http://127.0.0.1:8000/earth/'というURLを叩いた時に'Hello, World!!'を表示せよ

6. 名前、生年月日、身長(小数点第1位まで)、体重(整数)、血液型(A,B,O,AB)の情報を持つHumanモデルを作成せよ

7. Q4で作成したHumanモデルを基にデータベースにテーブルを作成せよ

8. Humanモデルの全ての情報を入力できるフォームを作成し、'http://127.0.0.1:8000/earth/create_human'というURLでフォームを表示せよ

9.  'http://127.0.0.1:8000/earth/create_human'ページからフォームに以下の情報を入力し、データベースにデータを登録せよ

10. 上記で作成した「佐藤太郎」さんのデータがearth_humanテーブルに作成されていることをsqlite3から確認せよ ※SQL問題

11. 管理画面からHumanモデルに下記のデータを追加せよ

12. Humanモデルの名前を全て表示する一覧ページを'http://127.0.0.1:8000/earth/humans'として作成せよ

13. 'http://127.0.0.1:8000/earth/human/<user_id>/'のURLで、そのuser_idをもつユーザの情報を全て表示せよ




