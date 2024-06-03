from django.urls import path

from . import views


app_name = 'monitor'
urlpatterns = [
    path("", views.index, name="index"),
    path('create/', views.created_task, name='create_task')
]
