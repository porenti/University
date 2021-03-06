from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


from .views import *

urlpatterns = [
    path("", index, name='home'),
    path("quest/<int:quest_id>", quest_return, name="quest"),
    path("courses/", course_list, name='courses'),
    path("courses/<int:course_id>", course_info, name='course_info'),
    path("add_course/", add_course, name='add_course'),
    path("add_question/", add_question, name='add_question'),
    path("about/", about, name='about'),
    path("login/", login, name='login')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
