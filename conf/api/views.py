import base64

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets, status
from rest_framework.response import Response

from .models import Event, Organization
from .serializers import (
    EventInputSerializer, EventOutputSerializer, OrganizationSerializer)
from .tasks import create_event_with_sleep


class EventViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Event.objects.prefetch_related(
        'organizations', 'organizations__user_organizaton').all()
    filter_backends = (
        DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('title',)
    ordering_fields = ('date',)
    filterset_fields = ('date',)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return EventOutputSerializer
        return EventInputSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image_content = None
        if 'image' in self.request.FILES:
            image_content = base64.b64encode(
                self.request.FILES['image'].read()).decode('utf-8')
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'organizations': request.data.getlist('organizations'),
            'date': serializer.validated_data.get('date'),
            'image': image_content
        }
        create_event_with_sleep.delay(data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrganizationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    pagination_class = None
