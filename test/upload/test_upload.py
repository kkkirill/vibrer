import json

import faker
import pytest

from utils.upload_file import FileUploaderS3


@pytest.mark.django_db
class TestUpload:

    @pytest.mark.parametrize('file_name', ['media/song.mp3'])
    def test_upload_file(self, file_name):
        file_uploader = FileUploaderS3()
        key = file_name
        file_uploader.upload_file_to_s3(file_name, key)
        response = file_uploader.head_object(key)
        assert response['ResponseMetadata']['HTTPStatusCode'] == 200

    def test_create_song_with_upload(self, client, artists, genres, keys):
        factory = faker.Faker()
        title = factory.pystr(min_chars=5, max_chars=15)
        explicit = factory.pybool()
        url_prefix = factory.url(schemes=None)
        song_file = f'{url_prefix}{keys["fkey"]}'
        song_image = f'{url_prefix}{keys["ikey"]}'
        genre_ids = [genre.id for genre in genres]
        artist_ids = [artist.id for artist in artists]
        data = {
            'title': title,
            'explicit': explicit,
            'image': song_image,
            'file': song_file,
            'genres': genre_ids,
            'artists': artist_ids
        }
        data = json.dumps(data)
        res = client.post('/api/song/', data=data,
                          content_type='application/json')
        song_dict = res.json()
        assert res.status_code == 201
        assert song_dict.get('title') == title
        assert song_dict.get('image') == song_image
        assert song_dict.get('file') == song_file
        assert song_dict.get("explicit") == explicit
        assert set(song_dict.get("genres")) == set(genre_ids)
        assert set(song_dict.get("artists")) == set(artist_ids)
