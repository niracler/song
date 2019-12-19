import re

from django.db.models import Count
from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator

from utils.utils import CurrentUserDefault
from .models import Song, Author, SongFav


class AuthorSmallSerializer(serializers.ModelSerializer):
    """关于作者的序列化函数"""

    class Meta:
        model = Author
        fields = ('aid', 'name')


class SongSerializer(serializers.ModelSerializer):
    sid = serializers.IntegerField(label='ID', validators=[UniqueValidator(queryset=Song.objects.all())],
                                   help_text='空的话， 就是自增序列', required=False)
    lyric = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    area = serializers.CharField(allow_blank=True, allow_null=True, required=False)

    class Meta:
        model = Song
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].myuser
        song = super().create(validated_data)
        song.creator = user.username
        song.save()
        return song


class SongListSerializer(serializers.ModelSerializer):
    """关于歌曲的序列化函数"""
    authors = AuthorSmallSerializer(many=True, read_only=True)

    class Meta:
        model = Song
        exclude = ('lyric',)


class SongDetailSerializer(serializers.ModelSerializer):
    """关于歌曲的序列化函数"""
    authors = AuthorSmallSerializer(many=True, read_only=True)
    lyric = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Song
        fields = "__all__"

    def get_lyric(self, obj):
        lyric = []
        try:
            res = re.findall(r'\[(.*?)\](.*?)\n', obj.lyric)

            for i in res:
                t = re.findall(r'(.*?):(.*?)\.(..)', i[0])
                if not t: continue

                t = t[0]
                sec = 60 * int(t[0]) + int(t[1]) + int(t[2]) / 100
                lyric.append(
                    {
                        'time': sec,
                        'text': i[1].strip(),
                    }
                )
        except Exception as e:
            print(e)

        return lyric


class SongFavSerializer(serializers.ModelSerializer):
    """用户收藏的序列化函数"""

    username = serializers.HiddenField(
        default=CurrentUserDefault()
    )
    song = SongListSerializer()

    class Meta:
        model = SongFav
        fields = ('username', 'song', 'id')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # check the request is list view or detail view
        # is_list_view = isinstance(self.instance, list)
        # extra_ret = {'key': 'list value'} if is_list_view else {'key': 'single value'}

        extra_ret = {}
        for key in ret['song'].keys():
            extra_ret[key] = ret['song'][key]

        extra_ret['fid'] = ret['id']

        ret.update(extra_ret)

        del ret['id']
        del ret['song']
        return ret


class SongFavCreateSerializer(serializers.ModelSerializer):
    """用户收藏的序列化函数"""

    username = serializers.HiddenField(
        default=CurrentUserDefault()
    )

    class Meta:
        model = SongFav

        fields = ('username', 'song', 'id')
        validators = [
            UniqueTogetherValidator(
                queryset=SongFav.objects.all(),
                fields=('username', 'song'),
                message="已经收藏"
            )
        ]
