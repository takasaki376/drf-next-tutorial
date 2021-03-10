from django.urls import path, re_path
from django.conf.urls import include
from rest_framework import routers
from .views import BlogViewSet ,BlogListView

# ModelViewSet はrouterに定義する事でCRUD処理に応じたメソッドと紐づく
router = routers.DefaultRouter()
router.register('blog',BlogViewSet)

# generics などModelViewSet以外はurlpatternsの中に定義する
urlpatterns = [
    re_path('bloglist', BlogListView.as_view(), name='bloglist'),
    path('', include(router.urls)),
]