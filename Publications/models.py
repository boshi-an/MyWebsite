from cgitb import text
from django.db import models

# Create your models here.

from mdeditor.fields import MDTextField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Publication(models.Model):
    name = models.CharField(max_length=1024, help_text="the name of the publication or project.")
    teaser = ProcessedImageField(upload_to='avatar2',
                                 default='avatar2/matthew.png',
                                 verbose_name='teaser',
                                 # resize to valid size
                                 processors=[ResizeToFill(512,512)],)
    introduction = MDTextField()
    addinfo = models.CharField(default='', max_length=1024, help_text="oral? best paper?")