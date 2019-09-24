from random import randint
from typing import Union

import factory

from apps.media.models.album import Album
from apps.media.models.artist import Artist
from apps.media.models.genre import Genre
from apps.media.models.song import Song
from apps.user.models.playlist import Playlist
from apps.user.models.user import User

GENRES = [
    'Hip - Hop',
    'Reggae',
    'Pop',
    'Indie',
    'Rock',
    'Classic',
    'R & B',
    'Jazz',
]


class GenreFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: GENRES[n % len(GENRES)])

    class Meta:
        model = Genre


class ArtistFactory(factory.django.DjangoModelFactory):
    stage_name = factory.Faker('name')
    info = factory.Faker('text', max_nb_chars=200)
    photo = factory.Faker('file_name', category="image")

    class Meta:
        model = Artist

    @factory.post_generation
    def genres(self, create, extracted):
        if not create:
            return

        if extracted:
            for gn in extracted:
                self.genres.add(gn)


class SongFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('pystr', min_chars=5, max_chars=15)
    duration = factory.Faker('pyint', min_value=30, max_value=300)
    file = factory.Faker('file_name', category="audio")
    image = factory.Faker('file_name', category="image")
    listens = factory.Faker('pyint')
    explicit = factory.Faker('pybool')

    class Meta:
        model = Song

    @factory.post_generation
    def artists(self, create, extracted):
        if not create:
            return

        if extracted:
            for ar in extracted:
                self.artists.add(ar)

    @factory.post_generation
    def genres(self, create, extracted):
        if not create:
            return

        if extracted:
            for gn in extracted:
                self.genres.add(gn)


class AlbumFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('pystr', min_chars=5, max_chars=15)
    songs_amount = 0
    release_year = factory.Faker('date_between', start_date='-30y', end_date='now')
    photo = factory.Faker('file_name', category="image")

    class Meta:
        model = Album

    @factory.post_generation
    def artists(self, create, extracted):
        if not create:
            return

        if extracted:
            for ar in extracted:
                self.artists.add(ar)

    @factory.post_generation
    def genres(self, create, extracted):
        if not create:
            return

        if extracted:
            for gn in extracted:
                self.genres.add(gn)

    @factory.post_generation
    def songs(self, create, extracted):
        if not create:
            return

        if extracted:
            self.songs_amount = len(extracted)

            for so in extracted:
                self.songs.add(so)


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('pystr', min_chars=5, max_chars=20)
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', 'password')
    photo = factory.Faker('file_name', category='image')
    followers_amount = 0
    is_staff = factory.Faker('pybool')

    class Meta:
        model = User

    @factory.post_generation
    def followers(self, create, extracted):
        if not create:
            return

        if extracted:
            self.followers_amount = len(extracted)

            for fo in extracted:
                self.followers.add(fo)

    @factory.post_generation
    def liked_songs(self, create, extracted):
        if not create:
            return

        if extracted:
            for ls in extracted:
                self.liked_songs.add(ls)


class PlaylistFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('pystr', min_chars=5, max_chars=10)
    songs_amount = 0
    is_private = factory.Faker('pybool')
    owner = factory.SubFactory(UserFactory)

    class Meta:
        model = Playlist

    @factory.post_generation
    def songs(self, create, extracted):
        if not create:
            return

        if extracted:
            self.songs_amount = len(extracted)

            for so in extracted:
                self.songs.add(so)


def fill_with_data(model: Union[Album, Artist, Genre, Song, User, Playlist],
                   min_limit: int, max_limit: int) -> frozenset:
    """
    This function generates a collection with random size.
        Takes:
            model: queryset with multiple instances of one type(
                Album, Artist, Genre, Song, Playlist or User
            ).
            min_limit: defines min size of collection, integer.
            max_limit: defines max size of collection, integer.
        Logic:
            Fills buffer with randomly chosen instances from model.
            Buffer size variates from min_limit to max_limit.
        Returns:
            Hashable buffer with random amount of model instances.
    """
    return frozenset(
        model[randint(0, len(model)-1)]
        for _ in range(randint(min_limit, max_limit))
    )


def fill(amount=50):
    Album.objects.all().delete()
    Artist.objects.all().delete()
    Genre.objects.all().delete()
    Song.objects.all().delete()
    User.objects.all().delete()
    Playlist.objects.all().delete()

    # creating genres here
    for _ in range(len(GENRES)):
        GenreFactory.create()

    # creating artists here
    genres = Genre.objects.all()
    for _ in range(amount//3):
        ArtistFactory.create(genres=fill_with_data(genres, 1, 3))

    # creating songs here
    artists = Artist.objects.all()
    for _ in range(amount):
        SongFactory.create(artists=fill_with_data(artists, 1, 3),
                           genres=fill_with_data(genres, 1, 3))

    # creating albums here
    songs = Song.objects.all()
    for _ in range(amount//4):
        AlbumFactory.create(artists=fill_with_data(artists, 1, 3),
                            genres=fill_with_data(genres, 1, 3),
                            songs=fill_with_data(songs, 5, 10))

    # creating users here
    for _ in range(amount):
        users = User.objects.all()
        user = UserFactory.create(
            followers=fill_with_data(users, 0, len(users)),
            liked_songs=fill_with_data(songs, 5, 10)
        )
        # creating playlists for user
        for _ in range(amount//10):
            PlaylistFactory.create(songs=fill_with_data(songs, 5, 10),
                                   owner=user)
