from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


from .views import *


urlpatterns = [
    path('', index),
    path('quest/', quest.as_view()),
    path('webquest/<str:st>', webquest),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
