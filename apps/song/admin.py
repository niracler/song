from django.contrib import admin

# Register your models here.

from .models import Song


# Register your models here.
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    """文章管理类"""
    list_display = ('sid', 'name', 'created', 'updated', 'creator', 'click')
    list_filter = ('area', )
    search_fields = ('name', 'lyric')
    date_hierarchy = 'created'
    ordering = ('created', 'name')
