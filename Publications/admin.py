from django.contrib import admin

# Register your models here.

from . import models

# Define the admin class
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('Name',)

admin.site.register(models.Pulication, PublicationAdmin)