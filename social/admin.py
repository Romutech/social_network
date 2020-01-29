from django.contrib import admin
from .models import Profile, ProfileStatus, Comment, User

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(ProfileStatus)
admin.site.register(Comment)
