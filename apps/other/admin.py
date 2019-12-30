from django.contrib import admin

# Register your models here.

from .models import UserOperation, VisitorCount, Comment, User


# Register your models here.
@admin.register(UserOperation)
class UserOperationAdmin(admin.ModelAdmin):
    """管理类"""
    list_display = ('id', 'uid', 'time_local', 'res_type')
    list_filter = ('res_type','time_local')
    search_fields = ('res_id',)
    date_hierarchy = 'time_local'
    ordering = ('time_local', 'uid')


@admin.register(VisitorCount)
class VisitorCountAdmin(admin.ModelAdmin):
    """管理类"""
    list_display = ('id', 'vis_type', 'res_type', 'res_id', 'click', 'time_type', 'time_local')
    list_filter = ('res_type', 'vis_type', 'time_type', 'time_local')
    search_fields = ('res_type',)
    date_hierarchy = 'time_local'
    ordering = ('time_local',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """管理类"""
    list_display = ('cid', 'content', 'uid')
    list_filter = ('created',)    
    date_hierarchy = 'created'
    ordering = ('cid',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """管理类"""
    list_display = ('uid', 'name', 'email', 'status')
    list_filter = ('status', 'created')
    date_hierarchy = 'created'
    ordering = ('uid',)
