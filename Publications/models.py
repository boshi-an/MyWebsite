from django.db import models

# Create your models here.

from mdeditor.fields import MDTextField

class Pulication(models.Model):
    Name = models.CharField(max_length=1024)
    Introduction = MDTextField()