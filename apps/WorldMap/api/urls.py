from rest_framework.routers import DefaultRouter
from django.urls import include, path

from apps.WorldMap.api.viewsets import worldMapViewSet

router = DefaultRouter()

router.register(prefix="WorldMap", viewset= worldMapViewSet)


urlpatterns = [
    path("api/", include(router.urls))
]