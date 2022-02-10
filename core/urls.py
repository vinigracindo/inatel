from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('schedule/import/', views.import_work_scheduling,
         name='import-work-schedule'),
    path('schedule/list/', views.schedule_list, name='schedule-list'),
    path('schedule/detail/<int:schedule_pk>/',
         views.schedule_detail, name='schedule-detail')
]
