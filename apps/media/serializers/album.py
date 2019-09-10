from rest_framework.serializers import ModelSerializer

from apps.media.models.album import Album
from apps.media.serializers.artist import ArtistShortInfoSerializer
from apps.media.serializers.genre import GenreDetailSerializer
from apps.media.serializers.song import SongShortInfoSerializer


class AlbumSerializer(ModelSerializer):
    genres = GenreDetailSerializer(many=True, )
    songs = SongShortInfoSerializer(many=True, )

    class Meta:
        model = Album
        fields = ('url', 'title', 'songs_amount', 'photo',
                  'release_year', 'genres', 'songs')
        read_only_fields = ('songs_amount',)


class AlbumDetailSerializer(AlbumSerializer):
    artists = ArtistShortInfoSerializer(many=True, )

    class Meta(AlbumSerializer.Meta):
        fields = AlbumSerializer.Meta.fields + ('artists',)
