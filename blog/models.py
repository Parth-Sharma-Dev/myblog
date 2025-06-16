from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(100)
    body = models.CharField(1000000)
    create_at = models.DateTimeField(default=datetime.now, blank=True)

class Contact(models.Model):
    name = models.CharField(100)
    email = models.EmailField(100)
    message = models.TextField()
    date_time = models.DateTimeField()