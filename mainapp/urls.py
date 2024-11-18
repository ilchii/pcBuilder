from django.urls import path, include, re_path
from mainapp.views import index

urlpatterns = [
    path('', index, name="index"),
]