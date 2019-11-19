from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin, \
    RetrieveModelMixin
from .models import Song
from .filters import SongFiliter
from .serializers import SongSerializer, SongCreateSerializer


# Create your views here.

class SongPagination(PageNumberPagination):
    """用于文章内容分页的类"""
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 300


class SongViewSet(viewsets.GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,
                  DestroyModelMixin):
    queryset = Song.objects.all()
    pagination_class = SongPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = SongFiliter
    search_fields = ('sid', 'name')
    ordering_fields = ('sid', 'created')

    def get_serializer_class(self):
        if self.action == "list":
            return SongSerializer
        elif self.action == "create":
            return SongCreateSerializer
        return SongSerializer
