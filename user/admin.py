from django.contrib import admin
from user.models import UserManager
from user.models import UserProfile

# Register your models here.
admin.site.register(UserManager)
admin.site.register(UserProfile)