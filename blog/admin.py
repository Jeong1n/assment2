from django.contrib import admin
from blog.models import Catagorymodel, Article, Comment
# Register your models here.
admin.site.register(Catagorymodel)
admin.site.register(Article)
admin.site.register(Comment)