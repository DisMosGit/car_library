from django.contrib.auth.models import User
from rest_framework import serializers
from .models import CarBrand, CarModel, CarModification, CarSpecifications, PersonalCar


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ['id', 'brand']


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id', 'brand', 'model', 'model_age']


class CarModificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModification
        fields = ['id', 'model']


class CarSpecificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpecifications
        fields = ['id', 'mod']


class PersonalCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalCar
        fields = ['id', 'owner', 'drivers', 'car', 'VIN', 'name', 'mileage']
        read_only_fields = ['owner', 'drivers']


# class PersonalCarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PersonalCar
#         fields = ['id', 'url', 'owner', 'drivers', 'car', 'VIN', 'name', 'mileage']
#         read_only_fields = ['owner', 'drivers']