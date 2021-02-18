from rest_framework import routers

from music.views import *

router = routers.DefaultRouter()
router.register('artists', ArtistViewSet)
router.register('genres', GenreViewSet)
router.register('albums', AlbumViewSet)
router.register('songs', SongViewSet)
