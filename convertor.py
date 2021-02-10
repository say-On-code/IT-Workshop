#sayan chaudhuri roll=13
import tkinter as tk
from tkinter import *
from functools import partial
root = tk.Tk()
root.title('Temperature convertor')
root.geometry('500x300')
var = tk.StringVar()
numberInput = tk.StringVar()
def call_convert(rlabel1, inputn):
    tem = inputn.get()
    if var.get() == 'A':
        f = float((float(tem) * 9 / 5) + 32)
        k = float((float(tem) + 273.15))
        rlabel1.config(text="%f Fahrenheit" % f)
    if var.get() == 'B':
        c = float((float(tem) - 32) * 5 / 9)
        k = c + 273
        rlabel1.config(text="%f Celsius" % c)
    return
frame = Frame(root)
r1 = tk.Radiobutton(root, text='Celsius to Fahrenheit', variable=var, value='A', command=call_convert)
r1.pack()
r2 = tk.Radiobutton(root, text='Fahrenheit to Celsius', variable=var, value='B', command=call_convert)
r2.pack()
input_label = tk.Label(root,  width=20, text='enter temp',bg='Black',fg='yellow')
input_entry = tk.Entry(root, textvariable=numberInput,bg='yellow')
input_label.pack()
input_entry.pack()
result_label1 = tk.Label(root, bg='yellow', width=20)
result_label1.pack()
call_convert = partial(call_convert, result_label1, numberInput)
Button(root, text='convert',width=10,bg='Black',fg='yellow',command=call_convert).pack()
root.mainloop()
