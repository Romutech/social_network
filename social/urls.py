from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.list_profiles, name='list_profiles'),
    path('profile/<id>', views.show_profile, name='show_profile'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout_view'),
    path('signin/', views.signin, name='signin'),
    path('login_user/', views.login_user, name='login_user'),
]
