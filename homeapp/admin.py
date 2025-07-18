from django.contrib import admin

# Register your models here.
from .models import Project,Tag,Product,KeyFeature,Benefit,Image,Video,Requirement,ProductCategory
admin.site.register(Project)
admin.site.register(Product)
admin.site.register(KeyFeature)
admin.site.register(Benefit)
admin.site.register(Requirement)
admin.site.register(Image)
admin.site.register(Video)
admin.site.register(Tag)
admin.site.register(ProductCategory)