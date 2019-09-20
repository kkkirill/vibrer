from django.db.models import (
    BooleanField, CharField, ManyToManyField, Model, PositiveSmallIntegerField)

from apps.media.models.song import Song


class Playlist(Model):
    name = CharField(max_length=200)
    songs = ManyToManyField(Song, related_name='playlists')
    songs_amount = PositiveSmallIntegerField(default=0)
    is_private = BooleanField(default=False)

    def __str__(self):
        return self.name
