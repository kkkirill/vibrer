from rest_framework.serializers import ModelSerializer

from apps.media.models.genre import Genre


class GenreDetailSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ('url', 'name')
        extra_kwargs = {
            'name': {'validators': []},
        }
