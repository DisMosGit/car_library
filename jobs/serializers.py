from django.contrib.auth.models import User
from rest_framework import serializers
from django.utils import timezone

from cars.models import PersonalCar
from .models import JobList, JobOnCar


class CarUserRelatedField(serializers.PrimaryKeyRelatedField):
    view_name = 'personalcar-detail'

    def get_queryset(self):
        queryset = (
            PersonalCar.objects.filter(owner=self.context['request'].user)
            | self.context['request'].user.driven.all()).distinct()
        return queryset


class JobListSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobList
        fields = ['id', 'name']


class JobOnCarSerializer(serializers.ModelSerializer):
    car = CarUserRelatedField()
    datetime = serializers.DateTimeField(default=timezone.now)

    class Meta:
        model = JobOnCar
        fields = ['id', 'user', 'car', 'job', 'datetime', 'cost']
        read_only_fields = ['user']
