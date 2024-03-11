from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Event, Organization

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'phone_number')


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('pk', 'title', 'description', 'address', 'postcode')


#
class OrganizationEventSerializer(OrganizationSerializer):
    participants = UserSerializer(many=True, source='user_organizaton')
    organization_address = serializers.SerializerMethodField()

    class Meta(OrganizationSerializer.Meta):
        fields = (
            'title', 'description', 'organization_address', 'participants')

    def get_organization_address(self, obj):
        return f'{obj.address} {obj.postcode}'


class EventInputSerializer(serializers.ModelSerializer):
    organizations = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Organization.objects.all())

    class Meta:
        model = Event
        fields = ('title', 'description', 'organizations', 'image', 'date')


class EventOutputSerializer(serializers.ModelSerializer):
    organizations = OrganizationEventSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('title', 'description', 'organizations', 'image', 'date')
