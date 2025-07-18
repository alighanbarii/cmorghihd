from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.



def indexPage(request):
    projects=Project.objects.all()
    context={"projects":projects}
    return render(request,'homeapp/index.html',context)

def aboutPage(request):
    context={}
    return render(request,'homeapp/about.html',context)

def contactusPage(request):
    context={}
    return render(request,'homeapp/contactus.html',context)

def projectsPage(request):
    projects=Project.objects.all()
    context={"projects":projects,'product_id':1}
    return render(request,'homeapp/projects.html',context)
def projectDetailPage(request,project_id):
    context={"project_id":project_id}
    return render(request,'homeapp/project_detail.html',context)

def productsPage(request):
    context={"product_id":"1"}
    return render(request,'homeapp/products.html',context)

def productDetailPage(request,product_id):
    
    context={"product_id":product_id}
    return render(request,'homeapp/product_detail.html',context)


def cooperationPage(request):
    projects=Project.objects.all()
    context={"projects":projects}
    return render(request,'homeapp/cooperation.html',context)
def cooperateonPage(request,project_id):
    return render(request,'homeapp/cooperateon.html',{"project_id":project_id})

def newsPage(request):
    context={}
    return render(request,'homeapp/news.html',context)

def newsDetailPage(request,news_id):
    context={"news_id":news_id}
    return render(request,'homeapp/news_detail.html',context)