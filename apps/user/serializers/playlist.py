from rest_framework.serializers import ModelSerializer

from apps.user.models.user import Playlist
from apps.media.serializers.song import SongShortInfoSerializer


class PlaylistSerializer(ModelSerializer):
    songs = SongShortInfoSerializer(many=True)

    class Meta:
        model = Playlist
        fields = ('url', 'name', 'songs', 'songs_amount', 'is_private')


class PlaylistShortInfoSerializer(PlaylistSerializer):

    class Meta(PlaylistSerializer.Meta):
        fields = ('url', 'name', 'songs_amount')
