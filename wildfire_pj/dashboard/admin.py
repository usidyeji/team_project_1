from django.contrib import admin

# Register your models here.
from dashboard import models

# class WildFireAdmin(admin.ModelAdmin):
#   list_display = ('country', 'population')

admin.site.register(models.Wildfire)
admin.site.register(models.MonthCause)
admin.site.register(models.WildFire_day)
admin.site.register(models.WildFire_time)