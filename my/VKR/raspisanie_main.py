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
    _now_time = strftime('%d %m',gmtime(time())).split(' ')
    _day_now = int(_now_time[0])
    _month_now = int(_now_time[1])
    list_days_for_generate = []
    for item in _days:
        _month = int(item[1].split('-')[1])
        _day = int(item[1].split('-')[2])
        if _month >= _month_now:
            if _day > _day_now:
                list_days_for_generate.append(item[1])

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
    for i in _t:
        _sql = "SELECT name FROM all_group WHERE id = {}".format(i)
        _z = con.execute(_sql).fetchall()
        _name = _z[0][0]
        works_group[_name] = {"Предметы": []}
        _sql = "Select prepod_id, subject, hours, hours_end, room_id from all_work where (group_id = {}) and (hours > hours_end)".format(i)
        _z = con.execute(_sql).fetchall()
        for item in _z:
            _sql = "SELECT name from all_personal WHERE id = {}".format(item[0])
            _p = con.execute(_sql).fetchall()
            works_group[_name]["Предметы"].append({"Дисциплина": item[1], "Преподаватель": _p[0][0], "Часов осталось": item[2]-item[3], "Подходящий тип аудиторий": item[4]})

    #print(works_group) #Получили словарь групп у которых есть пары
    #Заполняем словари групп

except:
    print("Ошибка при извлечении данных")
    print(e)
finally:
    con.close()


#### функция которая рандомит результаты
def random_generate(_list):
    _end_list = []
    _sum = sum(_list)
    _new_list = []
    for i in _list:
        _new_list.append(i*100//_sum)
    for i in range(4):
        _z = random(0,sum(_new_list))
        _c = _new_list[0]
        for item in range(len(_new_list)):
            if _z <= _c:
                _end_list.append(item)
                break
            else:
                _c += _new_list[item+1]
    return _end_list
    #Добавить проверку на превышение пар





def create_for_group_one_day(_dict):
    _z = []
    for item in _dict:
        #print(item)
        _z.append(item["Часов осталось"])

    _x = random_generate(_z)
    _r = []
    for i in _x:
        _r.append(_dict[i])
    return _r





################Формируем расписание
raspisanie = {}
for item in list_days_for_generate:
    raspisanie[str(item)] = []
    for j in works_group:
        raspisanie[str(item)].append(create_for_group_one_day(works_group[j]["Предметы"]))
#print(raspisanie)

#Запись в бд
try:
    con = sql.connect('db.sqlite3')
    cur = con.cursor()
    for i in raspisanie:
        try:
            _sql = "INSERT INTO all_raspisanie (date,json) VALUES ( '{}' , '{}' )".format(i,dumps(raspisanie[i]))
            print(_sql)
            cur.execute(_sql)
        except:
            _sql = "UPDATE all_raspisanie SET json = '{}' where date = '{}'".format(dumps(raspisanie[i]),i)
            cur.execute(_sql)
except:
    print("Ошибка при добавлении данных")
    print(e)

finally:
    con.commit()
    con.close()
