from rest_framework import serializers
from .models import Song



class SongSerializer(serializers.ModelSerializer):
    """关于歌曲的序列化函数"""

    class Meta:
        model = Song
        fields = "__all__"

class SongCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('name', 'file')