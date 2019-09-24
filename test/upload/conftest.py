import pytest

from utils.factories import (
    ArtistFactory, GenreFactory, SongFactory)


@pytest.fixture
def song():
    return SongFactory.create(
        artists=ArtistFactory.create_batch(size=2),
        genres=GenreFactory.create_batch(size=2)
    )

@pytest.fixture
def artists():
    return ArtistFactory.create_batch(size=2)


@pytest.fixture
def genres():
    return GenreFactory.create_batch(size=2)
