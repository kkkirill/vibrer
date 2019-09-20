from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin

from apps.user.models.playlist import Playlist
from apps.user.permissions import IsOwnerOrAdmin
from apps.user.serializers.playlist import (
    PlaylistCUSerializer, PlaylistSerializer, PlaylistShortInfoSerializer,
    SongsInPlaylistSerializer)


class PlaylistView(NestedViewSetMixin, viewsets.ModelViewSet):
    http_method_names = ('get', 'post', 'put')

    def get_serializer_class(self):
        method = getattr(self.request, 'method', None)
        action = getattr(self, 'action', None)
        if self.request and method == 'GET':
            if action == 'list':
                return PlaylistShortInfoSerializer
            elif action == 'retrieve':
                return PlaylistSerializer
        elif self.request and method in ('POST', 'PUT'):
            return PlaylistCUSerializer

    def get_queryset(self):
        user_id = self.kwargs['parent_lookup_user_playlists']
        return Playlist.objects.filter(users=user_id)


class SongsInPlaylistView(NestedViewSetMixin, viewsets.ModelViewSet):
    http_method_names = ('post', 'delete',)
    serializer_class = SongsInPlaylistSerializer

    def get_queryset(self):
        playlist_id = self.kwargs['parent_lookup_playlist']
        return Playlist.objects.filter(pk=playlist_id)

    def destroy(self, request, *args, **kwargs):
        playlist_id = self.kwargs['parent_lookup_playlist']
        playlist = Playlist.objects.get(pk=playlist_id)
        song_id = self.kwargs.get('pk')
        playlist.songs.remove(song_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
