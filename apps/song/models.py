from django.db import models
from .tools import get_songs_path


# Create your models here.

class Author(models.Model):
    aid = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=128, verbose_name='作者名')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ('-aid',)
        db_table = "t_author"

    def __str__(self):
        return self.name


class Song(models.Model):
    sid = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=128, verbose_name='歌曲名称')
    file = models.FileField(upload_to=get_songs_path, verbose_name='歌曲文件链接')
    authors = models.ManyToManyField(Author, related_name='song_author', verbose_name='作者')
    creator = models.IntegerField(default=1, verbose_name='创建者ID')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ('-sid',)
        db_table = "t_song"

    def __str__(self):
        return self.name


class PlayList(models.Model):
    lid = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=128, verbose_name='歌单名称')
    tracks = models.ManyToManyField(Song, related_name='tracks', verbose_name='歌曲列表')
    creator = models.IntegerField(default=1, verbose_name='创建者ID')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ('-lid',)
        db_table = "t_play_list"

    def __str__(self):
        return self.name
