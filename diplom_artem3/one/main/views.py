from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import json
import ast

from .models import *

from random import randint as random
slg_r = "abcdefghijklmnopqrstuvwxyz0123456789"



def index(request):
    return HttpResponse("main_page")
    #return render(request, "index.html")

def webquest(request, st):
    a = Quest.objects.filter(slag = st)
    return HttpResponse(a[0].text)


@method_decorator(csrf_exempt, name='dispatch')
class quest(View):
    def get(self, request):
        return HttpResponse("create quest")
        #return render(request, "create web course.html")

    def post(self, request):
        dt = request.body.decode('utf-8')
        print(dt)

        _st = ""
        while len(_st) != 20:
            _st += slg_r[random(0,len(slg_r)-1)]

        d = {"text": dt, "slag": _st}

        Quest.objects.create(**d)
        return HttpResponse("return quest")
