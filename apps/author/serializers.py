from django.db.models import Count
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from song.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    """关于作者的序列化函数"""

    aid = serializers.IntegerField(label='ID', validators=[UniqueValidator(queryset=Author.objects.all())],
                                   help_text='空的话， 就是自增序列', required=True, allow_null=True)
    songs = serializers.SerializerMethodField(read_only=True, method_name='get_songs')

    def get_songs(self, obj):
        queryset = Author.objects.filter(name=obj.name)
        authors = queryset.annotate(songs=Count('song_author'))

        return authors[0].songs

    class Meta:
        model = Author
        fields = "__all__"
