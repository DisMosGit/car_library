from django.db import models
from django.core.exceptions import ValidationError
from users.models import User


# Create your models here.
class CarBrand(models.Model):
    brand = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.brand


class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand,
                              related_name='models',
                              on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    model_age = models.IntegerField()

    def __str__(self):
        return self.brand.__str__() + " " + self.model + " " + str(
            self.model_age)


class CarModification(models.Model):
    model = models.ForeignKey(CarModel,
                              related_name='modifications',
                              on_delete=models.CASCADE)


class CarSpecifications(models.Model):
    mod = models.ForeignKey(CarModification,
                            related_name='specifications',
                            on_delete=models.CASCADE)


def vin_validator(value):
    pass


class PersonalCar(models.Model):
    car = models.ForeignKey(CarModification,
                            related_name='personal_cars',
                            on_delete=models.CASCADE)
    owner = models.ForeignKey(User,
                              related_name='cars',
                              on_delete=models.CASCADE)
    drivers = models.ManyToManyField(User,
                                     related_name='driven',
                                     related_query_name='driven_q')
    VIN = models.CharField(max_length=17)
    name = models.CharField(max_length=63)
    mileage = models.IntegerField(default=0)
    tank_size = models.FloatField(null=True)
    tank_level = models.FloatField(default=0)

    def __str__(self):
        return self.owner.__str__() + " " + self.car.__str__() + " " + self.VIN

