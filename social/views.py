from django.shortcuts import render, redirect

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
