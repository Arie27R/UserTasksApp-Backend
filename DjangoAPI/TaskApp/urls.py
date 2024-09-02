from django.urls import re_path
from TaskApp import views

urlpatterns = [
    re_path(r'^task/$', views.taskApi),
    re_path(r'^task/([0-9]+)$',views.taskApi)
]
