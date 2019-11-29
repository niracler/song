from django.db.models import Count
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Song, Author, PlayList, Comment, Tag


# -------------------------标签的序列化函数---------------------------------

class TagSerializer(serializers.ModelSerializer):
    times = serializers.SerializerMethodField(read_only=True)

    def get_times(self, obj):
        queryset = Tag.objects.filter(name=obj.name)
        tags = queryset.annotate(times=Count('playlist_tag'))

        return tags[0].times

    class Meta:
        model = Tag
        fields = "__all__"


# -------------------------评论的序列化函数---------------------------------

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


# -------------------------作者的序列化函数---------------------------------

class AuthorSerializer(serializers.ModelSerializer):
    """关于作者的序列化函数"""

    songs = serializers.SerializerMethodField(read_only=True, method_name='get_songs')

    def get_songs(self, obj):
        queryset = Author.objects.filter(name=obj.name)
        authors = queryset.annotate(songs=Count('song_author'))

        return authors[0].songs

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


# -------------------------歌曲的序列化函数---------------------------------


class AuthorSmallSerializer(serializers.ModelSerializer):
    """关于作者的序列化函数"""

    class Meta:
        model = Author
        fields = ('aid', 'name')


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"


class SongListSerializer(serializers.ModelSerializer):
    """关于歌曲的序列化函数"""
    authors = AuthorSmallSerializer(many=True, read_only=True)

    class Meta:
        model = Song
        fields = "__all__"


class SongCreateSerializer(serializers.ModelSerializer):
    """关于歌曲创建的序列化函数"""
    sid = serializers.IntegerField(label='ID', validators=[UniqueValidator(queryset=Song.objects.all())],
                                   help_text='空的话， 就是自增序列', required=False)
    creator = serializers.IntegerField(label='用户ID', read_only=True)

    class Meta:
        model = Song
        fields = ('sid', 'name', 'file', 'authors', 'creator')

    def create(self, validated_data):
        user = self.context['request'].myuser
        song = super().create(validated_data)
        song.creator = user.id
        song.save()
        return song


class SongUpdateSerializer(serializers.ModelSerializer):
    """关于歌曲修改的序列化函数"""

    class Meta:
        model = Song
        fields = ('name', 'authors')


# -------------------------歌单的序列化函数---------------------------------

class TagSamllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tid', 'name')


class SongSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('sid', 'name', 'file')


class PlayListSerializer(serializers.ModelSerializer):
    """关于歌单的序列化函数"""

    lid = serializers.IntegerField(label='ID', validators=[UniqueValidator(queryset=PlayList.objects.all())],
                                   help_text='空的话， 就是自增序列', required=False)
    tags = serializers.SerializerMethodField()
    stags = serializers.CharField(label="文章标签的字符串", help_text='中间用空格隔开', allow_null=True, allow_blank=True,
                                  write_only=True)
    tracks = serializers.SerializerMethodField(label="歌曲目录")

    def get_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]

    def get_tracks(self, obj):
        if self.context['view'].action == 'retrieve':
            return SongListSerializer(obj.tracks, many=True, context={'request': self.context['request']}).data
        return [song.sid for song in obj.tracks.all()]

    class Meta:
        model = PlayList
        fields = "__all__"
        read_only_fields = ('creator', 'tags')

    def create(self, validated_data):
        tags = validated_data.pop('stags')
        playlist = super().create(validated_data)
        playlist.tags.set(get_tag_list(tags))

        return playlist

    def update(self, instance, validated_data):
        tags = validated_data.pop('stags')
        playlist = super().update(instance, validated_data)
        playlist.tags.set(get_tag_list(tags))

        return playlist


def get_tag_list(tags):
    tag_list = []

    try:
        for tag in tags.split(' '):
            if tag:
                tag, created = Tag.objects.update_or_create(name=tag)
                tag_list.append(tag)
    except Exception as e:
        tag_list = []
        print(e)
    return tag_list
