from django.db import models
from .tools import get_songs_path


# Create your models here.

class Song(models.Model):
    sid = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=128, verbose_name='歌曲名称')
    file = models.FileField(upload_to=get_songs_path, verbose_name='歌曲文件链接')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ('-sid',)
        db_table = "t_song"

    def __str__(self):
        return self.name
