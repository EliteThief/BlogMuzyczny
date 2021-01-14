from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=400)


class Channel(models.Model):
    channel_name = models.CharField(max_length=400)
    date_of_creation = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class VideoInfo(models.Model):
    artist_name = models.CharField(max_length=400)
    album_name = models.CharField(max_length=400)
    year_of_prod = models.DateField(default=timezone.now)
    description = models.TextField(max_length=5000)


class Video(models.Model):
    views = models.IntegerField()
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    video_info = models.ForeignKey(VideoInfo, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    file = models.FileField()

class CommentSection(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)


class Comment(models.Model):
    date_of_posting = models.DateTimeField(default=timezone.now)
    content = models.CharField(max_length=400)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    comment_section = models.ForeignKey(CommentSection, on_delete=models.CASCADE)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)