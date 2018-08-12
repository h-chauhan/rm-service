from rest_framework import serializers
from .models import *

class PlacementNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacementNotification
        fields = '__all__'

class InternNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternNotification
        fields = '__all__'

class PlacementJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacementJobOpening
        fields = '__all__'

class InternJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternJobOpening
        fields = '__all__'