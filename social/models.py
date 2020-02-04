from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User as User_Auth

class User(User_Auth):
    pass


class Profile(models.Model):
    user      = models.CharField(max_length=100, verbose_name="")
    date      = models.DateTimeField(default=timezone.now, verbose_name="Date de création")

    class Meta:
        verbose_name="Profil"

    def __str__(self):
        return "Profil de {}".format(User_Auth.objects.get(id=self.user))

class Message(models.Model):
    content = models.CharField(max_length=100, verbose_name="")
    author  = models.CharField(max_length=100, verbose_name="")
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


def save_status(request):
    try:
        if request.POST['type_form'] == 'profile_status':
            status = ProfileStatus()
            status.content = request.POST['content']
            status.profile = Profile(id=request.POST['profile'])
            status.author = request.user.id
            status.save()
            return True
    except:
        pass

    return False

def save_comment(request, form):
    try:  
        if request.POST['type_form'] == 'comment_status':
            if form.is_valid():
                comment = Comment()
                comment.content = request.POST['content']
                comment.status = ProfileStatus.objects.get(id=request.POST['status'])
                comment.author = request.user.id
                comment.save()
                return True
    except:
        pass

    return False