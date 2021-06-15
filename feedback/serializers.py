from django.contrib.auth.models import User
from rest_framework import serializers
from django.utils import timezone

class FeedbackSerializer(serializers.Serializer):
    user = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    text = serializers.CharField(max_length=511)
    datetime = serializers.DateTimeField(read_only=True, default=timezone.now)


