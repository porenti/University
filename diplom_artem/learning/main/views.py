from django.http import HttpResponse,Http404
from django.shortcuts import render

from .models import *
from .forms import *


def index(request):
    return render(request, 'main/index.html')

def login(request):
    return HttpResponse("login")

def course_list(request):
    courses_list = courses.objects.all()
    return render(request, "main/course_list.html", {"list_c": courses_list})

def about(request):
    return render(request, 'main/about.html')

def quest_return(request, quest_id):
    #передаем 7 - значное число, первые 3 - номер курса, 1 - номер шаблона, 3 - номер вопроса
    _str = str(quest_id)
    if len(_str) != 7:
        raise Http404()
        #return HttpResponse("Ты долбоеб")
    else:
        context = {
            "Title": "Вопрос",
            "id_course": _str[0:3],
            "number_shablon": _str[3],
            "id_answer": _str[4:7]
        }
        return render(request, 'main/test.html', context = context)

def course_info(request, course_id):
    if len(str(course_id)) != 3:
        raise Http404()
    return HttpResponse(course_id)

def add_course(request):
    if request.method == "POST":
        form = AddCourse(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            try:
                courses.objects.create(**form.cleaned_data)
            except:
                form.add_error(None, 'Ошибка добавления курса')
    else:
        form = AddCourse()
    return render(request, 'main/add_course.html', {'form': form})

def add_question(request):
    if request.method == "POST":
        form = addAnswer(request.POST)
        if form.is_valid():
            z = courses.objects.filter(course_name = form.cleaned_data.get('course'))
            try:
                a = answer.objects.create(name_answer=form.cleaned_data["name_answer"], answer=form.cleaned_data["answer"], key=form.cleaned_data["key"])
                a.course.set(z)
            except:
                form.add_error(None, 'Ошибка добавления задания')
    else:
        form = addAnswer()
    return render(request, 'main/add_question.html', {'form': form})