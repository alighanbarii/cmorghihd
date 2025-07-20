from django.urls import path
from . import views
urlpatterns=[
    path('',views.indexPage,name='projects'),
    path('<str:pk>',views.projectDetailPage,name='project-detail'),
    path('send_resume/<str:pk>',views.sendResumePage,name="send-resume")
]