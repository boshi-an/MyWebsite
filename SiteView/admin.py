from django.contrib import admin

# Register your models here.
from preferences.admin import PreferencesAdmin
from SiteView.models import SitePreference
from . import models

admin.site.register(SitePreference, PreferencesAdmin)

class ContactMethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
class MyTitleAdmin(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(models.ContactMethod, ContactMethodAdmin)
admin.site.register(models.MyTitles, MyTitleAdmin)