from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import json

from .models import *

from random import randint as random
slg_r = "abcdefghijklmnopqrstuvwxyz0123456789"



def index(request):
    return render(request, "index.html")

def webquest(request, st):
    a = Quest.objects.filter(slag = st)
    return render(request, "view-quest.html")
    #return HttpResponse(a[0].text)


@method_decorator(csrf_exempt, name='dispatch')
class quest(View):
    def get(self, request):
        return render(request, "create-web-quest.html")

    def post(self, request):
        dt = request.body.decode('utf-8')

        _st = ""
        while len(_st) != 20:
            _st += slg_r[random(0,len(slg_r)-1)]

        print(dt.split('"'))
        print()

        d = {"text": dt, "slag": _st, "name": dt.split('"')[3]}
        print(d)
        Quest.objects.create(**d)
        return HttpResponse("return quest")

def find(request, st):
    al = Quest.objects.all()
    wq = []
    for item in al:
        if st.lower() in item.name.lower():
            wq.append({"Name": item.name, "URL": item.slag})
    _r = json.dumps(wq, ensure_ascii=False)
    return HttpResponse(_r)
