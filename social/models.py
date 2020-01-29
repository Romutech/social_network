from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class User(User):
   pass


class Profile(models.Model):
    user      = models.ForeignKey(User, on_delete=models.CASCADE) #Todo manage User model
    date      = models.DateTimeField(default=timezone.now, verbose_name="Date de création")

    class Meta:
        verbose_name="Profil"

    def __str__(self):
        return "Profil de {}".format(self.user.username)


class Status(models.Model):
    content = models.CharField(max_length=100, verbose_name="Statut")
    author  = models.ForeignKey('User', on_delete=models.CASCADE)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    date    = models.DateTimeField(default=timezone.now, verbose_name="Date de création")

    class Meta:
        verbose_name="Statut"

    def __str__(self):
        return self.content


class Comment(models.Model):
    content = models.CharField(max_length=100, verbose_name="Commentaire")
    author  = models.ForeignKey('User', on_delete=models.CASCADE)
    status  = models.ForeignKey('Status', on_delete=models.CASCADE)
    date    = models.DateTimeField(default=timezone.now, verbose_name="Date de création")

    class Meta:
        verbose_name="Commentaire"

    def __str__(self):
        return self.content

