from django.db import models
from django.utils import timezone
# Create your models here.



class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(default=timezone.now)
