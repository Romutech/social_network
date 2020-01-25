from django.shortcuts import render

def list_profiles(request):

    return render(request, 'social/list_profiles', locals())

def show_profile(request):

    return render(request, 'social/show_profile', locals())

def edit_profile(request):

    return render(request, 'social/edit_profile', locals())

def save_comment(request):

    return render(request, 'social/save_comment', locals())

def save_status(request):

    return render(request, 'social/save_status', locals())
