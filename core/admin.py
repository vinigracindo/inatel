from django.contrib import admin

from core.models import ScheduleWork, ScheduleWorkFile

# Register your models here.
admin.site.register(ScheduleWorkFile)
admin.site.register(ScheduleWork)
