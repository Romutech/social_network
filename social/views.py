from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import Http404
from .models import Profile, ProfileStatus, Comment, save_status, save_comment
from social.forms import CommentForm, ProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as User_Auth
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

def list_profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'social/list_profiles.html', locals())

def show_profile(request, id):
    try:
        profile = Profile.objects.get(id=id)
    except:
        raise Http404
    statutes = ProfileStatus.objects.filter(profile=profile)
    form = CommentForm(request.POST or None)
    if save_status(request):
        return redirect(show_profile, id)
    elif save_comment(request, form):
        return redirect(show_profile, id)
    return render(request, 'social/show_profile.html', locals())

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            profile = Profile()
            profile.user = user
            profile.username = user.username
            profile.save()
            login(request, user)
            return redirect(list_profiles)
    else:
        form = UserCreationForm()
    return render(request, 'social/signup.html', {'form': form})

def signin(request):
    return render(request, 'social/login.html')

def login_user(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        messages.add_message(request, messages.SUCCESS, "Vous êtes connecté !")
        return redirect(list_profiles)
    else:
        messages.add_message(request, messages.ERROR, "Les champs renseignés sont invalides.")
        
    return redirect(signin)

def logout_view(request):
    logout(request)
    if request.user.is_authenticated:
        messages.add_message(request, messages.SUCCESS, "Vous êtes toujours connecté !")
    else:
        messages.add_message(request, messages.SUCCESS, "Vous êtes bien déconnecté !")
    return redirect(list_profiles)
