from rest_framework import viewsets

from apps.user.models.playlist import Playlist
from apps.user.serializers.playlist import (
    PlaylistSerializer, PlaylistShortInfoSerializer)


class PlaylistView(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    http_method_names = ('get',)

    def get_serializer_class(self):
        if getattr(self, 'action', None) == 'list':
            return PlaylistShortInfoSerializer

        return PlaylistSerializer
