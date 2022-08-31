from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
from mdeditor.fields import MDTextField
from preferences.models import Preferences

class MyTitles(models.Model):

    name = models.CharField(default="student", max_length=1024)

class ContactMethod(models.Model):

    name = models.CharField(default="email", max_length=1024, help_text="how do you name this method? email or github or anything else?")
    link = models.URLField(default="example@gmail.com", max_length=1024, help_text="the link of your contact method.")
    icon = models.CharField(default="email", max_length=1024, help_text="for display on front page, use the icon name from this page: https://semantic-ui.com/elements/icon.html")

class SitePreference(Preferences):

    my_name = models.CharField(default="me", max_length=1024, help_text="your name.")
    my_brief_intro = MDTextField(default="I am a student.", max_length=1024, help_text="self introduction on front page.")
    my_photo = ProcessedImageField(upload_to='avatar2',
                                 default='avatar2/matthew.png',
                                 verbose_name='photo',
                                 # resize to valid size
                                 processors=[ResizeToFill(512,512)])

class Star(models.Model):

    link = models.URLField(default="www.google.com",  max_length=1024)      # all accessible running incidents