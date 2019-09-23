import pytest

# from rest_auth.models import TokenModel
# from rest_auth.app_settings import create_token, TokenSerializer
from utils.factories import (
    PlaylistFactory, SongFactory, UserFactory)


@pytest.fixture
def playlist(is_private=False):
    user = UserFactory.create()
    return PlaylistFactory.create(owner=user, is_private=is_private,
                                  songs=SongFactory.create_batch(size=6))


@pytest.fixture
def playlist_qty():
    return 1


@pytest.fixture
def playlists(album_qty):
    user = UserFactory.create()
    return PlaylistFactory.create_batch(size=playlist_qty, owner=user)


@pytest.fixture
def user():
    user = UserFactory.get()
    PlaylistFactory.create(owner=user)
    return user


# @pytest.fixture
# def token(user):
#     return create_token(TokenModel, user, TokenSerializer)
