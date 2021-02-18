from rest_framework import serializers
from .models import *


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        exclude = [
            'id',
        ]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = [
            'id',
        ]


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        exclude = [
            'id',
        ]


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        exclude = [
            'id',
        ]
