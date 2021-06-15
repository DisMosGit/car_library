from django.db import models
from users.models import User
# Create your models here.


class Feedback(models.Model):
    user = models.ForeignKey(User,
                             related_name='feedbacks',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    data = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    class Meta:
        abstract = True
        
