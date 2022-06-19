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
    return HttpResponse("Home")

@method_decorator(csrf_exempt, name='dispatch')
class quest(View):
    def get(self, request):
        return HttpResponse("хуй")

    def post(self, request):
        #post_body = json.loads(request.body)
        dt = request.body.decode('utf-8')
        dt = dt.replace('\n','')
        cl_dt = ast.literal_eval(dt) #clear data
        print(cl_dt)
        print()


        #webquest = cl_dt["webquest"]
        groups = cl_dt["groups"]
        pools = cl_dt["pools"]
        questions = cl_dt["questions"]

        wb = {"name": webquest}
        print(wb)
        WebQuest.objects.create(**wb)
        wb_ob = WebQuest.objects.filter(name = wb["name"])
        wb_pk = wb_ob[0].pk
        print(wb_ob)  #id вебквеста

        for item in groups:
            g = {"name": item["name"], webquest: wb_pk, "role_id": item["role_id"]}
            Role.objects.create(**g)
            for jitem in pools:
                if item['name'] in jitem['forWhom'][0]:
                    _st = ""
                    while len(_st) != 20:
                        _st += slg_r[random(0,len(slg_r))]
                    p = {"name": jitem["name"], "role": g_ob, "slug": _st}
                    Quest_pool.object.create(**p)




        data = {'message': 'This is a POST request'}
        return JsonResponse(data)
