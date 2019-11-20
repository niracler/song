from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin, \
    RetrieveModelMixin
from .models import Song, Author, PlayList
from .filters import SongFiliter, AuthorFiliter, PlayListFiliter
from .serializers import SongListSerializer, SongSerializer, SongCreateSerializer, AuthorSerializer, \
    AuthorCreateSerializer, PlayListCreateSerializer, PlayListSerializer


# Create your views here.

class Pagination(PageNumberPagination):
    """用于内容分页的类"""
    page_size = 50
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 300


class SongViewSet(viewsets.GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,
                  DestroyModelMixin):
    queryset = Song.objects.all()
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = SongFiliter
    search_fields = ('sid', 'name')
    ordering_fields = ('sid', 'name', 'created')

    def get_serializer_class(self):
        if self.action == "list":
            return SongListSerializer
        elif self.action == "create":
            return SongCreateSerializer
        return SongSerializer


class AuthorViewSet(viewsets.GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,
                    DestroyModelMixin):
    queryset = Author.objects.all()
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = AuthorFiliter
    search_fields = ('aid', 'name')
    ordering_fields = ('aid', 'name', 'created')

    def get_serializer_class(self):
        if self.action == "list":
            return AuthorSerializer
        elif self.action == "create":
            return AuthorCreateSerializer
        return AuthorSerializer


class PlayListViewSet(viewsets.GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,
                      DestroyModelMixin):
    queryset = PlayList.objects.all()
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = PlayListFiliter
    search_fields = ('lid', 'name')
    ordering_fields = ('lid', 'name', 'created')

    def get_serializer_class(self):
        if self.action == "list":
            return PlayListSerializer
        elif self.action == "create":
            return PlayListCreateSerializer
        return PlayListSerializer
