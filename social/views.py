from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def list_profiles(request):

    return render(request, 'social/list_profiles.html', locals())

def show_profile(request, id):

    return render(request, 'social/show_profile.html', locals())

def edit_profile(request):

    return render(request, 'social/edit_profile.html', locals())

def save_profile(request):

    return redirect(show_profile, id)

def save_comment(request):

    return redirect(show_profile, id)

def save_status(request):

    return redirect(show_profile, id)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(list_profiles)
    else:
        form = UserCreationForm()
    return render(request, 'social/signup.html', {'form': form})