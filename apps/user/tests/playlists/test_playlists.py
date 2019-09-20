import faker
import pytest


@pytest.mark.django_db
class TestPlaylist:
    def test_permissions(self, client, user):
        """
        test get list of playlists without authentication
        """
        res = client.get(f'/api/user/{user.id}/playlist/',
                         content_type="application/json")
        # breakpoint()
        assert res.status_code == 401

    # def test_detail(self, client, playlist, user, token):
    #     """
    #     test playlist detail
    #     """
    #     breakpoint()
    #     user.is_staff = True
    #     user.save()
    #     res = client.get(f'/api/user/{user.id}/playlist/{playlist.id}/',
    #                      content_type="application/json",
    #                      **{'HTTP_AUTHORIZATION': 'Token ' + str(token)})
    #     playlist_dict = res.json()
    #     assert res.status_code == 200
    #     assert isinstance(playlist_dict.get('title'), str)
    #     assert isinstance(playlist_dict.get('is_private'), list)
