import json

import faker
import pytest


@pytest.mark.django_db
class TestPlaylist:
    def test_public(self, client, playlist):
        """
        test public playlist without authentication
        """
        owner_id = playlist.owner_id
        res = client.get(f'/api/user/{owner_id}/playlist/{playlist.id}/',
                         content_type="application/json")
        playlist_dict = res.json()
        assert res.status_code == 200
        assert isinstance(playlist_dict.get('name'), str)
        assert isinstance(playlist_dict.get('songs'), list)
        assert isinstance(playlist_dict.get('songs_amount'), int)
        assert playlist_dict.get('is_private') is False

    def test_detail(self, client, playlist, user, token):
        """
        test playlist detail
        """
        user.is_staff = True
        user.save()
        res = client.get(f'/api/user/{user.id}/playlist/{playlist.id}/',
                         content_type="application/json",
                         **{'HTTP_AUTHORIZATION': 'Token ' + str(token)})
        playlist_dict = res.json()
        assert res.status_code == 200
        assert isinstance(playlist_dict.get('name'), str)
        assert isinstance(playlist_dict.get('is_private'), bool)

    @pytest.mark.parametrize('playlist_qty', [0, 5, 10, 25, 45])
    def test_list(self, client, user, token, playlists, playlist_qty):
        """
        test list of playlist on getting right:
            * amount
            * data type
        """
        user.is_staff = True
        user.save()
        res = client.get(f'/api/user/{user.id}/playlist/',
                         content_type="application/json",
                         **{'HTTP_AUTHORIZATION': 'Token ' + str(token)})
        assert res.status_code == 200
        assert isinstance(res.json(), list)
        assert len(res.json()) == playlist_qty

    @pytest.mark.parametrize('is_private', [False, True])
    def test_create(self, client, user, token, is_private):
        """
        test create playlist
        """
        name = faker.Faker().pystr(min_chars=10, max_chars=30)
        data = json.dumps({
            "name": name,
            "is_private": is_private,
            "owner": user.id
        })
        res = client.post(f'/api/user/{user.id}/playlist/', data=data,
                          content_type="application/json",
                          **{'HTTP_AUTHORIZATION': 'Token ' + str(token)})
        playlist_dict = res.json()
        assert res.status_code == 201
        assert playlist_dict.get("name") == name
        assert playlist_dict.get("is_private") is is_private

    def test_update(self, client, user, token, playlist):
        """
        test update public playlist
        """
        name = faker.Faker().pystr(min_chars=10, max_chars=30)
        is_private = True
        data = json.dumps({
            "name": name,
            "is_private": is_private,
        })
        res = client.put(f'/api/user/{user.id}/playlist/{playlist.id}/',
                         data=data, content_type="application/json",
                         **{'HTTP_AUTHORIZATION': 'Token ' + str(token)})
        playlist_dict = res.json()
        assert res.status_code == 200
        assert playlist_dict.get("name") == name
        assert playlist_dict.get("is_private") is True

    def test_create_songs(self, client, user, token, playlist, songs):
        """
        test create songs to the playlist
        """
        user.is_staff = True
        user.save()
        playlist.songs.all().delete()
        # breakpoint()
        songs = [song.id for song in songs]
        data = json.dumps({"songs": songs})
        res = client.post(f'/api/user/{user.id}/playlist/{playlist.id}/song/',
                          data=data, content_type="application/json",
                          **{'HTTP_AUTHORIZATION': 'Token ' + str(token)})
        songs_dict = res.json()
        assert res.status_code == 201
        assert set(songs_dict.get("songs")) == set(songs)

    def test_delete_song(self, client, user, token, playlist):
        """
        test delete existing song
        """
        user.is_staff = True
        user.save()
        song_id = playlist.songs.first().id
        songs = {x.id for x in playlist.songs.all()}
        assert song_id in songs
        res = client.delete(
                f'/api/user/{user.id}/playlist/{playlist.id}/song/{song_id}/',
                content_type="application/json",
                **{'HTTP_AUTHORIZATION': 'Token ' + str(token)}
        )
        songs = {x.id for x in playlist.songs.all()}
        assert res.status_code == 204
        assert song_id not in songs
