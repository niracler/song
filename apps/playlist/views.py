from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin, ListModelMixin, CreateModelMixin, \
    RetrieveModelMixin
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .serializers import PlayListSerializer
from song.models import PlayList, Tag
from .filters import PlayListFilter
from utils.pagination import Pagination


class PlayListViewSet(CacheResponseMixin, viewsets.GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin,
                      UpdateModelMixin,
                      DestroyModelMixin):
    queryset = PlayList.objects.all()
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = PlayListFilter
    search_fields = ('name', 'description')
    ordering_fields = ('lid', 'name', 'created')

    def get_serializer_class(self):
        return PlayListSerializer


class TagViewSet(CacheResponseMixin, viewsets.GenericViewSet, ListModelMixin):
    tag_queryset = Tag.objects.all()
    queryset = tag_queryset.annotate(times=Count('playlist_tag'))
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('tid', 'name', 'times', 'created')

    def get_serializer_class(self):
        return TagSerializer
