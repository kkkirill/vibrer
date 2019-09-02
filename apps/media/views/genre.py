from rest_framework import viewsets
from apps.media.serializers.genre import GenreDetailSerializer
from apps.media.models.genre import Genre


class GenreListView(viewsets.ModelViewSet):
    serializer_class = GenreDetailSerializer
    queryset = Genre.objects.all()
