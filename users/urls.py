from django.urls import path
from . import views
urlpatterns=[
    path('profile/<str:pk>',views.profilePage,name='user-profile'),
    path('editprofile/<str:pk>',views.editProfilePage,name='edit-profile'),
    path('all',views.usersPage,name='user-all'),
]