from rest_framework import serializers
from .models import MessagesArea


class MessagesAreaSerilizer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = MessagesArea
        fields = ['user', 'message', 'timeStamp']
