from django.db import models


# Create your models here.

class Author(models.Model):
    aid = models.BigAutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=128, verbose_name='作者名')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    description = models.TextField(default='这人什么都没写', verbose_name='作者描述')

    class Meta:
        ordering = ('-aid',)
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
