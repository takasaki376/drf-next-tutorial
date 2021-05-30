from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    # 件名
    title = models.CharField(max_length=200)
    # コンテンツ
    content = models.TextField()
    # 登録日時
    created_at = models.DateTimeField(auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(auto_now=True)
    # 登録ユーザ
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )