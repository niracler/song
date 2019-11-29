import django_filters
from .models import Song, Author, PlayList, Tag


class SongFiliter(django_filters.rest_framework.FilterSet):
    """歌曲的api的过滤器"""
    sid = django_filters.CharFilter(field_name='sid')
    name = django_filters.CharFilter(field_name='name')
    creator = django_filters.CharFilter(field_name='creator')
    authors = django_filters.CharFilter(field_name='authors')

    class Meta:
        model = Song
        fields = ['sid', 'name', 'created', 'authors']


