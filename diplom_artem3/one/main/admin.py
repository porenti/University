from django.contrib import admin

from .models import *

class QuestAdmin(admin.ModelAdmin):
    list_dispay = ('id', 'slag', 'name')
    search_fields = ('name',)

admin.site.register(Quest, QuestAdmin)
