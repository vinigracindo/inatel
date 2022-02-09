from django.db import models


class ScheduleWorkFile(models.Model):
    file = models.FileField(upload_to='imports')
    created_at = models.DateTimeField(auto_now_add=True)


class ScheduleWork(models.Model):
    file = models.ForeignKey(ScheduleWorkFile, on_delete=models.CASCADE)
    informations = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
