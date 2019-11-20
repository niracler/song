from django.db.models import Count
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from taggit.models import Tag
from .models import Song, Author, PlayList, Comment


class TagSerializer(serializers.ModelSerializer):
    num_times = serializers.IntegerField(read_only=True)

    class Meta:
        model = Tag
        fields = "__all__"

    def get_num_times(self, obj):
        queryset = Tag.objects.filter(name=obj.name)
        tags = queryset.annotate(num_times=Count('taggit_taggeditem_items'))

        return tags[0].num_times


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


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
    tracks = SongListSerializer(many=True)
    tags = serializers.SerializerMethodField('get_tags')

    class Meta:
        model = PlayList
        fields = "__all__"

    def get_tags(self, obj):
        tags = []
        for i in obj.tags.all():
            tag = {'id': i.id, 'name': i.name}
            tags.append(tag)
        return tags


class PlayListCreateSerializer(serializers.ModelSerializer):
    """关于歌曲创建的序列化函数"""

    lid = serializers.IntegerField(label='ID', validators=[UniqueValidator(queryset=PlayList.objects.all())],
                                   help_text='空的话， 就是自增序列', required=False)
    tags = serializers.CharField(label="文章标签", help_text="文章标签", required=False)

    class Meta:
        model = PlayList
        fields = ('lid', 'name', 'tags', 'description')

    def create(self, validated_data):

        playlist = PlayList.objects.create(
            lid=validated_data['lid'],
	    name=validated_data['name'],
            description=validated_data['description'],        
)

        try:
            tags = validated_data['tags']
            for tag in tags.split(' '):
                if tag:
                    playlist.tags.add(tag)
            playlist.tags = tags
        except Exception as e:
            playlist.tags = ""

        return playlist


class PlayListUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayList
        fields = ('lid', 'tracks')

    def update(self, instance, validated_data):

        for track in validated_data['tracks']:
            instance.tracks.add(track)

        return instance
