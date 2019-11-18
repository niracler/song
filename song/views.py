from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from .models import Song
from .filters import SongFiliter
from .serializers import SongSerializer


# Create your views here.

class SongPagination(PageNumberPagination):
    """用于文章内容分页的类"""
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 300


class SongViewSet(viewsets.GenericViewSet, ListModelMixin):
    queryset = Song.objects.all()
    pagination_class = SongPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = SongFiliter
    search_fields = ('mid', 'name')
    ordering_fields = ('mid', 'created')

    def get_serializer_class(self):
        return SongSerializer
