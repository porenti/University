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
    return render(request, "index.html")

@method_decorator(csrf_exempt, name='dispatch')
class quest(View):
    def get(self, request):
        return render(request, "create web course.html")

    def post(self, request):
        _r = {}
        #post_body = json.loads(request.body)
        dt = request.body.decode('utf-8')
        dt = dt.replace('\n','')
        cl_dt = ast.literal_eval(dt) #clear data
        print(cl_dt)
        print()


        webquest = cl_dt["webquest"]
        groups = cl_dt["groups"]
        pools = cl_dt["pools"]
        questions = cl_dt["questions"]

        wb = {"name": webquest}
        print(wb)
        WebQuest.objects.create(**wb)
        wb_ob = WebQuest.objects.filter(name = wb["name"])
        wb_pk = wb_ob[0].pk
        print(wb_pk)  #id вебквеста

        for item in groups:
            g = {"name": item["name"], "webquest": wb_pk, "role_id": item["id"]}
            Role.objects.create(**g)

        for jitem in pools:
            for item in jitem["forWhom"]:
                _st = ""
                while len(_st) != 20:
                    _st += slg_r[random(0,len(slg_r)-1)]
                p = {"name": jitem["name"], "role_id": item, "slug": _st, "quest_pool_id": jitem["id"]}
                Quest_pool.objects.create(**p)
                _r_st = "/webquest/"+ _st
                _r[_r_st] = {"Роль": item, "Пул": jitem["name"]}

        for item in questions:
            q = {"name": item["name"], "text": item["question"], "type": item["type"], "answer": item["answer"], "pool": item["pool_id"], "question_id": item["id"]}
            Quest.objects.create(**q)

        return JsonResponse(_r)


def webquest(self,st):
    print(st)
    qp = Quest_pool.objects.filter(slug = st)[0]
    name_pool = qp.name
    role_id = qp.role_id
    r = Role.objects.filter(role_id = role_id)[0]
    name_role = r.name
    wq = WebQuest.objects.filter(pk = r.webquest)[0]
    name_wq = wq.name
    _r_dict = {"name_wq": name_wq,
                "name_pool": name_pool,
                "name_role": name_role,
                "quests": []}
    a = Quest.objects.filter(pool = qp.quest_pool_id)
    for item in a:
        _r_dict["quests"].append({"Текст вопроса:": item.text,
                                "Тип:": item.type,
                                "answer": item.answer})
    print(_r_dict)
    _r = json.dumps(_r_dict, ensure_ascii=False)
    return HttpResponse(_r)
