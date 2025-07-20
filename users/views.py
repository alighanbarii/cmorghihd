from django.shortcuts import render
from .models import Profile
from django.http import Http404
# Create your views here.

def usersPage(request):
    profiles=Profile.objects.all()
    context={"profiles":profiles}
    return render(request, 'users/index.html',context)

def editProfilePage(request,pk):
    try:
        profile=Profile.objects.get(id=pk)
    except Exception as e:
        raise Http404("page doesnt exist")
    
    if profile is None:
        raise Http404("page doesnt exist")
    
    context={"profile":profile,'user':profile.user}
    return render(request,'users/edit_profile.html',context)

def profilePage(request,pk):
    try:
        profile=Profile.objects.get(id=pk)
    except Exception as e:
        raise Http404("page doesnt exist")
    
    if profile is None:
        raise Http404("page doesnt exist")
    
    context={"profile":profile,'user':profile.user}
    return render(request,'users/user_profile.html',context)