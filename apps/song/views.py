from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin, \
    RetrieveModelMixin

from .models import Song
from .filters import SongFiliter
from .serializers import SongListSerializer, SongSerializer, \
    SongUpdateSerializer
from utils.permissions import IsAuthenticatedOrSearchOnly
from utils.pagination import Pagination


# Create your views here.


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
    permission_classes = (IsAuthenticatedOrSearchOnly,)
    # authentication_classes = ()
    search_fields = ('name',)
    ordering_fields = ('sid', 'name', 'created')

    def get_queryset(self):
        """有的情况下只取当前用户"""
        is_search = self.request.query_params.get("search", False)
        is_self = self.request.query_params.get("isSelf", False)

        if bool(
                (self.action == 'retrieve') or
                (not self.request.myuser and is_search) or  ## 没有登录并且是查找
                (is_search and not is_self)  ## 查找,并且不是查找自己
        ):
            return Song.objects.all()
        else:
            return Song.objects.filter(creator=self.request.myuser.username)

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return SongListSerializer
        elif self.action == "update":
            return SongUpdateSerializer
        return SongSerializer

    def get_object(self):

        return super().get_object()
