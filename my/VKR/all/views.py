from django.shortcuts import render
from rest_framework import generics
from all.serializers import *
from all.models import *

class GroupCreateView(generics.CreateAPIView):
    serializer_class = GroupDetailSerializer

class Blocked_dayView(generics.ListAPIView):
    serializer_class = Blocked_dayDetailSerializer
    queryset = Blocked_day.objects.all()

class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupDetailSerializer
    queryset = Group.objects.all()

class Blocked_dayCreateView(generics.CreateAPIView):
    serializer_class = Blocked_dayDetailSerializer

class GroupListView(generics.ListAPIView):
    serializer_class = GroupDetailSerializer
    queryset = Group.objects.all()

class Blocked_dayDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Blocked_dayDetailSerializer
    queryset = Blocked_day.objects.all()
###Personal
class PersonalCreateView(generics.CreateAPIView):
    serializer_class = PersonalDetailSerializer

class PersonalListView(generics.ListAPIView):
    serializer_class = PersonalDetailSerializer
    queryset = Personal.objects.all()

class PersonalDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonalDetailSerializer
    queryset = Personal.objects.all()
###Children
class ChildrenCreateView(generics.CreateAPIView):
    serializer_class = ChildrenDetailSerializer

class ChildrenListView(generics.ListAPIView):
    serializer_class = ChildrenDetailSerializer
    queryset = Children.objects.all()

class ChildrenDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChildrenDetailSerializer
    queryset = Children.objects.all()
###Closed_day
class Closed_dayCreateView(generics.CreateAPIView):
    serializer_class = Closed_dayDetailSerializer

class Closed_dayListView(generics.ListAPIView):
    serializer_class = Closed_dayDetailSerializer
    queryset = Closed_day.objects.all()

class Closed_dayDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Closed_dayDetailSerializer
    queryset = Closed_day.objects.all()
###Room_type
class Room_typeCreateView(generics.CreateAPIView):
    serializer_class = Room_typeDetailSerializer

class Room_typeListView(generics.ListAPIView):
    serializer_class = Room_typeDetailSerializer
    queryset = Room_type.objects.all()

class Room_typeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Room_typeDetailSerializer
    queryset = Room_type.objects.all()
###Room
class RoomCreateView(generics.CreateAPIView):
    serializer_class = RoomDetailSerializer

class RoomListView(generics.ListAPIView):
    serializer_class = RoomDetailSerializer
    queryset = Room.objects.all()

class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomDetailSerializer
    queryset = Room.objects.all()
###Work
class WorkCreateView(generics.CreateAPIView):
    serializer_class = WorkDetailSerializer

class WorkListView(generics.ListAPIView):
    serializer_class = WorkDetailSerializer
    queryset = Work.objects.all()

class WorkDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkDetailSerializer
    queryset = Work.objects.all()
###Finished
class FinishedCreateView(generics.CreateAPIView):
    serializer_class = FinishedDetailSerializer

class FinishedListView(generics.ListAPIView):
    serializer_class = FinishedDetailSerializer
    queryset = Finished.objects.all()

class FinishedDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FinishedDetailSerializer
    queryset = Finished.objects.all()
###Raspisanie
class RaspisanieListView(generics.ListAPIView):
    serializer_class = RaspisanieDetailSerializer
    queryset = Raspisanie.objects.all()
###Days
class DaysCreateView(generics.CreateAPIView):
    serializer_class = DaysDetailSerializer

class DaysListView(generics.ListAPIView):
    serializer_class = DaysDetailSerializer
    queryset = Days.objects.all()

class DaysDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DaysDetailSerializer
    queryset = Days.objects.all()
