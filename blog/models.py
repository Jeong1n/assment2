from django.db import models
from user.models import UserManager
# Create your models here.
class Catagorymodel(models.Model):
    name = models.CharField(max_length=100)
    Explanation = models.CharField(max_length=100)
    def __str__ (self):
        return f"{self.name}"



class Article(models.Model):
    author = models.ForeignKey(UserManager, on_delete=models.CASCADE)
    Explanation = models.CharField(max_length=100)
    Catagory = models.ManyToManyField(Catagorymodel)
    Contents = models.CharField(max_length=100)
    