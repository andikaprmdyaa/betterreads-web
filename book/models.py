# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    image_link = models.CharField(max_length=100)
