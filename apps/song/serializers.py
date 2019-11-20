from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Song, Author, PlayList


class AuthorSerializer(serializers.ModelSerializer):
    """关于作者的序列化函数"""

    class Meta:
        model = Author
        fields = "__all__"


class AuthorCreateSerializer(serializers.ModelSerializer):
    """关于作者创建的序列化函数"""

    aid = serializers.IntegerField(label='ID', validators=[UniqueValidator(queryset=Author.objects.all())],
                                   help_text='空的话， 就是自增序列', required=False)
    name = serializers.CharField(label="作者名", required=True, allow_blank=False)

    class Meta:
        model = Author
        fields = ('aid', 'name')


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
    sid = serializers.IntegerField(label='ID', validators=[UniqueValidator(queryset=Song.objects.all())],
                                   help_text='空的话， 就是自增序列', required=False)

    class Meta:
        model = Song
        fields = ('sid', 'name', 'file', 'authors')


class PlayListSerializer(serializers.ModelSerializer):
    """关于歌曲的序列化函数"""
    tracks = SongSerializer(many=True)

    class Meta:
        model = PlayList
        fields = "__all__"


class PlayListCreateSerializer(serializers.ModelSerializer):
    """关于歌曲创建的序列化函数"""

    lid = serializers.IntegerField(label='ID', validators=[UniqueValidator(queryset=PlayList.objects.all())],
                                   help_text='空的话， 就是自增序列', required=False)

    class Meta:
        model = PlayList
        fields = ('lid', 'name', 'tracks')
