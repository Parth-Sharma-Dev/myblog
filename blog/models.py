from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(100)
    body = models.CharField(1000000)
    create_at = models.DateTimeField(default=datetime.now, blank=True)