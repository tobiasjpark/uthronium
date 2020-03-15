def makeit():
    print('ASKING FOR NUMBERS')
    a = simpledialog.askfloat("Part 1", "Type in Part 1.")
    b = simpledialog.askfloat("Part 2", "Type in Part 2.")
    c = simpledialog.askfloat("Part 3", "Type in Part 3.")
    d = simpledialog.askfloat("Part 4", "Type in Part 4.")
    e = simpledialog.askfloat("Part 5", "Type in Part 5.")
    f = simpledialog.askfloat("Part 6", "Type in Part 6.")
    g = simpledialog.askfloat("Part 7", "Type in Part 7.")
    h = simpledialog.askfloat("Part 8", "Type in Part 8.")
    i = simpledialog.askfloat("Part 9", "Type in Part 9.")
    j = simpledialog.askfloat("Part 10", "Type in Part 10.")
    k = simpledialog.askfloat("Part 11", "Type in Part 11.")
    l = simpledialog.askfloat("Part 12", "Type in Part 12.")
    print('DECRYPTING VALUES')
    #6 = f 5 = e
    a = a + f
    a = a / e
    a = a - f
    print('PART 1 DECRYPTED ')
    b = b + f
    b = b / e
    b = b - f
    print('PART 2 DECRYPTED ')
    c = c + f
    c = c / e
    c = c - f
    print('PART 3 DECRYPTED ')
    f = f * 10
    d = d + 1
    d = d * f
    d = d - 1
    f = f / 10
    print('PART 4 DECRYPTED ')
    print('SKIPPING PARTS 5, 6,')
    g = g / e
    print('PART 7 DECRYPTED ')
    h = h + f
    h = h / e
    h = h - f
    print('PART 8 DECRYPTED ')
    i = i + f
    i = i / e
    i = i - f
    print('PART 9 DECRYPTED ')
    j = j + f
    j = j / e
    j = j - f
    print('PART 10 DECRYPTED ')
    k = k * e
    print('PART 11 DECRYPTED ')
    l = l + f
    l = l / e
    l = l - f
    print('PART 12 DECRYPTED ')
    print('VERIFYING NUMBERS ')
    if c != l:
        messagebox.showerror("Verification Failed", "The numbers you entered did not correctly form a uThrone kingdom.")
        ex()
    if a != k:
        messagebox.showerror("Verification Failed", "The numbers you entered did not correctly form a uThrone kingdom.")
        ex()
    print('CONVERTING PART 1 ')
    if a == 0 or a == 10:
        message('Default Throne Room')
        z = randint(1, 6)
        y = str('tr') + str(z)
        details[y] = 'y'
    elif a == 1 or a == 6:
        details["tr1"] == 'y'
    elif a == 2 or a == 7:
        details["tr2"] == 'y'
    elif a == 3 or a == 8:
        details["tr3"] == 'y'
    elif a == 4 or a == 9:
        details["tr4"] == 'y'
    if a > 5:
        details["money"] = 1000000000
        message('Murphy\'s Voice')
    print('PART 1 CONVERTED. VALUE IS %s' % a)
    print('CONVERTING PART 2')
    if b == 1:
        pass
        
def itmake():
    pass
def message(x):
    messagebox.showinfo("Message", "Your uThronium number parts include %s, which is no longer supported. You have been compensated with money for your loss." % x)
from tkinter import *
from tkinter import messagebox
from sys import exit as ex
root = Tk()
canvas = Canvas(root, width=1, height=1)
canvas.pack()
root.title("uThronium Kingdom Converter - uThrone/uThronium Backwards Compatability")
a = Button(root, text="uThrone Number Parts to .utr File", command=makeit)
a.pack()
b = Button(root, text=".utr File to uThrone Number Parts", command=itmake)
b.pack()
details = {
"money" : 0,
"lives" : 1,
"user" : None,
"time" : None,
"tr0" : False,
"tr1" : False,
"tr2" : False,
"tr3" : False,
"tr4" : False,
"tr5" : False,
"tr6" : False,
"person" : False,
"f1" : False,
"f2" : False,
"f3" : False,
"kill1" : False,
"kill2" : False,
"pass" : None,
"colorpass" : None,
"new" : False
}
mainloop()
