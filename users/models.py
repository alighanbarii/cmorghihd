from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Profile(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    username=models.CharField(max_length=300,blank=True,null=True)
    name=models.CharField(max_length=300)
    email=models.CharField(max_length=500)

    bio_summary=models.CharField(max_length=500)
    bio=models.TextField(max_length=5000)
    phone_number=models.CharField(max_length=30,null=True,blank=True)
    profile_image=models.ImageField(null=True,blank=True,upload_to='profiles/',default='profiles/default-user.jpg')
    social_github=models.CharField(max_length=500,null=True,blank=True)
    social_linkedin=models.CharField(max_length=500,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return str(self.name)

class Skill (models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    owner=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=150,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return self.name
    