from django.urls import include, path, re_path
from rest_framework import routers

from .views import EventViewSet, OrganizationViewSet

router = routers.DefaultRouter()

router.register('events', EventViewSet, basename='events')
router.register(
    'organizations', OrganizationViewSet, basename='organizations')

urlpatterns = [
    path('', include(router.urls)),
]
