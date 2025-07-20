from django.contrib import admin
from .models import News,Category,Writer,Image,Video,Link
# Register your models here.
admin.site.register(News)
admin.site.register(Category)
admin.site.register(Writer)
admin.site.register(Image)
admin.site.register(Video)
admin.site.register(Link)
