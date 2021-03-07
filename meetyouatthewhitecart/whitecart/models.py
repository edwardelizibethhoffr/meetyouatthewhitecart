from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
# Create your models here.


class UserBoxCoord(models.Model):

    x_coord = models.IntegerField()
    y_coord = models.IntegerField()
    user = models.ForeignKey('WhiteCartUser', on_delete=models.CASCADE)

    @property
    def getCoordinates(self):
        return {self.x_coord, self.y_coord}


class WhiteCartUser(AbstractBaseUser):

    username = models.CharField(verbose_name='username', max_length=40, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(verbose_name='date created', default=timezone.now)

