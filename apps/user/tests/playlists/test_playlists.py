import faker
import pytest


@pytest.mark.django_db
class TestPlaylist:
    @pytest.mark.parametrize('is_private', [False])
    def test_permissions(self, client, playlist, is_private):
        """
        test public playlist detail
        """
        owner_id = playlist.owner_id
        res = client.get(f'/api/user/{owner_id}/playlist/{playlist.id}/',
                         content_type="application/json")
        playlist_dict = res.json()
        # breakpoint()
        assert res.status_code == 200
        assert isinstance(playlist_dict.get('name'), str)
        assert isinstance(playlist_dict.get('songs'), list)
        assert isinstance(playlist_dict.get('songs_amount'), int)
        assert playlist_dict.get('is_private') is is_private

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
