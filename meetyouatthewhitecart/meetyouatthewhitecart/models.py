from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone

'''class WhitecCartUserManager(BaseUserManager):

    def _create_user(self, username):
        now = timezone.now()

        user = self.model(username=username, date_created=now, last_login=now)
        user.set_password(username)
        user.save(using=self._db)
        return user



class WhiteCartUser(AbstractBaseUser):

    username = models.CharField(_('username'), max_length=40, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(_('date created'), default=timezone.now)



class UserBoxCoord(models.Model):

    x_coord = models.IntergerField()
    y_coord = models.IntergerField()
    user = models.ForeignKey('WhiteCartUser')

    @property
    def getCoordinates(self):
        return {self.x_coord, self.y_coord} '''