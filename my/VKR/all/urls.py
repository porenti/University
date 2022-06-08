from django.contrib import admin
from django.urls import path, include
from all.views import *


urlpatterns = [
    path('group/create/', GroupCreateView.as_view()),
    path('group/list/', GroupListView.as_view()),
    path('blocked_day/detail/<int:pk>', Blocked_dayDetailView.as_view()),
    path('blocked_day/create/', Blocked_dayCreateView.as_view()),
    path('blocked_day/list/', Blocked_dayView.as_view()),
    path('group/detail/<int:pk>', GroupDetailView.as_view()), ###
    path('personal/create/', PersonalCreateView.as_view()),
    path('personal/list/', PersonalListView.as_view()),
    path('personal/detail/<int:pk>', PersonalDetailView.as_view()),
    path('children/create/', ChildrenCreateView.as_view()),
    path('children/list/', ChildrenListView.as_view()),
    path('children/detail/<int:pk>', ChildrenDetailView.as_view()),
    path('closed_day/create/', Closed_dayCreateView.as_view()),
    path('closed_day/list/', Closed_dayListView.as_view()),
    path('closed_day/detail/<int:pk>', Closed_dayDetailView.as_view()),
    path('room_type/create/', Room_typeCreateView.as_view()),
    path('room_type/list/', Room_typeListView.as_view()),
    path('room_type/detail/<int:pk>', Room_typeDetailView.as_view()),
    path('room/create/', RoomCreateView.as_view()),
    path('room/list/', RoomListView.as_view()),
    path('room/detail/<int:pk>', RoomDetailView.as_view()),
    path('work/create/', WorkCreateView.as_view()),
    path('work/list/', WorkListView.as_view()),
    path('work/detail/<int:pk>', WorkDetailView.as_view()),
    path('finished/create/', FinishedCreateView.as_view()),
    path('finished/list/', FinishedListView.as_view()),
    path('finished/detail/<int:pk>', FinishedDetailView.as_view()),
    path('raspisanie/list/', RaspisanieListView.as_view()),
    path('days/create/', DaysCreateView.as_view()),
    path('days/list/', DaysListView.as_view()),
    path('days/detail/<int:pk>', DaysDetailView.as_view()),
]
