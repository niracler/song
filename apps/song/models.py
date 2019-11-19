import os
import uuid
from datetime import datetime

from django.db import models

def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return os.path.join("files", filename)


# Create your models here.

class Song(models.Model):
    sid = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=128, verbose_name='歌曲名称')
    file = models.FileField(upload_to="song/", verbose_name='歌曲文件链接')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ('-sid',)
        db_table = "t_song"

    def __str__(self):
        return self.name
