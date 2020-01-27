from django.contrib import admin
from .models import Profile, Status, Comment, User

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Status)
admin.site.register(Comment)
