from django.db import models
from django.utils import timezone

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
    area = models.CharField(max_length=32, default='未知', verbose_name='地区')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        ordering = ('-sid',)
        db_table = 'song_song'
        verbose_name = '歌曲'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class SongFav(models.Model):
    """用户收藏的文章的关系类"""

    fid = models.BigAutoField(primary_key=True, verbose_name='ID')
    username = models.CharField(max_length=64, verbose_name='用户名')
    song = models.ForeignKey(Song, on_delete=models.DO_NOTHING, verbose_name="歌曲")
    created = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    class Meta:
        ordering = ('-created',)
        verbose_name = "歌曲收藏"
        verbose_name_plural = verbose_name
        unique_together = ("username", "song")

    def __str__(self):
        return self.username
