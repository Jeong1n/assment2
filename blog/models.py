from django.db import models
# Create your models here.
class Catagorymodel(models.Model):
    name = models.CharField(max_length=100)
    Explanation = models.CharField(max_length=100)
    def __str__ (self):
        return f"{self.name}"

class Article(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    Catagory = models.ManyToManyField(Catagorymodel)
    Contents = models.CharField(max_length=100)

class Comment(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    Article = models.ForeignKey(Article, on_delete=models.CASCADE)
    Comment = models.CharField(max_length=100)