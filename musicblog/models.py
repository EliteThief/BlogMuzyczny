from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=30)

class Post(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField()
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)


