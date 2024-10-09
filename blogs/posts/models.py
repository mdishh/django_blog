from django.db import models
from datetime import datetime
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateField(default=datetime.now, blank=True)
    body = models.CharField(max_length=1000)
