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

def questplay(request):
    return render(request, "play.html")

def about(request):
    return render(request, "about.html")

@method_decorator(csrf_exempt, name='dispatch')
class quest(View):
    def get(self, request):
        return render(request, "create web course.html")

    def post(self, request):
        _r = {}
        #post_body = json.loads(request.body)
        dt = request.body.decode('utf-8')
        cl_dt = ast.literal_eval(dt)#.replace("\\","") #clear data
        print(cl_dt)


        webquest = cl_dt["name"]
        groups = cl_dt["roles"]
        pools = cl_dt["pools"]
        questions = cl_dt["questions"]

        wb = {"name": webquest}
        WebQuest.objects.create(**wb)
        wb_ob = WebQuest.objects.filter(name = wb["name"])
        wb_pk = wb_ob[0].pk
        for item in groups:
            g = {"name": groups[item]["name"], "webquest": wb_pk, "role_id": item}
            Role.objects.create(**g)

        for jitem in pools:
            _st = ""
            while len(_st) != 20:
                _st += slg_r[random(0,len(slg_r)-1)]
            p = {"name": pools[jitem]["name"], "role_id": pools[jitem]['forWhom'], "slug": _st, "quest_pool_id": jitem}
            Quest_pool.objects.create(**p)
            _r_st = "/webquest/"+ _st
            _r[_r_st] = {"Роль": item, "Пул": pools[jitem]["name"]}

        for item in questions:
            print(questions)
            q = {"name": questions[item]["name"], "text": questions[item]["question"], "type": questions[item]["type"], "answer": questions[item]["answer"], "pool": questions[item]["pool_id"], "question_id": item}
            Quest.objects.create(**q)

        print(_r)
        return JsonResponse(_r)


def webquest(request,st):
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

def getall(request,st):
    print(st)
    all_wq = WebQuest.objects.all()
    wq = []
    for item in all_wq:
        if st.lower() in item.name.lower():
            wq.append({"Название": item.name, 'pk': item.pk, "Роли": []})
        #[{'Название': 'анонимные мастурбаторы', 'pk': 3}]
    for item in wq:
        rols = Role.objects.filter(webquest = item['pk'])
        for jitem in rols:
            _q = []
            qp = Quest_pool.objects.filter(role_id = jitem.role_id)
            for kitem in qp:
                _q.append({"Пул вопросов": kitem.name, "Путь": kitem.slug})
            item["Роли"].append({'Роль': jitem.name, "id": jitem.role_id, "Пулы": _q})

    _r = json.dumps(wq, ensure_ascii=False)
    return HttpResponse(_r)
