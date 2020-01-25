from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.list_profiles, name='list_profiles'),
    path('profile/<id>', views.show_profile, name='show_profile'),
    path('edit/<id>', views.edit_profile, name='edit_profile'),
    path('comment/save', views.save_comment, name='save_comment'),
    path('status/save', view.save_status, name='save_status')
]