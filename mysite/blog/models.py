from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    genre = models.CharField(max_length=10)
    member = models.TextField()

