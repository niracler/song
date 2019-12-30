from django.contrib import admin

# Register your models here.

from .models import PlayList, PlayListFav


# Register your models here.
@admin.register(PlayList)
class PlayListAdmin(admin.ModelAdmin):
    """歌单管理类"""
    list_display = ('lid', 'name', 'creator', 'click', 'created', 'updated')
    list_filter = ('creator',)
    search_fields = ('name', 'description')
    date_hierarchy = 'created'
    ordering = ('created', 'name')


@admin.register(PlayListFav)
class PlayListFavAdmin(admin.ModelAdmin):
    """歌单管理类"""
    list_display = ('id', 'username', 'playlist_id', 'created')
    list_filter = ('created',)
    search_fields = ('username', 'playlist_id')
    date_hierarchy = 'created'
    ordering = ('created', 'username')
