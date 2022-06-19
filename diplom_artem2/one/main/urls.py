from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('main/', index),
    path('quest/', quest.as_view()),
    path('webquest/<str:st>', webquest),
]
