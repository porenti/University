from django.contrib import admin

from .models import *

class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "rukovoditel", "name_napr")
    search_fields = ("name",)
    list_filter = ("name_napr", "name")

class PersonalAdmin(admin.ModelAdmin):
    list_display = ("name", "special")
    search_fields = ("name",)
    list_filter = ("special", "name")


class ChildrenAdmin(admin.ModelAdmin):
    list_display = ("name", "date_of_birth", "group")
    search_fields = ("name","group")
    list_filter = ("name", "date_of_birth", "group")


class WorkAdmin(admin.ModelAdmin):
    list_display = ("prepod", "group", "subject", "hours", "hours_end", "room")
    search_fields = ("prepod","group", "subject")
    list_filter = ("prepod", "group", "subject")

class RoomAdmin(admin.ModelAdmin):
    list_display = ("room_number","type_room")
    list_filter = ("room_number", "type_room")

class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ("type_room",)
    list_filter = ("type_room",)

class Closed_dayAdmin(admin.ModelAdmin):
    list_display = ("persona","date")
    list_filter = ("persona", "date")

class Blocked_dayAdmin(admin.ModelAdmin):
    list_display = ("group","date")
    list_filter = ("group", "date")


admin.site.register(Group, GroupAdmin)
admin.site.register(Blocked_day, Blocked_dayAdmin)
admin.site.register(Personal, PersonalAdmin)
admin.site.register(Children, ChildrenAdmin)
admin.site.register(Closed_day, Closed_dayAdmin)
admin.site.register(Room_type, RoomTypeAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Days)
admin.site.register(Raspisanie)
