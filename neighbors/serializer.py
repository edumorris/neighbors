from rest_framework import serializers
from .models import Profile, Neighborhood

class HoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ('neighborhood_name', 'location', 'occupants', 'Admin')