import django_filters

from song.models import Author


class AuthorFiliter(django_filters.rest_framework.FilterSet):
    """作者的api的过滤器"""
    aid = django_filters.CharFilter(field_name='aid')
    name = django_filters.CharFilter(field_name='name')
    created = django_filters.CharFilter(field_name='created')

    class Meta:
        model = Author
        fields = ['aid', 'name', 'created']
