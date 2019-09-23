from django.db.models import (
    BooleanField, CharField, ForeignKey, ManyToManyField, Model,
    PositiveSmallIntegerField, CASCADE)

from apps.media.models.song import Song
from apps.user.models.user import User


class Playlist(Model):
    name = CharField(max_length=200)
    songs = ManyToManyField(Song, related_name='playlists')
    songs_amount = PositiveSmallIntegerField(default=0)
    is_private = BooleanField(default=False)
    owner = ForeignKey(User, related_name='playlists', on_delete=CASCADE)

    def __str__(self):
        return self.name
