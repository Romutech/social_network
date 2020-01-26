from django.db import models
from django.utils import timezone

class Profile(models.Model):
    firstname = models.CharField(max_length=100)
    lastname  = models.CharField(max_length=100)
    user      = models.ForeignKey('User', on_delete=models.CASCADE) #Todo manage User model
    date      = models.DateTimeField(default=timezone.now, verbose_name="Date de création")

    class Meta:
        verbose_name="Profil"

    def __str__(self):
        return "profil de {} {}".format(self.firstname, self.lastname)
