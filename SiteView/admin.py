from django.contrib import admin

# Register your models here.
from preferences.admin import PreferencesAdmin
from SiteView.models import MyPreferences

admin.site.register(MyPreferences, PreferencesAdmin)