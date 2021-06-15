from django.db import models
from cars.models import PersonalCar
from users.models import User
# Create your models here.


class JobList(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class JobOnCar(models.Model):
    user = models.ForeignKey(User,
                             related_name='jobs',
                             on_delete=models.CASCADE)
    car = models.ForeignKey(PersonalCar,
                            related_name='jobs',
                            on_delete=models.CASCADE)
    job = models.ForeignKey(JobList,
                            related_name='cars',
                            on_delete=models.CASCADE)
    datetime = models.DateTimeField(null=False)
    cost = models.FloatField(default=0)

    def __str__(self):
        return self.job.name + " " + self.datetime