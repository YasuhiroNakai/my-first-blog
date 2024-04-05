# 他ファイルの参照
from django.conf import settings
from django.db import models
from django.utils import timezone

# Postのオブジェクトを定義
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # ブログを公開するメソッド
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    # ポストのタイトルのテキストを返す
    def __str__(self):
        return self.title