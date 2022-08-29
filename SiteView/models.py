from django.db import models

# Create your models here.
from mdeditor.fields import MDTextField
from preferences.models import Preferences

class MyPreferences(Preferences):
    portal_contact_email = models.EmailField()
