from distutils.command.upload import upload
from django.db import models
from embed_video.fields import EmbedVideoField


class Community(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='commu_photo')
    date = models.DateField(auto_now_add=True)
    video = EmbedVideoField()

    def __str__(self):
        return self.title

# 일단 Community 테이블 데이터의 분류로는 title, body , photo, date, (+video_url 추가예정)

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Community, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment