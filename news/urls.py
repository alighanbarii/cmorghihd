from django.urls import path
from . import views

urlpatterns=[
    path('',views.newsPage,name="news"),
    path('<str:pk>/',views.newsDetailPage,name='news-detail'),
    path('create',views.createNews,name='create-news'),
    path('update/<str:pk>',views.updateNews,name='update-news'),
    path('delete/<str:pk>',views.deleteNews,name="delete-news")
]