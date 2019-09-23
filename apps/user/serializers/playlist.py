from rest_framework.serializers import ModelSerializer

from apps.media.serializers.song import SongShortInfoSerializer
from apps.user.models.playlist import Playlist


class PlaylistSerializer(ModelSerializer):
    songs = SongShortInfoSerializer(many=True,)

    class Meta:
        model = Playlist
        fields = ('name', 'songs', 'songs_amount', 'is_private', 'owner')
        read_only_fields = ('songs_amount',)


class PlaylistShortInfoSerializer(ModelSerializer):
    class Meta(PlaylistSerializer.Meta):
        fields = ('name', 'id',)


class PlaylistCUSerializer(ModelSerializer):

    class Meta(PlaylistSerializer.Meta):
        fields = ('name', 'is_private', 'owner')


class SongsInPlaylistSerializer(ModelSerializer):
    class Meta(PlaylistSerializer.Meta):
        fields = ('songs',)

    def create(self, validated_data):
        songs_data = validated_data.pop("songs", None)
        playlist_id = self._context['view'].kwargs['parent_lookup_playlist']
        playlist = Playlist.objects.get(id=playlist_id)
        playlist.songs.add(*songs_data)
        return playlist
