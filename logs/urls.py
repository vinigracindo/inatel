from django.urls import path

from logs import views

app_name = 'logs'

urlpatterns = [
    path('', views.list, name='list'),
    path('detail/<int:log_pk>/', views.view_reqres, name='view_reqres'),
]
