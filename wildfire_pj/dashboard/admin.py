from django.contrib import admin

# Register your models here.
from dashboard import models

# class WildFireAdmin(admin.ModelAdmin):
#   list_display = ('country', 'population')

admin.site.register(models.Wildfire)