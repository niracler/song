from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from author.filters import AuthorFiliter
from author.serializers import AuthorSerializer
from .models import Author
from utils.pagination import Pagination


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
        return AuthorSerializer