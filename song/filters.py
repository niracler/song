import django_filters
from .models import Song


class SongFiliter(django_filters.rest_framework.FilterSet):
    """电歌曲的api的过滤器"""
    mid = django_filters.CharFilter(field_name='mid')
    name = django_filters.CharFilter(field_name='name')
    created = django_filters.CharFilter(field_name='created')

    class Meta:
        model = Song
        fields = [
            'mid', 'name', 'created'
        ]
