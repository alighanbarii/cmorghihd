from django.shortcuts import render,redirect
from .models import News
# Create your views here.
from .forms import NewsForm


def newsPage(request):
    newses=News.objects.all()
    context={"newses":newses}
    return render(request,'news/news.html',context)

def newsDetailPage(request,pk):
    news=News.objects.get(id=pk)
    context={'news':news}
    return render(request,'news/news_detail.html',context)

def createNews(request):
    if request.method=="POST":
        form=NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            return redirect('create-news')
    
    form=NewsForm()
    context={'form':form}
    return render(request,'news/create_news.html',context)

def updateNews(request,pk):
    if request.method=="POST":
        news=News.objects.get(id=pk)
        if news is not None:
            form=NewsForm(request.POST,instance=news)
            if form.is_valid():
                form.save()
                return redirect('news')
            else:
                ##not a valid form
                return redirect("news")
        else:
            ## news is not in the database
            return redirect('news')
    news=News.objects.get(id=pk)
    
    if news is not None:
        form =NewsForm(instance=news)
        context={"form":form,"news_id":pk}
        return render(request,'news/update_news.html',context)
    else: 
        return redirect('news')

def deleteNews(request,pk):
    news=News.objects.get(id=pk)
    if news is None:
        return redirect('news')
    if request.method=="POST":
        news.delete()
        return redirect ('news')
    
    context={'news':news,'news_id':news.id}
    return render(request,'news/delete_news.html',context)

