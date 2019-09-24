import pytest
from rest_auth.app_settings import TokenSerializer, create_token
from rest_auth.models import TokenModel

from utils.factories import PlaylistFactory, SongFactory, UserFactory


@pytest.fixture
def song_qty():
    return 1


@pytest.fixture
def songs(song_qty):
    return SongFactory.create_batch(size=song_qty, explicit=False)


@pytest.fixture
def playlist(user, songs):
    return PlaylistFactory.create(owner=user, is_private=False,
                                  songs=songs)


@pytest.fixture
def playlist_qty():
    return 1


@pytest.fixture
def playlists(playlist_qty, user):
    return PlaylistFactory.create_batch(size=playlist_qty, owner=user)


@pytest.fixture
def is_staff(is_staff=False):
    return is_staff


@pytest.fixture
def user(is_staff):
    return UserFactory.create(is_staff=is_staff)


@pytest.fixture
def token(user):
    return create_token(TokenModel, user, TokenSerializer)


@pytest.fixture
def songs_for_added():
    return SongFactory.create_batch(size=4)
