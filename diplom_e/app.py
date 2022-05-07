from flask import Flask, request
import irbis
import json

app = Flask(__name__)

try:
    client = irbis.Connection()
    client.parse_connection_string('host=172.27.176.1;port=6666;' +
    'database=RDR;user=1;password=1;')
    client.connect()

    client_b = irbis.Connection()
    client_b.parse_connection_string('host=172.27.176.1;port=6666;' +
    'database=IBIS;user=1;password=1;')
    client_b.connect()

except Exception as E:
    print('error connection')


def search_one_people_books(client,family):
    return_dict = {}
    found = client.search('"A={}$"'.format(family))
    for item in found:
        records = client.read_records(item) #Все подходящии люди
        for jitem in records:   #jitem - совпадение по запросу фамилии (одинаковая часть фамилии)
            _f_name = jitem.fm(10) #фамилия
            _s_name = jitem.fm(11) #имя
            _t_name = jitem.fm(12) #отчество
            _jitem = str(jitem).split("\n")
            name = "{} {} {}".format(_f_name,_s_name,_t_name)
            _list_books = []
            for zitem in _jitem: #перебор всех записей по человеку
                if zitem.startswith("40"):  #перебор всех взятых книг по человеку
                    _zitem = zitem.split("^")
                    _book = {"book_name": "None", "date_take": "None", "date_return": "None"}
                    for i in _zitem:
                        if i.startswith("c"):
                            _book["book_name"] = i[1:]
                        if i.startswith("d"):
                            _i = i[1:]
                            _new_data = "{}{}.{}{}.{}{}{}{}".format(_i[6],_i[7],_i[4],_i[5],_i[0],_i[1],_i[2],_i[3])
                            _book["date_take"] = _new_data
                        if i.startswith("e"):
                            _i = i[1:]
                            _new_data = "{}{}.{}{}.{}{}{}{}".format(_i[6],_i[7],_i[4],_i[5],_i[0],_i[1],_i[2],_i[3])
                            _book["date_return"] = _new_data
                    _list_books.append(_book)
        if len(_list_books) > 0:
            return_dict[name] = _list_books
    return return_dict


def search_one_people(client,family):
    return_dict = {}
    found = client.search('"A={}$"'.format(family))
    for item in found:
        records = client.read_records(item) #Все подходящии люди
        for jitem in records:   #jitem - совпадение по запросу фамилии (одинаковая часть фамилии)
            _f_name = jitem.fm(10) #фамилия
            _s_name = jitem.fm(11) #имя
            _t_name = jitem.fm(12) #отчество
            _adress = (str(jitem.fm(13,"a")) if str(jitem.fm(13,"a")) != "None" else "")+" "+(str(jitem.fm(13,"b")) if str(jitem.fm(13,"b"))
            != "None" else "")+" "+(str(jitem.fm(13,"c")) if str(jitem.fm(13,"c")) != "None" else "")+" "+(str(jitem.fm(13,"d")) if str(jitem.fm(13,"d"))
            != "None" else "")+" "+(str(jitem.fm(13,"e")) if str(jitem.fm(13,"e")) != "None" else "")+" "+(str(jitem.fm(13,"f")) if str(jitem.fm(13,"f"))
            != "None" else "")+" "+(str(jitem.fm(13,"g")) if str(jitem.fm(13,"g")) != "None" else "")+" "+(str(jitem.fm(13,"h")) if str(jitem.fm(13,"h")) != "None" else "")
            _adress = _adress.replace("  "," ")
            _adress = _adress.replace("  "," ")
            _telephone = jitem.fm(17)
            _group = jitem.fm(90, "a")
            _group_number = jitem.fm(90, "e")
            name = "{} {} {}".format(_f_name,_s_name,_t_name)
        return_dict[name] = [_adress,_telephone,_group,_group_number]
    return return_dict

def create_user(client,family,name,otchestvo,address,telephone,group_a,group_e):
    record = irbis.Record()
    try:
        _adress = address.split("!")
        _stroka_adressa = "^a{}^b{}^c{}^d{}^e{}^f{}^g{}".format(_adress[0],_adress[1],_adress[2],_adress[3],_adress[4],_adress[5],_adress[6])
        record.add(13, _stroka_adressa)
    except:
        pass
    record.add(10, family)
    record.add(11, name)
    record.add(12, otchestvo)
    record.add(17, telephone)
    record.add(90, "^a{}^e{}".format(group_a,group_e))
    print(group_e)
    print(record)
    client.write_record(record)

def create_book(client,name_book,author,year,izdatel,isbn):
    record = irbis.Record()
    _name_book = name_book.split("!")
    _name_book = " ".join(_name_book)
    _author = author.split("!")
    record.add(200, "^a{}".format(_name_book))
    record.add(700, "^a{}^b{}".format(_author[0],_author[1]))
    record.add(210, "^d{}".format(year))
    record.add(210, "^c{}".format(izdatel))
    record.add(10, "^a{}".format(isbn))
    client.write_record(record)


@app.route('/check_book')  # Данные о книгах, которые взяты пользователями
def get_books():
    last_name = request.args.get("last_name")
    _json = json.dumps(search_one_people_books(client, last_name),
                                        sort_keys=False,
                                        indent=4,
                                        ensure_ascii=False)
    return _json

@app.route('/check_user')
def get_users(): #    - Данные о пользователях
    last_name = request.args.get("last_name")
    _json = json.dumps(search_one_people(client, last_name),
                                        sort_keys=False,
                                        indent=4,
                                        ensure_ascii=False)
    return _json

@app.route('/new_user')  #client,family,name,otchestvo,address,telephone,group_a,group_e
def new_users(): #    - Новый о пользователях
    family = request.args.get("family")
    name = request.args.get("name")
    otchestvo = request.args.get("otchestvo")
    address = request.args.get("address")
    telephone = request.args.get("telephone")
    group_a = request.args.get("group_a")
    group_e = request.args.get("group_e")
    try:
        create_user(client,family,name,otchestvo,address,telephone,group_a,group_e)
        return "new user create"
    except:
        return "Error, coda ne bydet"

@app.route('/new_boks')
def new_boks(): #    - Новый книга
    name_book = request.args.get("name_book")
    author = request.args.get("author")
    year = request.args.get("year")
    izdatel = request.args.get("izdatel")
    isbn = request.args.get("isbn")
    create_book(client_b,name_book,author,year,izdatel,isbn)
    return "new_boks"






if __name__ == '__main__':
    app.run()
