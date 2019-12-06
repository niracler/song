from django.db.models import Count
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Song, Author


class AuthorSmallSerializer(serializers.ModelSerializer):
    """关于作者的序列化函数"""

    class Meta:
        model = Author
        fields = ('aid', 'name')


class SongSerializer(serializers.ModelSerializer):
    sid = serializers.IntegerField(label='ID', validators=[UniqueValidator(queryset=Song.objects.all())],
                                   help_text='空的话， 就是自增序列', required=False)

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
        fields = "__all__"
