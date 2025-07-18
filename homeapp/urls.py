from django.urls import path
from . import views

urlpatterns=[
    path('',views.indexPage,name='index'),
    path('about',views.aboutPage,name='about'),
    path('contactus',views.contactusPage,name='contact-us'),
    path('projects',views.projectsPage,name='projects'),
    path('project_detail/<str:project_id>',views.projectDetailPage,name='project-detail'),
    path('cooperate',views.cooperationPage,name='cooperate'),
    path('cooperateon/<str:project_id>',views.cooperateonPage,name='cooperate-on'),
    path('products',views.productsPage,name="products"),
    path('product_detail/<str:product_id>',views.productDetailPage,name='product-detail'),
    path('news',views.newsPage,name='news'),
    path('news_detail/<str:news_id>',views.newsDetailPage,name='news-detail'),

]