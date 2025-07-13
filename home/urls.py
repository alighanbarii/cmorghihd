from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("news", views.news, name="news"),
    path("contactus", views.contactus, name="contactus"),
    path("products", views.products, name="index"),
    path("news_detail", views.news_detail, name="news_detail"),
    path("product_detail", views.product_detail, name="product_detail"),

    
]