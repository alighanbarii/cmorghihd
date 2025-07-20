from django.db import models
import uuid
# Create your models here.

class Project(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    title=models.CharField(max_length=200)
    project_image=models.ImageField(null=True,blank=True,default='projects/default-project.jpg')
    started_at=models.DateTimeField(auto_now_add=True)
    closes_at=models.DateTimeField(null=True,blank=True)
    description_summary=models.TextField(max_length=1000)
    description=models.TextField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title