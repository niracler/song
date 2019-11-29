from django.db.models import Count
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin, \
    RetrieveModelMixin
from .models import Song, Author, PlayList, Comment, Tag
from .filters import SongFiliter, AuthorFiliter, PlayListFiliter
from .serializers import SongListSerializer, SongSerializer, SongCreateSerializer, AuthorSerializer, \
    AuthorCreateSerializer, PlayListCreateSerializer, PlayListSerializer, TagSerializer, CommentSerializer, \
    PlayListUpdateSerializer, SongUpdateSerializer
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from utils.permissions import IsOwnerOrReadOnly, IsSongAuthenticated


# Create your views here.

class Pagination(PageNumberPagination):
    """用于内容分页的类"""
    page_size = 10
    page_size_query_param = 'ps'
    page_query_param = 'p'
    max_page_size = 300


class TagViewSet(CacheResponseMixin, viewsets.GenericViewSet, ListModelMixin):
    tag_queryset = Tag.objects.all()
    queryset = tag_queryset.annotate(num_times=Count('playlist_tag'))
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('tid', 'name', 'times', 'created')

    def get_serializer_class(self):
        return TagSerializer


class CommentViewSet(CacheResponseMixin, viewsets.GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin):
    queryset = Comment.objects.all()
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('cid', 'body')
    ordering_fields = ('cid', 'body', 'created')

    def get_serializer_class(self):
        if self.action == "list":
            return CommentSerializer
        elif self.action == "create":
            return CommentSerializer
        return CommentSerializer


class SongViewSet(CacheResponseMixin, viewsets.GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin,
                  UpdateModelMixin,
                  DestroyModelMixin):
    """
    List:只能获取到自己上传的数据
    Retrieve:可以获得别人上传的歌曲
    """

    queryset = Song.objects.all()
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = SongFiliter
    permission_classes = (IsSongAuthenticated,)
    # authentication_classes = ()
    search_fields = ('name',)
    ordering_fields = ('sid', 'name', 'created')

    def get_queryset(self):
        """只取当前用户"""
        if self.action in ("list", "update"):
            return Song.objects.filter(creator=self.request.myuser.id)
        else:
            return Song.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return SongListSerializer
        elif self.action == "create":
            return SongCreateSerializer
        elif self.action == "retrieve":
            return SongListSerializer
        elif self.action == "update":
            return SongUpdateSerializer
        return SongSerializer


class AuthorViewSet(CacheResponseMixin, viewsets.GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin):
    author_queryset = Author.objects.all()
    queryset = author_queryset.annotate(songs=Count('song_author'))
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = AuthorFiliter
    search_fields = ('name',)
    ordering_fields = ('aid', 'name', 'created', 'songs')

    def get_serializer_class(self):
        if self.action == "list":
            return AuthorSerializer
        elif self.action == "create":
            return AuthorCreateSerializer
        return AuthorSerializer


class PlayListViewSet(CacheResponseMixin, viewsets.GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin,
                      UpdateModelMixin,
                      DestroyModelMixin):
    queryset = PlayList.objects.all()
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = PlayListFiliter
    search_fields = ('name', 'description')
    ordering_fields = ('lid', 'name', 'created')

    def get_serializer_class(self):
        if self.action == "list":
            return PlayListSerializer
        elif self.action == "create":
            return PlayListCreateSerializer
        elif self.action == "update":
            return PlayListUpdateSerializer
        return PlayListSerializer
