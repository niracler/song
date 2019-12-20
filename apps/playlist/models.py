from django.utils import timezone
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
        verbose_name = '歌单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class PlayListFav(models.Model):
    """用户收藏的文章的关系类"""

    username = models.CharField(max_length=64, verbose_name='用户名')
    playlist = models.ForeignKey(PlayList, on_delete=models.DO_NOTHING, verbose_name="歌单")
    created = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    class Meta:
        ordering = ('-created',)
        verbose_name = "歌单收藏"
        verbose_name_plural = verbose_name
        unique_together = ("username", "playlist")

    def __str__(self):
        return self.username
