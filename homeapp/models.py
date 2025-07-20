from django.db import models
import uuid
# Create your models here.

class ProductCategory(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)
    class_number=models.IntegerField()
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)
    name=models.CharField(max_length=100)
    category=models.ForeignKey(ProductCategory,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=150)
    slogan=models.CharField(max_length=200)
    short_desc=models.TextField(max_length=1000)
    long_desc=models.TextField(max_length=3000,null=True,blank=True)
    videos=models.ManyToManyField("Video",blank=True)
    images=models.ManyToManyField("Image",blank=True)
    def __str__(self):
        return f"{self.name} {self.title}"

class Video(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    name=models.CharField(max_length=200)
    src=models.CharField(max_length=500,null=False,blank=False)
    def __str__(self):
        return self.name

class Image(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)
    name=models.CharField(max_length=100)
    src=models.CharField(max_length=500,null=False,blank=False)
    def __str__(self):
        return self.name

class KeyFeature(models.Model):
    id=models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True,unique=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    description=models.TextField(max_length=1000)
    def __str__(self):
        return self.title

class Benefit(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    text=models.CharField(max_length=300)
    def __str__(self):
        return self.text

class Requirement(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    text=models.CharField(max_length=300)
    def __str__(self):
        return self.text

    
class Tag(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    name=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)