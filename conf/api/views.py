from django.shortcuts import render
from rest_framework import mixins, viewsets, generics

from .models import Event, Organization
from .serializers import (
    EventInputSerializer, EventOutputSerializer, OrganizationSerializer)


class EventViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Event.objects.prefetch_related(
        'organizations', 'organizations__user_organizaton').all()

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return EventOutputSerializer
        return EventInputSerializer


class OrganizationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    pagination_class = None
