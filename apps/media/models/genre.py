from django.db.models import Model, CharField


class Genre(Model):
    HH = 'Hip - Hop'
    REG = 'Reggae'
    POP = 'Pop'
    IND = 'Indie'
    ROCK = 'Rock'
    CLS = 'Classic'
    RdB = 'R & B'
    JAZZ = 'Jazz'
    GENRES = (
        (HH, 'Hip - Hop'),
        (REG, 'Reggae'),
        (POP, 'Pop'),
        (IND, 'Indie'),
        (ROCK, 'Rock'),
        (CLS, 'Classic'),
        (RdB, 'R & B'),
        (JAZZ, 'Jazz'),
    )
    name = CharField(choices=GENRES)