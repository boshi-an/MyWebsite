from django.contrib import admin

# Register your models here.

from . import models

# Define the admin class
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'teaser', 'introduction', 'addinfo')

admin.site.register(models.Publication, PublicationAdmin)