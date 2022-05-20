import sqlite3 as sql
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from closed import kety #token

#Инициализиурем словарь команд
def commands_init():
    _c = {}
    try:
        con = sql.connect("db.db")
        cur = con.cursor()
        cur.execute("SELECT * from answers")
        _z = cur.fetchall()
        for i in _z:
            _c[i[1]] = i[2]
    except:
        print("Ошибка бд")
    finally:
        con.close()

    return _c

def update(id, table, new_text):
    _ex = 0
    try:
        con = sql.connect("db.db")
        cur = con.cursor()
        _sql = "UPDATE {} set answer = '{}' where command = '{}'".format(str(table), str(new_text), str(id))
        cur.execute(str(_sql))
        con.commit()
    except:
        _ex = 1
        raise
        print("Ошибка бд")
    finally:
        con.close()
        if _ex == 1:
            return False
        else:
            return True

commands = commands_init()
print(commands)

bot = Bot(token=kety)
dp = Dispatcher(bot)

async def on_startup(_):
    print("bot start")

'''*************************************Клавиатура***********************'''

buttons = []
for i in commands:
    buttons.append(KeyboardButton(i))

kb_client_main = ReplyKeyboardMarkup(resize_keyboard = True)
kb_client_fak = ReplyKeyboardMarkup(resize_keyboard = True)

kb_client_main.row(buttons[0],buttons[1],buttons[2]).row(buttons[3],buttons[4],buttons[5]).row(buttons[6],buttons[7],buttons[8]).add(buttons[15])
kb_client_fak.row(buttons[9],buttons[10]).row(buttons[11],buttons[12]).row(buttons[13],buttons[14])


'''*************************************КЛИЕНТ***********************'''

text = """/info - Информация о нашем ВУЗе
/openday - День открытых дверей
/course - Курсы для абитуриентов
/specialties - Направления подготовки
/guide - Как подать документы на поступление онлайн
/contacts - Контактная информация
/direction - Узнай на какую специальность ты проходишь
/studorganizations - Внеучебная деятельность
/excursion - Интерактивная экскурсия по университету"""

text_admin = """UPDATE {команда} {Таблица} {Новый текст}
Таблицы: answers

"""
#3 нижних и 2 феми
_exams = {"ru": [40,
            "Педагогическое образование / Физическая культура и спорт",
            "Педагогическое образование / Безопасность жизнедеятельности",
            "Педагогическое образование (с двумя профилями подготовки) / Безопасность жизнедеятельности и дополнительное образование в области туризма",
            "Педагогическое образование / Информатика",
            "Педагогическое образование (с двумя профилями подготовки) / Биология и экология"],
          "mat": [39,
            "Педагогическое образование / Информатика",
            "Педагогическое образование (с двумя профилями подготовки) / Биология и экология"],
          "ob": [42,
            "Педагогическое образование (с двумя профилями подготовки) / Биология и экология",
            "Педагогическое образование / Информатика",
            "Педагогическое образование / Физическая культура и спорт",
            "Педагогическое образование / Безопасность жизнедеятельности",
            "Педагогическое образование (с двумя профилями подготовки) / Безопасность жизнедеятельности и дополнительное образование в области туризма",
            ],
          "fiz": [36,
            "Педагогическое образование (с двумя профилями подготовки) / Биология и экология",
            "Педагогическое образование / Информатика"],
          "pff": [40,
          "Педагогическое образование / Физическая культура и спорт"],
          "pfb": [40,
          "Педагогическое образование / Безопасность жизнедеятельности",
          "Педагогическое образование (с двумя профилями подготовки) / Безопасность жизнедеятельности и дополнительное образование в области туризма"]
         }

_people = {}

text_calc = """Для того чтобы посчитать возможные направления введите свои результаты экзаменов в виде, каждый отдельным сообщением
КОД_ЭКЗАМЕНА БАЛЛ
Коды экзаменов:
ru - русский язык
is - история
fiz - физика
geo - география
bio - биология
ob - обществознание
mat - математика
ins - иностранный язык
lit - литератруа
en - Профессиональное испытание (Английский язык)
inf - Информатика и ИКТ
tv - Творческое испытание (Рисунок и композиция)
pff - Профессиональное испытание (Сдача норматива по гимнастике)
pfo - Профессиональное испытание (Общество и экономика
pfb - Профессиональное испытание (Безопасность жизнедеятельности)
"""

@dp.message_handler(commands=['start','help'])
async def command_start(message: types.Message):
    await message.answer(text, reply_markup=kb_client_main)


@dp.message_handler(commands=['admin',])
async def command_start(message: types.Message):
    await message.answer(text_admin, reply_markup=kb_client_main)


@dp.message_handler()
async def exco_send(message: types.Message):
    _msg = message.text
    if _msg in commands:
        if _msg == '/specialties':
            await message.answer(commands[_msg], reply_markup=kb_client_fak)
        elif _msg == '/calc':
            try:
                if len(_people[message.from_user.id]) == 3:
                    _list = []
                    _r_list = []
                    for i in _people[message.from_user.id]:
                        _list += _exams[i]
                    print(_list)
                    for i in _list:
                        if (_list.count(i) > 2):
                            if i not in _r_list:
                                _r_list.append(i)
                    if _r_list:
                        _txt = "Вам подходят следующие специальности: \n\n" + '\n\n'.join(_r_list)
                        await message.answer(_txt, reply_markup=kb_client_main)
                    else:
                        await message.answer('Вам ничего не подходит', reply_markup=kb_client_main)


                else:
                    print(len(_people[message.from_user.id]))
                    await message.answer('Вам нужно ввести 3 экзамена', reply_markup=kb_client_main)
            except:
                _people[message.from_user.id] = {}
                await message.answer(text_calc, reply_markup=kb_client_main)
        else:
            await message.answer(commands[_msg], reply_markup=kb_client_main)
    else:
        if _msg.split(" ")[0].upper() == "UPDATE":
            if message.from_user.id == 5336707481:
                a = _msg.split(" ")
                _r = update(str(a[1]),str(a[2])," ".join(a[3:]))
                if _r:
                    commands[str(a[1])] = " ".join(a[3:])
                    await message.answer("Успешно")
                else:
                    await message.answer("Не Успешно")
            else:
                await message.answer("Низя")
        elif _msg.split(" ")[0].lower() in _exams:
            try:
                if int(_msg.split(" ")[1]) < _exams[_msg.split(" ")[0].lower()][0]:
                    await message.answer("У вас слишком маленький балл за этот экзамен")
                else:
                    _people[message.from_user.id][_msg.split(" ")[0].lower()] = int(_msg.split(" ")[1])
                    print(_people)
                    print(len(_people[message.from_user.id]))
                    await message.answer("Данные записаны\nПродолжайте вводить\nПосле внесения 3х результатов вы можете повторить команду /calc")
            except:
                _people[message.from_user.id] = {}
        else:
            await message.answer(text)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
