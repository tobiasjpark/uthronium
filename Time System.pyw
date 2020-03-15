def start():
    global x
    x = int(time())
def end():
    global x
    x = time() - x
    x = x / 60
    int(x)
    global y
    y = int(y - x)
    message.showinfo("Total Time in Minutes Spent", x)
    message.showinfo("Total Time Left", y)
def read():
    global y
    y = data.askinteger("How Much Did You Read?", "How many minutes did you obtain by reading?")
    message.showinfo("Total Time Left", "You have %s minutes left!" % y)
def p():
    message.showinfo("Minutes Left", y)
from tkinter import messagebox as message
from tkinter import simpledialog as data
from tkinter import Tk as screen
from tkinter import Button as button
from time import time, asctime
window = screen()
a = button(window, text="I Read a Book", command=read)
d = button(window, text="How Much Time Left?", command=p)
if asctime()[0] != 'Sun':
    b = button(window, text="I Am Doing Computer/Games/TV", command=start)
    c = button(window, text="I Am Finsihed Doing Computer/Games/TV", command=end)
window.title("Time System")
a.pack()
if asctime()[0] != 'Sun':
    b.pack()
    c.pack()
d.pack()
