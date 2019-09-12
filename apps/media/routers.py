from rest_framework import routers

from apps.media.views.album import AlbumView
from apps.media.views.artist import ArtistView
from apps.media.views.genre import GenreView
from apps.media.views.song import SongView




router = routers.DefaultRouter()
router.register('genre', GenreView)
router.register('artist', ArtistView)
router.register('album', AlbumView)
router.register('song', SongView)
