from django.db import models
from django.utils import timezone

class Profile(models.Model):
    firstname = models.CharField(max_length=100)
    lastname  = models.CharField(max_length=100)
    #user     = models.ForeignKey('User', on_delete=models.CASCADE) #Todo manage User model
    date      = models.DateTimeField(default=timezone.now, verbose_name="Date de création")

    class Meta:
        verbose_name="Profil"

    def __str__(self):
        return "profil de {} {}".format(self.firstname, self.lastname)


class Status(models.Model):
    content = models.CharField(max_length=100)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    date    = models.DateTimeField(default=timezone.now, verbose_name="Date de création")

    class Meta:
        verbose_name="Statut"

    def __str__(self):
        return self.content


class Comment(models.Model):
    content = models.CharField(max_length=100)
    status  = models.ForeignKey('Status', on_delete=models.CASCADE)
    date    = models.DateTimeField(default=timezone.now, verbose_name="Date de création")

    class Meta:
        verbose_name="Commentaire"

    def __str__(self):
        return self.content