import tkinter as tk
from random import randint as random

window = tk.Tk()

entry_input = tk.Entry(
width=25)
entry_input.pack()
entry_output = tk.Entry(
width=25)
entry_output.pack()

def push():
    entry_output.delete(0)
    text = entry_input.get()

    _text = []
    for item in text:
        if item not in _text:
            _text.append(item)  #собираем алфавит
    _len = len(text) #получаем длину алфавита для деления

    _random_list = []
    for i in range(_len): #генерим гамму - рандомим
        _random_list.append(random(0,_len))

    _modul_list = []
    for i in range(_len): #считаем значение по модулю
        _modul_list.append((_text.index(text[i])+1+_random_list[i])%_len)

    _output_text = ''
    for i in range(_len): #шифруем со значениями по модулю
        _output_text += text[_modul_list[i]]


    entry_output.insert(0, _output_text)



button = tk.Button(
    text="Зашифровать",
    width=25,
    height=5,
    bg="white",
    fg="black",
    command=push
)
button.pack()

window.mainloop()
