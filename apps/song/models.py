from django.db import models

from author.models import Author
from .tools import get_songs_path


# Create your models here.


class Song(models.Model):
    sid = models.BigAutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=128, verbose_name='歌曲名称')
    file = models.FileField(upload_to=get_songs_path, verbose_name='歌曲文件链接')
    authors = models.ManyToManyField(Author, related_name='song_author', verbose_name='作者')
    cimg = models.ImageField(upload_to='cimg', default='cimg/default.jpg', verbose_name='封面')
    click = models.BigIntegerField(default=0, verbose_name='点击次数')
    lyric = models.TextField(default=None, verbose_name='歌词')
    creator = models.CharField(default='niracler4', max_length=64, verbose_name='创建者用户名')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        ordering = ('-sid',)
        db_table = 'song_song'
        verbose_name = '歌曲'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



