from django.shortcuts import render
from .serializers import BlogSerializer
from .models import Blog
from rest_framework import viewsets, generics ,permissions
from .custompermissions import OwnerPermission

# ==================================================
# viewsの役割
# RESTでのリクエストに対して処理を行い、レスポンスを返す。
#
# generics
# ListAPIView：一覧
# RetrieveAPIView：キー検索
# CreateAPIView：作成
# UpdateAPIView；更新
# DestroyAPIView：削除
# ListCreateAPIView：一覧＋作成
# RetrieveUpdateAPIView：キー検索＋更新
# RetrieveDestroyAPIView：キー検索＋削除
# RetrieveUpdateDestroyAPIView：キー検索＋更新＋削除
#
# viewsets
# ModelViewSet：一覧＊キー検索＋作成＋更新＋削除
# 参考：https://note.crohaco.net/2018/django-rest-framework-view/
# ==================================================

# querysetで指定したModelのCRUD処理を行う。
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # 検索は誰でもOK、登録、更新、削除は認証エラー
    permission_classes = (OwnerPermission,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# querysetで指定したModelの全件抽出処理を行う。
# ModelViewSetでも可能である。
# urls.pyの書き方が違うので、サンプルとして定義する。
class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # 認証チェックをしない
    permission_classes = (permissions.AllowAny,)


