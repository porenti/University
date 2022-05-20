from django import forms
from .models import *

class AddCourse(forms.Form):
    course_name = forms.CharField(max_length=255, label = 'Название курса')
    author = forms.CharField(max_length=255, label = 'Автор')
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label = 'Описание')


class addAnswer(forms.Form):
    name_answer = forms.CharField(max_length=255)
    answer = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    key = forms.CharField(max_length=255)
    course = forms.ModelChoiceField(queryset=courses.objects.all())
