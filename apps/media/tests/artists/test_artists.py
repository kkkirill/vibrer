import faker
import pytest


@pytest.mark.django_db
class TestArtists:
    def test_detail(self, client, artist):
        """
        test artist details
            * check basic structure
        """
        res = client.get(f'/api/artist/{artist.id}')
        artist_dict = res.json()
        fields = ('stage_name', 'info', 'photo', 'genres')
        assert res.status_code == 200
        assert all(artist_dict.get(k) for k in fields)

    @pytest.mark.parametrize('artist_qty', [0, 5, 10, 25, 45])
    def test_list(self, client, artists, artist_qty):
        """
        test list of artists on getting right:
            * amount
            * data type
        """
        res = client.get('/api/artist')
        assert res.status_code == 200
        assert isinstance(res.json(), list)
        assert len(res.json()) == artist_qty

    def test_detail_error(self, client):
        """
        test artist details for non-existing artist
        """
        res = client.get(f'/api/artist/{faker.Faker().random_number(digits=30)}')
        assert res.status_code == 404
