from rest_framework import serializers
from all.models import *

class GroupDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class Blocked_dayDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blocked_day
        fields = '__all__'

class PersonalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'

class ChildrenDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = '__all__'

class Closed_dayDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Closed_day
        fields = '__all__'

class Room_typeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room_type
        fields = '__all__'

class RoomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class WorkDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'

class FinishedDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finished
        fields = '__all__'

class RaspisanieDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Raspisanie
        fields = ['date', 'json']

class DaysDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Days
        fields = '__all__'
