from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin, \
    RetrieveModelMixin

from .models import Song, Comment
from .filters import SongFiliter
from .serializers import SongListSerializer, SongSerializer, CommentSerializer, \
    SongUpdateSerializer
from utils.permissions import IsAuthenticated
from utils.pagination import Pagination


# Create your views here.


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
    permission_classes = (IsAuthenticated,)
    # authentication_classes = ()
    search_fields = ('name',)
    ordering_fields = ('sid', 'name', 'created')

    def get_queryset(self):
        """有的情况下只取当前用户"""
        is_search = self.request.query_params.get("search", False)
        is_all = self.request.query_params.get("all", False)

        if bool(
                (not self.request.myuser and is_search) or  ## 没有登录并且是查找
                (self.request.myuser and is_search and is_all)  ## 登录查找,并查找全部
        ):
            return Song.objects.all()
        else:
            return Song.objects.filter(creator=self.request.myuser.id)

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return SongListSerializer
        elif self.action == "update":
            return SongUpdateSerializer
        return SongSerializer
