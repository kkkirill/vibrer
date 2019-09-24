import pytest
from rest_auth.app_settings import TokenSerializer, create_token
from rest_auth.models import TokenModel

from utils.factories import PlaylistFactory, SongFactory, UserFactory


@pytest.fixture
def playlist(user):
    return PlaylistFactory.create(owner=user, is_private=False,
                                  songs=SongFactory.create_batch(size=6))


@pytest.fixture
def playlist_qty():
    return 1


@pytest.fixture
def playlists(playlist_qty, user):
    return PlaylistFactory.create_batch(size=playlist_qty, owner=user)


@pytest.fixture
def user():
    return UserFactory.create(is_staff=False)


@pytest.fixture
def token(user):
    return create_token(TokenModel, user, TokenSerializer)


@pytest.fixture
def songs():
    return SongFactory.create_batch(size=4)
