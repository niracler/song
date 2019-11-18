import django_filters
from .models import Song


class SongFiliter(django_filters.rest_framework.FilterSet):
    """电歌曲的api的过滤器"""
    sid = django_filters.CharFilter(field_name='sid')
    name = django_filters.CharFilter(field_name='name')
    created = django_filters.CharFilter(field_name='created')

    class Meta:
        model = Song
        fields = [
            'sid', 'name', 'created'
        ]
