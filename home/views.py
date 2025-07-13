from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):
    #template=loader.get_template('home/index.html')
    return render(request,'home/index.html')

def about(request):
    return render(request,'home/about.html')

def contactus(request):
    return render(request,'home/contactus.html')

def news(request):
    return render(request,'home/news.html')

def news_detail(request):
    return render(request,'home/news_detail.html')

def product_detail(request):
    return render(request,'home/product_detail.html')

def products(request):
    return render(request,'home/products.html')
