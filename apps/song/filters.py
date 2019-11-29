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


class AuthorFiliter(django_filters.rest_framework.FilterSet):
    """作者的api的过滤器"""
    aid = django_filters.CharFilter(field_name='aid')
    name = django_filters.CharFilter(field_name='name')
    created = django_filters.CharFilter(field_name='created')

    class Meta:
        model = Author
        fields = ['aid', 'name', 'created']


class PlayListFiliter(django_filters.rest_framework.FilterSet):
    """歌单的api的过滤器"""
    lid = django_filters.CharFilter(field_name='lid')
    name = django_filters.CharFilter(field_name='name')
    created = django_filters.CharFilter(field_name='created')
    tags = django_filters.CharFilter(method='tags_filter', field_name='tags')

    class Meta:
        model = PlayList
        fields = ['lid', 'name', 'created', 'tags']

    # 查找指定分类下的所有图书
    def tags_filter(self, queryset, name, value):
        try:
            tag = Tag.objects.get(name=value)
        except Exception as e:
            print(e)
            tag = Tag()
        return queryset.filter(tags__in=[tag])
