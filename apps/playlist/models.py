from django.db import models

# Create your models here.
from song.models import Song


class Tag(models.Model):
    tid = models.BigAutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=32, unique=True, verbose_name='标签名')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        ordering = ('-tid',)
        db_table = 'song_tag'

    def __str__(self):
        return self.name

class PlayList(models.Model):
    lid = models.BigAutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=128, verbose_name='歌单名称')
    tracks = models.ManyToManyField(Song, related_name='tracks', verbose_name='歌曲列表')
    creator = models.CharField(default='niracler4', max_length=64, verbose_name='创建者用户名')
    tags = models.ManyToManyField(Tag, related_name='playlist_tag', verbose_name='标签')
    cimg = models.ImageField(upload_to='cimg', default='cimg/default.jpg', verbose_name='封面')
    click = models.BigIntegerField(default=0, verbose_name='点击次数')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    description = models.TextField(verbose_name='歌单描述')

    class Meta:
        ordering = ('-lid',)
        db_table = 'song_playlist'
        verbose_name = '歌单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name