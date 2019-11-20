from rest_framework import serializers
from .models import Song, Author, PlayList


class AuthorSerializer(serializers.ModelSerializer):
    """关于作者的序列化函数"""

    class Meta:
        model = Author
        fields = "__all__"


class AuthorCreateSerializer(serializers.ModelSerializer):
    """关于作者创建的序列化函数"""

    class Meta:
        model = Author
        fields = ('name',)


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"


class SongListSerializer(serializers.ModelSerializer):
    """关于歌曲的序列化函数"""
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Song
        fields = "__all__"


class SongCreateSerializer(serializers.ModelSerializer):
    """关于歌曲创建的序列化函数"""

    class Meta:
        model = Song
        fields = ('name', 'file', 'authors')


class PlayListSerializer(serializers.ModelSerializer):
    """关于歌曲的序列化函数"""
    tracks = SongSerializer(many=True)

    class Meta:
        model = PlayList
        fields = "__all__"


class PlayListCreateSerializer(serializers.ModelSerializer):
    """关于歌曲创建的序列化函数"""

    class Meta:
        model = PlayList
        fields = ('name', 'tracks')
