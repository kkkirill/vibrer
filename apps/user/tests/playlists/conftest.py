import pytest

# from rest_auth.models import TokenModel
# from rest_auth.app_settings import create_token, TokenSerializer
from utils.factories import (
    PlaylistFactory, SongFactory, UserFactory)


@pytest.fixture
def playlist():
    return PlaylistFactory.create(
        songs=SongFactory.create_batch(size=6),
    )


@pytest.fixture
def playlist_qty():
    return 1


@pytest.fixture
def playlists(album_qty):
    return PlaylistFactory.create_batch(size=playlist_qty)


@pytest.fixture
def user():
    return UserFactory.create(
        playlists=PlaylistFactory.create_batch(size=5)
    )


# @pytest.fixture
# def token(user):
#     return create_token(TokenModel, user, TokenSerializer)
