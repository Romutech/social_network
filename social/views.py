from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import Http404
from .models import Profile, ProfileStatus, Comment
from social.forms import CommentForm, ProfileForm
from django.contrib.auth.forms import UserCreationForm

def list_profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'social/list_profiles.html', locals())

def show_profile(request, id):
    try:
        profile = Profile.objects.get(id=id)
    except:
        raise Http404

    dded = User.objects.get(id=request.user.id)
    
    form = CommentForm(request.POST or None)

    try:    
        if request.POST['type_form'] == 'profile_status':
            status = ProfileStatus()
            status.content = request.POST['content']
            status.profile = Profile.objects.get(id=request.POST['profile'])
            status.author = User.objects.get(id=user.profile)
            status.save()
            return redirect(show_profile, id)
    except:
        pass

    if form.is_valid():
        comment = Comment()
        comment.content = request.POST['content']
        comment.status = ProfileStatus.objects.get(id=request.POST['status'])
        comment.author = User.objects.get(id=user.profile)
        comment.save()
        return redirect(show_profile, id)

    statutes = ProfileStatus.objects.filter(profile=profile)
    return render(request, 'social/show_profile.html', locals())

def edit_profile(request):
    return render(request, 'social/edit_profile.html', locals())

def create_profile(request):
    form = ProfileForm(request.POST or None)

    rid = request.user.id
    ref = User.objects.all()

    if form.is_valid():
        profile = Profile()
        profile.user = User.objects.get(id=request.user.id)
      
        profile.save()
        return redirect(list_profiles)
        
    return render(request, 'social/create_profile.html', locals())

def save_profile(request):
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
