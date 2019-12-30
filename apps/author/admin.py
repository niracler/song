from django.contrib import admin

# Register your models here.

from .models import Author


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """管理类"""
    list_display = ('aid', 'name', 'created', 'updated')
    list_filter = ('created',)
    search_fields = ('name', 'description')
    date_hierarchy = 'created'
    ordering = ('created', 'name')
