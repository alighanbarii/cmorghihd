from django.db import models
import uuid


class Writer(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=300)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    key=models.CharField(max_length=150,null=True)
    title=models.CharField(max_length=200,null=True)
    created_at=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
# Create your models here.
class News(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)
    title=models.CharField(max_length=150)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    time=models.CharField(max_length=100)
    summary=models.TextField(max_length=1500,null=True)
    text=models.TextField(max_length=5000)
    writer=models.ForeignKey(Writer,on_delete=models.SET_NULL,null=True)
    images=models.ManyToManyField("Image")
    videos=models.ManyToManyField("Video")
    links=models.ManyToManyField("Link")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title



class Link(models.Model):
    id=models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True,unique=True)
    title=models.CharField(max_length=200)
    url=models.CharField(max_length=500)
    # news=models.ForeignKey(News,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Image(models.Model):
    id=models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True,unique=True)
    title=models.CharField(max_length=200)
    name=models.CharField(max_length=300)
    src=models.CharField(max_length=500)
    # news=models.ForeignKey(News,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class Video(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)
    title=models.CharField(max_length=200)
    name=models.CharField(max_length=300)
    src=models.CharField(max_length=500)
    # news=models.ForeignKey(News,on_delete=models.CASCADE)
    def __str__(self):
        return self.title