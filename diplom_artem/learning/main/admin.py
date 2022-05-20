from django.contrib import admin

from .models import *

class coursesAdmin(admin.ModelAdmin):
    list_display = ("course_name", "author", "description")
    search_fields = ("author", "course_name")
    list_filter = ("course_name", "author")

class answerAdmin(admin.ModelAdmin):
    list_display = ("answer", "name_answer", "key")
    search_fields = ("name_answer", "key")
    list_filter = ("name_answer",)


admin.site.register(people)
admin.site.register(courses, coursesAdmin)
admin.site.register(answer, answerAdmin)