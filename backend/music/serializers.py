from rest_framework import serializers
from .models import *


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        exclude = [
            'id',
        ]
