from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User as User_Auth

class User(User_Auth):
   pass

class Profile(models.Model):
    user      = models.ForeignKey(User_Auth, on_delete=models.CASCADE) 
    date      = models.DateTimeField(default=timezone.now, verbose_name="Date de création")

    class Meta:
        verbose_name="Profil"

    def __str__(self):
        return "Profil de {}".format(self.user.username)

class Message(models.Model):
    content = models.CharField(max_length=100, verbose_name="")
    author  = models.ForeignKey('User', on_delete=models.CASCADE)
    date    = models.DateTimeField(default=timezone.now, verbose_name="Date de création")

class ProfileStatus(Message):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    class Meta:
        verbose_name="Statut"

    def __str__(self):
        return self.content


class Comment(Message):
    status  = models.ForeignKey('ProfileStatus', on_delete=models.CASCADE)

    class Meta:
        verbose_name="Commentaire"

    def __str__(self):
        return self.content

