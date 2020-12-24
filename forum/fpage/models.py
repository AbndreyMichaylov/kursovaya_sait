from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Comment(models.Model):
    text = models.CharField(max_length=150)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    post_id = models.IntegerField(default=0)
    time = models.TimeField(default=datetime.now().time())
    def __str__(self):
        return self.text + ':' + self.user.username

class Post(models.Model):
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=300)
    username = models.ForeignKey(to=User, on_delete=models.CASCADE)
    comments = models.ManyToManyField(to=Comment, blank=True)
    time = models.TimeField(default=datetime.now().time())
    def __str__(self):
        return self.title
