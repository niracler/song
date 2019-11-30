import django_filters

from song.models import PlayList, Tag


class PlayListFilter(django_filters.rest_framework.FilterSet):
    """歌单的api的过滤器"""
    lid = django_filters.CharFilter(field_name='lid')
    name = django_filters.CharFilter(field_name='name')
    created = django_filters.CharFilter(field_name='created')
    tags = django_filters.CharFilter(method='tags_filter', field_name='tags')

    class Meta:
        model = PlayList
        fields = ['lid', 'name', 'created', 'tags']

    # 查找指定标签下的所有歌单
    def tags_filter(self, queryset, name, value):
        try:
            tag = Tag.objects.get(name=value)
        except Exception as e:
            print(e)
            tag = Tag()
        return queryset.filter(tags__in=[tag])
