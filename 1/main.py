import tkinter as tk
from random import randint as random

window = tk.Tk()

entry_input = tk.Entry(
width=25)
entry_input.pack()
entry_output = tk.Entry(
width=25)
entry_output.pack()

_alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
_alph_reverse = _alph[::-1]

print(_alph_reverse)
print(_alph)

def push():
    entry_output.delete(0)
    text = entry_input.get()

    _text = ''

    for i in text:
        _text += _alph_reverse[_alph.index(i)]

    entry_output.insert(0, _text)

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
