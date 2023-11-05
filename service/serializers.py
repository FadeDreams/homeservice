from rest_framework import serializers
from .models import Service, UsersApplied

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields ='__all__'

class UsersAppliedSerializer(serializers.ModelSerializer):

    service = ServiceSerializer()

    class Meta:
        model = UsersApplied
        fields = ('user', 'resume', 'appliedAt', 'service')
