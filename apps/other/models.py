# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class UserOperation(models.Model):
    uid = models.BigIntegerField()
    remote_addr = models.CharField(max_length=64)
    time_local = models.DateTimeField()
    http_method = models.CharField(max_length=32)
    res_type = models.CharField(max_length=64)
    res_id = models.CharField(max_length=64)
    status = models.CharField(max_length=32)
    body_bytes_sent = models.BigIntegerField()
    http_referer = models.CharField(max_length=128)
    http_user_agent = models.CharField(max_length=256)
    created = models.DateTimeField(blank=True, null=True)
    http_url = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        verbose_name = '用户行为'
        verbose_name_plural = verbose_name
        db_table = 'monitor_user_operation'


class VisitorCount(models.Model):
    vis_type = models.CharField(max_length=32)
    res_type = models.CharField(max_length=64)
    res_id = models.CharField(max_length=64)
    time_type = models.CharField(max_length=32)
    time_local = models.DateTimeField()
    click = models.BigIntegerField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        verbose_name = '浏览量'
        verbose_name_plural = verbose_name
        db_table = 'monitor_visitor_count'


class Comment(models.Model):
    cid = models.AutoField(primary_key=True)
    content = models.CharField(max_length=150)
    created = models.DateTimeField()
    liked_count = models.IntegerField()
    pid = models.IntegerField()
    resource_id = models.BigIntegerField()
    type = models.IntegerField()
    replied_id = models.IntegerField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        db_table = 't_comment'


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=33, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    head_icon = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        db_table = 't_user'
