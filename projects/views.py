from django.shortcuts import render,redirect
from .models import Project
from django.http import Http404
from users.models import Profile
# Create your views here.

def indexPage(request):
    projects=Project.objects.all()
    context={'projects':projects}
    return render(request,'projects/index.html',context)
def projectDetailPage(request,pk):
    project=Project.objects.get(id=pk)
    if project is None:
        raise Http404('page not found!')

    context={'project':project}
    return render(request,'projects/project_detail.html',context)

def sendResumePage(request,pk):
    profile=Profile.objects.first()
    user=profile.user
    context={"profile":profile,"user":user}
    return render(request,'users/edit_profile.html',context)