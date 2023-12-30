from rest_framework import serializers
from .models import Room

# Creating the serializer for the room
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        # Specifying the model
        model = Room
        # Specifying the fields
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')