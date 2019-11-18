from django.db import models


# Create your models here.

class Song(models.Model):
    sid = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=128, verbose_name='歌曲名称')
    url = models.CharField(max_length=256, verbose_name='歌曲链接')
    created = models.DateTimeField(verbose_name='创建时间')

    class Meta:
        ordering = ('-sid',)
        db_table = "t_song"

    def __str__(self):
        return self.name
