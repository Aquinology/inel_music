from rest_framework import routers

from music.views import AlbumViewSet

router = routers.DefaultRouter()
router.register('albums', AlbumViewSet)
