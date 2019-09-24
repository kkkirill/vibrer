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

    @pytest.mark.parametrize('file_name,image_name',
                             [('media/song.mp3', 'media/dingo.png')])
    def test_create_song_with_upload(self, client, artists, genres, file_name,
                                     image_name):
        file_uploader = FileUploaderS3()
        fkey = file_uploader.upload_file_to_s3(file_name)
        ikey = file_uploader.upload_file_to_s3(image_name)
        factory = faker.Faker()
        title = factory.pystr(min_chars=5, max_chars=15)
        explicit = factory.pybool()
        url_prefix = factory.url(schemes=None)
        file = f'{url_prefix}{fkey}'
        image = f'{url_prefix}{ikey}'
        genres = [genre.id for genre in genres]
        artists = [artist.id for artist in artists]
        data = {
            'title': title,
            'explicit': explicit,
            'image': image,
            'file': file,
            'genres': genres,
            'artists': artists
        }
        data = json.dumps(data)
        res = client.post('/api/song/', data=data,
                          content_type='application/json')
        song_dict = res.json()
        assert res.status_code == 201
        assert song_dict.get('title') == title
        assert song_dict.get('image') == image
        assert song_dict.get('file') == file
        assert song_dict.get("explicit") == explicit
        assert set(song_dict.get("genres")) == set(genres)
        assert set(song_dict.get("artists")) == set(artists)
