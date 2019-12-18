from django.db.models import Count

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin, ListModelMixin, CreateModelMixin, \
    RetrieveModelMixin
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .models import PlayList, Tag, PlayListFav
from utils.pagination import Pagination
from utils.permissions import IsAuthenticatedOrSearchAndTagsOnly, IsOwnerOrReadOnly
from .serializers import PlayListSerializer, PlayListDetailSerializer, TagSerializer, PlaylistFavSerializer, PlaylistFavCreateSerializer
from .filters import PlayListFilter


class PlaylistFavViewSet(viewsets.GenericViewSet, CreateModelMixin, DestroyModelMixin, ListModelMixin):
    """用户收藏的功能的视图"""
    queryset = PlayListFav.objects.all()
    pagination_class = Pagination
    permission_classes = (IsOwnerOrReadOnly,)

    def get_serializer_class(self):
        if self.action == "create":
            return PlaylistFavCreateSerializer
        else:
            return PlaylistFavSerializer

    def get_queryset(self):
        """只取当前用户"""
        username = self.request.query_params.get("username", False)
        if username:
            username = username[0]
            return PlayListFav.objects.filter(username=username)
        elif self.request.myuser:
            username = self.request.myuser.username
            return PlayListFav.objects.filter(username=username)
        else:
            return []


class PlayListViewSet(CacheResponseMixin, viewsets.GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin,
                      UpdateModelMixin,
                      DestroyModelMixin):
    queryset = PlayList.objects.all()
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = PlayListFilter
    permission_classes = (IsAuthenticatedOrSearchAndTagsOnly,)
    search_fields = ('name', 'description')
    ordering_fields = ('lid', 'name', 'created')

    def get_queryset(self):
        """有的情况下只取当前用户"""
        is_search = self.request.query_params.get("search", False)
        is_self = self.request.query_params.get("isSelf", False)
        is_tags = self.request.query_params.get("tags", False)

        if bool(
                (self.action == 'retrieve') or
                (not self.request.myuser and is_search) or  ## 没有登录并且是查找
                (is_search and not is_self) or  ## 查找,并且不是查找自己
                (is_tags and not is_self)
        ):
            return PlayList.objects.all()
        else:
            return PlayList.objects.filter(creator=self.request.myuser.username)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PlayListDetailSerializer
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
