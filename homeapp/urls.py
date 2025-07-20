from django.urls import path
from . import views

urlpatterns=[
    path('',views.indexPage,name='index'),
    path('about',views.aboutPage,name='about'),
    path('contactus',views.contactusPage,name='contact-us'),
    path('cooperate',views.cooperationPage,name='cooperate'),
    path('cooperateon/<str:project_id>',views.cooperateonPage,name='cooperate-on'),
    path('products',views.productsPage,name="products"),
    path('product_detail/<str:product_id>',views.productDetailPage,name='product-detail'),
    

]