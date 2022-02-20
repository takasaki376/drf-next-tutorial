# Python
バージョン 3.8  

# 環境構築手順

## ライブラリインストール (仮想環境)
pip install Django==3.1.7   
pip install djangorestframework==3.12.2   
pip install django-cors-headers==3.7.0  

## 設定から仮想環境を選択する

# プロジェクト、アプリ作成 (ターミナルから実行)
django-admin startproject blog .  
django-admin startapp api  

## ローカルサーバ起動
manage.py を右クリック　→　実行  
右上の構成の編集　→　パラメータにrunserverと入力する  
右上の再生ボタン　→　ローカルサーバが起動する  
http://127.0.0.1:8000/ にアクセスしてDjangoのデフォルト画面が起動する  

## setting.py の編集
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

## api/models.py の編集
必要なテーブルのmodelを作成する。
テーブルを参照する時の定義であり、マイグレーションにて

## api/admin.py の編集　（Django administrationに表示される）
models.py に定義したモデルを追加する。  
Django administrationに表示させたくない場合は不要  

## マイグレーション (ターミナルから実行)（macは python3 かも）
```
python manage.py makemigrations  
python manage.py migrate
```

## スーパーユーザ作成 (ターミナルから実行)
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

## ローカルサーバ起動
http://127.0.0.1:8000/admin/ に接続する。  
Django administration　にスーパーユーザでログインする。    
admin.py で定義したmodelに対してGUIでCRUD操作が行える。  

## api/serializers.py 新規作成
RESTでやり取りするデータの入出力を記述する。

## api/views.py の編集
リクエストに対する処理を記述する。  

## urls.py を定義する。
blog/urls.py  
api/urls.py

## 動作確認
http://127.0.0.1:8000/api/blog/  
　GETメソッド：リスト表示されること  
　POSTメソッド：新規登録されること  
http://127.0.0.1:8000/api/blog/[pk]/  
  ※pkは各データのidの値  
　GETメソッド：該当データが１件表示されること  
　PUTメソッド；更新されること  
　PATCHメソッド：指定した項目のみ更新されること  
　DELETEメソッド：削除されること  
http://127.0.0.1:8000/api/bloglist/    
　GETメソッド：リスト表示されること  

#　ログイン処理追加
## ログイン処理用にライブラリのインストール

```
pip install djoser
pip install djangorestframework-simplejwt
```

## 公式ページ
[djoser](https://djoser.readthedocs.io/en/latest/)
Django認証システムのREST 実装。
djoserライブラリは、 登録、ログイン、ログアウト、パスワードのリセット、アカウントのアクティブ化などの
基本的なアクションを処理する一連のDjango Rest Frameworkビューを提供します。
カスタム ユーザー モデルで動作します。

[djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)


## 認証用のURL追加

\blog\urls.py
```
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
```

## setting.py に認証用の設定追加
JWTの有効期限を設定するためにimportする
```
from datetime import timedelta
```

INSTALLED_APPSにdjoserを追加する
```
INSTALLED_APPS = [
  ...
  'djoser',
]
```


DEFAULT_PERMISSION_CLASSES：各APIのアクセス権のデフォルト設定を変更する
DEFAULT_AUTHENTICATION_CLASSES：認証にJWTを使用する

```
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

SIMPLE_JWT = {
    #フロントエンドから受け取るトークンの最初は"JWT"で始まる （必須）
    'AUTH_HEADER_TYPES':('JWT',),
    #トークンの持続時間をの設定（無くてもよい）
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10)
}

```

## Chromeの拡張ツールをインストールする
JWTの認証済とみなすために使用する
[ModHeader](https://chrome.google.com/webstore/detail/modheader/idgpnmonknjnojddfkpgkljpfnnfcklj?hl=ja)

## 動作確認
- ユーザ作成（POSTのみ）
http://127.0.0.1:8000/auth/users
- トークン作成(djoser)  
http://127.0.0.1:8000/auth/jwt/create  
- ユーザ取得、更新（GET、PUT、PATCH）　※トークン取得済であること
http://127.0.0.1:8000/auth/users/me  
- トークン更新(djoser)  
http://127.0.0.1:8000/auth/jwt/refresh  
http://127.0.0.1:8000/api/blog/  
　GETメソッド：エラーになること
  
※__上記のユーザ作成で、１件はユーザを作成すること__

## models.py修正
import 文追加
```
from django.contrib.auth.models import User
```
```
    # 登録ユーザ
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
```

## マイグレーション (ターミナルから実行)（macは python3 かも）
```
> python manage.py makemigrations  

Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1   ### <- １を選択する
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> 2   ### <- １を選択する(後から追加したユーザをデフォルト値とする)
> python manage.py migrate
```

## アクセス権の個別設定用ファイル作成
- apiフォルダにcustompermissions.pyの新規ファイル作成
```
from rest_framework import permissions

class OwnerPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # GETメソッドの場合は無条件の許可する
        if request.method in permissions.SAFE_METHODS:
            return True
        #  GETメソッド以外は、 owner とログインユーザが一致する場合のみ許可する
        return obj.owner.id == request.user.id
```


## views.py の修正
import 文追加
```
from .custompermissions import OwnerPermission
```

- BlogViewSetに対して、個別設定した権限を設定する
- 登録時にログインユーザを設定する
※下記の * 印の行を追加する
  
```
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
*   permission_classes = (OwnerPermission,)
*
*   def perform_create(self, serializer):
*       serializer.save(owner=self.request.user)
```

## serializers.py
- 登録ユーザを表示項目に追加する
※下記の * 印の行を追加する

```
class BlogSerializer(serializers.ModelSerializer):
    # 登録日時のフォーマット指定と、read_only=Trueをつける事でGETメソッド
    # ではレスポンスを返すがPOST、PUTなど更新時は受け取らない。
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
*   username = serializers.ReadOnlyField(source='owner.username' ,read_only=True)

    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'created_at', 'updated_at'
*                 , 'owner', 'username'
        )
        extra_kwargs = {'owner': {'read_only': True}}
```

## 動作確認

http://127.0.0.1:8000/auth/users
- ユーザ作成（POSTのみ）  
http://127.0.0.1:8000/api/blog/    
-　GETメソッド：データが取得できること  
-　POSTメソッド：エラーになること  
http://127.0.0.1:8000/auth/jwt/create
- トークン作成(djoser)  
http://127.0.0.1:8000/api/blog/  
-　GETメソッド：リスト表示されること  
-　POSTメソッド：新規登録されること  
http://127.0.0.1:8000/api/blog/[pk]/  
  ※pkは各データのidの値  
-　GETメソッド：該当データが１件表示されること  
-　PUTメソッド；更新されること  
-　PATCHメソッド：指定した項目のみ更新されること  
-　DELETEメソッド：削除されること  
http://127.0.0.1:8000/api/bloglist/    
-　GETメソッド：リスト表示されること  
