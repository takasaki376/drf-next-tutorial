# Python
バージョン 3.8  

# ライブラリインストール (仮想環境)
pip install Django==3.1.7   
pip install djangorestframework==3.12.2   
pip install django-cors-headers==3.7.0  

# 設定から仮想環境を選択する

# プロジェクト、アプリ作成 (ターミナルから実行)
django-admin startproject blog .  
django-admin startapp api  

# ローカルサーバ起動
manage.py を右クリック　→　実行  
右上の構成の編集　→　パラメータにrunserverと入力する  
右上の再生ボタン　→　ローカルサーバが起動する  
http://127.0.0.1:8000/ にアクセスしてDjangoのデフォルト画面が起動する  

# setting.py の編集
動作するサーバ設定
```
ALLOWED_HOSTS = ['127.0.0.1']
```

INSTALLED_APPS に追加  
```
    'rest_framework',  
    'api.apps.ApiConfig',  
    'corsheaders',
```
MIDDLEWARE に追加
```
    'corsheaders.middleware.CorsMiddleware',  
```

フロントエンドのURLを定義する行を追加
ここで設定されたURLからのみアクセス可能になり、他のURLの場合はエラーになる。
```
CORS_ORIGIN_WHITELIST = ['http://localhost:3000']
```

###今回やっていないけど、サーバデプロイするならやること  
　次の値を環境変数にもたせる  
　SECRET_KEY：githubに公開しないため  
　DEBUG：ローカルとサーバで設定値を変更するため  
　ALLOWED_HOSTS：ローカルとサーバで設定値を変更するため
　CORS_ORIGIN_WHITELIST：ローカルとサーバで設定値を変更するため
　DATABASES：ローカルとサーバで設定値を変更するため  

# api/models.py の編集
必要なテーブルのmodelを作成する。
テーブルを参照する時の定義であり、マイグレーションにて

# api/admin.py の編集　（Django administrationに表示される）
models.py に定義したモデルを追加する。  
Django administrationに表示させたくない場合は不要  

# マイグレーション (ターミナルから実行)（macは python3 かも）
```
python manage.py makemigrations  
python manage.py migrate
```

# スーパーユーザ作成 (ターミナルから実行)
```
python manage.py createsuperuser
```

Username (leave blank to use 'os loginuser'): [ユーザ名を入力する]  
Email address:  [空白のままEnterキー]  
Password:  [パスワードを入力する]  
Password (Username): [再度パスワードを入力する]    
The password is too similar to the username.  
This password is too short. It must contain at least 8 characters.  
This password is too common.  
Bypass password validation and create user anyway? [y/N]: y  [パスワードが簡単な場合の確認メッセージ]    
Superuser created successfully.  

# ローカルサーバ起動
http://127.0.0.1:8000/admin/ に接続する。  
Django administration　にスーパーユーザでログインする。    
admin.py で定義したmodelに対してGUIでCRUD操作が行える。  

# api/serializers.py 新規作成
RESTでやり取りするデータの入出力を記述する。

# api/views.py の編集
リクエストに対する処理を記述する。  

# urls.py を定義する。
blog/urls.py  
api/urls.py

# 動作確認
http://127.0.0.1:8000/api/blog/  
　GETメソッド：リスト表示されること  
　POSTメソッド：新規登録されること  
http://127.0.0.1:8000/api/blog/pk/  
  ※pkは各データのidの値  
　GETメソッド：該当データが１件表示されること  
　PUTメソッド；更新されること  
　PATCHメソッド：指定した項目のみ更新されること  
　DELETEメソッド：削除されること  
http://127.0.0.1:8000/api/bloglist/    
　GETメソッド：リスト表示されること  
