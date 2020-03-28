from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BlogEntry(models.Model):
    article = models.CharField(max_length=4000)
    heading = models.CharField(max_length=400)
    subheading = models.CharField(max_length=800, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    pubDate = models.DateField("Date Published")
