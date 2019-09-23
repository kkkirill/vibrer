from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import NestedRouterMixin

from apps.user.views.playlist import PlaylistView, SongsInPlaylistView
from apps.user.views.user import UserView


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()


user_playlist_router = router.register(
    r'user',
    UserView,
    basename='user')
user_playlist_router.register(
    r'playlist',
    PlaylistView,
    basename='playlist',
    parents_query_lookups=['user_playlists']
).register(
    r'song',
    SongsInPlaylistView,
    basename='user-playlist-song',
    parents_query_lookups=['user', 'playlist']
)
