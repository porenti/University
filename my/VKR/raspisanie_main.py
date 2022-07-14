from random import randint as random
import sqlite3 as sql
from time import time, strftime, gmtime
from json import dumps


#Извлечение данных из бд

try:
    con = sql.connect('db.sqlite3')
    cur = con.cursor()
    ### Извлекаем дни
    _sql = "Select * from all_days"
    cur.execute(_sql)
    _days = list(cur.fetchall())
    print(_days)
    _now_time = strftime('%d %m',gmtime(time())).split(' ')
    _day_now = int(_now_time[0])
    _month_now = int(_now_time[1])
    list_days_for_generate = {}
    for item in _days:
        _month = int(item[1].split('-')[1])
        _day = int(item[1].split('-')[2])
        if _month > _month_now:
            list_days_for_generate[item[0]] = item[1]
        elif _month == _month_now:
            if _day > _day_now:
                list_days_for_generate[item[0]] = item[1]


    #print(list_days_for_generate) #Список дней на когда генерировать расписание
    #Смотрим группы, которые еще остались с часами
    _sql = "SELECT * FROM all_work WHERE hours > hours_end"
    _works = con.execute(_sql).fetchall()
    works_group = {}
    _t = [] # айди групп
    for item in _works:
        if item[4] not in _t:
            _t.append(item[4])
    #print(_works)
    #print(_t)
    rooms = {}
    _sql = "Select * from all_room_type"
    types = con.execute(_sql).fetchall()
    _sql = "Select * from all_room"
    room = con.execute(_sql).fetchall()
    for jitem in types:
        rooms[jitem[0]] = []
        for item in room:
            if item[2] == jitem[0]:
                rooms[jitem[0]].append(item[1])
    print(rooms) #DICT 3




    need_teacher_dict = {} #id преподов которых нам нужны

    for i in _t:
        _sql = "SELECT name, id FROM all_group WHERE id = {}".format(i)
        _z = con.execute(_sql).fetchall()
        _name = _z[0][1]
        works_group[_name] = {"Предметы": []}
        _sql = "Select prepod_id, subject, hours, hours_end, room_id from all_work where (group_id = {}) and (hours > hours_end)".format(i)
        _z = con.execute(_sql).fetchall()
        for item in _z:
            _sql = "SELECT name, id from all_personal WHERE id = {}".format(item[0])
            _p = con.execute(_sql).fetchall()
            works_group[_name]["Предметы"].append({"Дисциплина": item[1], "Преподаватель": _p[0][0], "Часов осталось": item[2]-item[3], "Подходящий тип аудиторий": item[4]})
            if _p[0][1] not in need_teacher_dict:
                need_teacher_dict[_p[0][1]] =_p[0][0]
    #dict 2
    print(need_teacher_dict)
    #dict 1
    print(works_group) #Получили словарь групп у которых есть пары
    print(list_days_for_generate)

except:
    print("Ошибка при извлечении данных")
    print(e)
finally:
    con.close()


print('\n'*3)

# перебираем дни
_ras = {}
print('\n'*3)
for jitem in list_days_for_generate:
    try:
        # dont use prepod  ### DUP
        DUP = []
        con = sql.connect('db.sqlite3')
        cur = con.cursor()
        _sql = "Select persona_id from all_closed_day where date = '{}'".format(list_days_for_generate[jitem])
        cur.execute(_sql)
        _data_dup = cur.fetchall()
        for item in _data_dup:
            DUP.append(item[0])
        #print(DUP)
        #dont use group ### dug
        DUG = []
        con = sql.connect('db.sqlite3')
        cur = con.cursor()
        _sql = "Select group_id from all_blocked_day where date = '{}'".format(list_days_for_generate[jitem])
        cur.execute(_sql)
        _data_dug = cur.fetchall()
        for item in _data_dug:
            DUG.append(item[0])
        #print(DUG)
    except:
        print('Ошибка при извлечении данных о нерабочих днях')
    finally:
        con.close()
    #############################################
    _raspisanie = {"Преподаватель": {}, "Группа": {}, "Кабинет": {}}
    #формируем большую матрицу
    for item in need_teacher_dict:
        if item not in DUP:
            _raspisanie["Преподаватель"][need_teacher_dict[item]] = {'id': item, "Пары":
                                                            {"1": {"Группа": "", "Дисциплина": "", "Аудитория": ""},
                                                            "2": {"Группа": "", "Дисциплина": "", "Аудитория": ""},
                                                            "3": {"Группа": "", "Дисциплина": "", "Аудитория": ""},
                                                            "4": {"Группа": "", "Дисциплина": "", "Аудитория": ""},
                                                            "5": {"Группа": "", "Дисциплина": "", "Аудитория": ""}}}
    for item in works_group:
        if item not in DUG:
            _raspisanie["Группа"][str(item)] = {'id': item, "Пары":
                                                            {"1": {"Преподаватель": "", "Дисциплина": "", "Аудитория": ""},
                                                            "2": {"Преподаватель": "", "Дисциплина": "", "Аудитория": ""},
                                                            "3": {"Преподаватель": "", "Дисциплина": "", "Аудитория": ""},
                                                            "4": {"Преподаватель": "", "Дисциплина": "", "Аудитория": ""},
                                                            "5": {"Преподаватель": "", "Дисциплина": "", "Аудитория": ""}}}
    for item in rooms:
        for i in rooms[item]:
            _raspisanie["Кабинет"][i] = {"Пары":
                                            {"1": {"Преподаватель": "", "Дисциплина": ""},
                                            "2": {"Преподаватель": "", "Дисциплина": ""},
                                            "3": {"Преподаватель": "", "Дисциплина": ""},
                                            "4": {"Преподаватель": "", "Дисциплина": ""},
                                            "5": {"Преподаватель": "", "Дисциплина": ""}}}
    ### _raspisanie # dict 4
    print("\n"*3)
    #for item in _raspisanie:
        #for k in _raspisanie[item]:
            #print(k, _raspisanie[item][k])
    #print("\n"*3)
    _count_lessons = {} #количество пар
    for i in _raspisanie["Преподаватель"]:#формируем расписание для преподов которые работают
        print(i)
        _id = _raspisanie["Преподаватель"][i]["id"]
        _count_lessons[_id] = 0 #Количество пар у препода
        try:
            con = sql.connect('db.sqlite3')
            cur = con.cursor()
            _sql = "Select * from all_work where prepod_id = {}".format(_id)
            cur.execute(_sql)
            _data_dug = cur.fetchall()
        finally:
            con.close()

        predmet_list = []
        for item in _data_dug:
            predmet_list.append([item[1],(item[2]-item[3])//2,item[4],item[6]])

        print(predmet_list)
        _r = []
        for item in predmet_list:
            for j in range(item[1]):
                _r.append({"Группа": item[2], "Дисциплина": item[0], "Пары:": item[1], "Тип аудитории": item[3]})
        c = 0
        while True:
            c += 1
            try:
                if (_count_lessons[_id] >= 4) or (len(predmet_list) == 0) or len(_data_dug) == 1 or c > 25:
                    break

                a = len(_r)-1
                anti_povtor = []
                for item in range(1,6):
                    para = _r[random(0,a)]
                    if len(anti_povtor)-len(set(anti_povtor)) == 2:
                        break
                    if _raspisanie["Преподаватель"][need_teacher_dict[_id]]["Пары"][str(item)]["Группа"] == "" and _raspisanie["Группа"][str(para["Группа"])]["Пары"][str(item)]["Преподаватель"] == "":
                        for k in rooms[para["Тип аудитории"]]:
                            if _raspisanie["Кабинет"][k]["Пары"][str(item)]["Преподаватель"] == "":
                                #Записываем данные если преподаватель свободен, группа свободна и аудитория свободна
                                _raspisanie["Преподаватель"][need_teacher_dict[_id]]["Пары"][str(item)]["Группа"] = para["Группа"]
                                _raspisanie["Преподаватель"][need_teacher_dict[_id]]["Пары"][str(item)]["Дисциплина"] = para["Дисциплина"]
                                _raspisanie["Преподаватель"][need_teacher_dict[_id]]["Пары"][str(item)]["Аудитория"] = k
                                _raspisanie["Группа"][str(para["Группа"])]["Пары"][str(item)]["Преподаватель"] = i
                                _raspisanie["Группа"][str(para["Группа"])]["Пары"][str(item)]["Дисциплина"] = para["Дисциплина"]
                                _raspisanie["Группа"][str(para["Группа"])]["Пары"][str(item)]["Аудитория"] = k
                                _raspisanie["Кабинет"][k]["Пары"][str(item)]["Преподаватель"] = i
                                _raspisanie["Кабинет"][k]["Пары"][str(item)]["Дисциплина"] = para["Дисциплина"]
                                _count_lessons[_id] += 1
                                anti_povtor.append(para["Группа"])
                                print(anti_povtor)
                                break
            except:
                c += 1

        #print(_raspisanie)

    _ras[list_days_for_generate[jitem]] = _raspisanie
#Запись в бд

try:
    con = sql.connect('db.sqlite3')
    cur = con.cursor()
    for i in _ras:
        try:
            _sql = "INSERT INTO all_raspisanie (date,json) VALUES ( '{}' , '{}' )".format(i,dumps(_ras[i], ensure_ascii=False))
            cur.execute(_sql)
        except:
            _sql = "UPDATE all_raspisanie SET json = '{}' where date = '{}'".format(dumps(_ras[i], ensure_ascii=False),i)
            cur.execute(_sql)
except:
    print("Ошибка при добавлении данных")
    print(e)

finally:
    con.commit()
    con.close()

print(True)
