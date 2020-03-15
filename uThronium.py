import subprocess
from traceback import format_exc
from getpass import getuser
import turtle
from os import makedirs, execl, remove
from time import asctime, sleep, localtime, time
from random import randint, shuffle
from tkinter import *
from tkinter import messagebox, filedialog, simpledialog
from tkinter.filedialog import askopenfilename
import sys
import os.path
from platform import uname
import pickle
import urllib.request, urllib.error, urllib.parse
import os
import random

def voice(x):
    speak(x)  
def speak(val):
    if details["tr0"] == True:
        if debug["os"] == True:
            user = "C:\\Documents and settings\\all users\\Documents\\uthronium\\"  
        else:   
            user = "C:\\users\\public\\Documents\\uthronium\\"
        number = random.randint(1, 17)
        deb = open(str(user) + str("speak" + str(number) + ".vbs"), 'w')
        deb.write('''
On Error Resume Next
Dim Message, Speak
Set Speak=CreateObject("sapi.spvoice")
Speak.Rate = 2
Speak.Speak "''' + val + '''"
WaitUntilDone(-1)
''')
        deb.close()
        subprocess.Popen([str(user) + str("speak" + str(number) + ".vbs")], shell=True, creationflags=subprocess.SW_HIDE)
def restart():
    canvas.destroy()
    root.destroy()
    python = sys.executable
    os.execl(python, python, * sys.argv)
def will():
    try:
        if details["money"] > 0:
            x = messagebox.askyesno("Leave a Will?", "You have died. Would you like to go back in time and leave a will?")
            if x and confirm() == True:
                x = simpledialog.askinteger("How Many People?", "How many kingdom's will you include in your will?")
                for y in range(0, x):
                    messagebox.showinfo("Money Remaining", "You have %s dollars left to give." % details["money"])
                    z = simpledialog.askfloat("How Much to Who?", str("How much money would you like to donate to the ") + str(y + 1) + str('st kingdom?'))
                    if z > details["money"]:
                        x = messagebox.askretrycancel("Transaction Failed", "That transaction failed. Please try again.")
                    if debug["os"] == True:
                        initit = "C:\\Documents and settings\\all users\\Documents\\uthronium\\"
                    else:
                        initit = "C:\\users\\public\\Documents\\uthronium\\"
                    if uname()[0] == 'Linux' or uname()[0] == 'Darwin':
                        user = getuser()
                        initit = str('/home/') + str(user) + str('/Public/uthronium/')
                    file = filedialog.askopenfilename(filetypes=(("uThronium Kingdoms", ".utr"),), initialdir=initit)
                    print(file)
                    ds = file
                    fil = open(file, 'rb')
                    file1 = pickle.load(fil)
                    file2 = open(ds, 'wb')
                    file1["money"] = file1["money"] + z
                    pickle.dump(file1, file2)
                    fil.close()
                    z = z * -1
                    mone(z)
    except Exception:
        er(format_exc())
class password_input:
    def __init__(self, x):
        if x == True:
            try:
                self.go = True
                self.win = Toplevel()
                self.win.title("Enter Password")
                #win.resizable(0, 0)
                self.window = Canvas(self.win, width=300, height=100)
                self.window.pack()
                w = 300
                h = 100
                ws = self.win.winfo_screenwidth()
                hs = self.win.winfo_screenheight()
                x = (ws/2) - (w/2)
                y = (hs/2) - (h/2) - 32
                self.win.geometry('%dx%d+%d+%d' % (w, h, x, y))
                self.win.resizable(0, 0)
                self.window.create_rectangle(0, 20, 300, 50, fill='white', outline='black')
                self.window.bind_all('<KeyPress>', self.password)
                self.m = ""
                self.n = 0
                self.x = self.window.create_text(10, 40, text=self.m, font=('Belwe Cn BT', 20), fill='black', anchor=W)
                a = Button(self.win, text="OK", command=self.go2, padx=50)
                a.place(relx=.05, rely=.75, anchor=W)
                b = Button(self.win, text="Cancel", command=self.reset, padx=50)
                b.place(relx=.95, rely=.75, anchor=E)
            except Exception:
                er(format_exc())
    def password(self, key):
        if self.go:
            try:
                letter = key.char
                #status('pass')
                bac = key.keysym
                key = bac
                if len(bac) > 1:
                    if bac == 'BackSpace':
                        if self.n > 0:
                            self.m = back(self.m)
                            self.n = self.n - 1
                            t = '*' * self.n
                            self.window.itemconfig(self.x, text=t, font=('Belwe Cn BT', 20), fill='black', anchor=W)
                    elif bac == 'space':
                        self.m = self.m + ' '
                        self.n = self.n + 1
                        t = '*' * self.n
                        self.window.itemconfig(self.x, text=t, font=('Belwe Cn BT', 20), fill='black', anchor=W)
                    elif bac == 'Return':
                        self.go2()
                        return None
                    elif letter == '`':
                        key = '`'
                    elif letter == '~':
                        key = '~'
                    elif letter == '!':
                        key = '!'
                    elif letter == '@':
                        key = '@'
                    elif letter == '#':
                        key = '#'
                    elif letter == '$':
                        key = '$'
                    elif letter == '%':
                        key = '%'
                    elif letter == '^':
                        key = '^'
                    elif letter == '&':
                        key = '&'
                    elif letter == '*':
                        key = '*'
                    elif letter == '(':
                        key = '('
                    elif letter == ')':
                        key = ')'
                    elif letter == '-':
                        key = '-'
                    elif letter == '_':
                        key = '_'
                    elif letter == '=':
                        key = '='
                    elif letter == '+':
                        key = '+'
                    elif letter == '[':
                        key = '['
                    elif letter == ']':
                        key = ']'
                    elif letter == '{':
                        key = '{'
                    elif letter == '}':
                        key = '}'
                    elif letter == '\\':
                        key = '\\'
                    elif letter == '|':
                        key = '|'
                    elif letter == ':':
                        key = ':'
                    elif letter == ';':
                        key = ';'
                    elif letter == '"':
                        key = '"'
                    elif letter == "'":
                        key = "'"
                    elif letter == '<':
                        key = '<'
                    #CONTINUE PROGRAMMING SYMBOLS INTO THIS FUNCTION
                else:
                    self.m = self.m + key
                    self.n = self.n + 1
                    t = '*' * self.n
                    self.window.itemconfig(self.x, text=t, font=('Belwe Cn BT', 20), fill='black', anchor=W)
            except Exception:
                er(format_exc())
    def go2(self):
        if self.go:
            x = self.m
            self.window.destroy()
            self.win.destroy()
            self.go = False
            if x == details["pass"]:
                drawroom()
                speak("Welcome back! Here are the latest updates on your kingdom: " + details["News"])
            else:
                y = messagebox.askretrycancel("Wrong Password", "Incorrect password. Try again?.")
                if y == True:
                    password_input(True)
                else:
                    resetdetail()
                    status('n')
            return None
    def reset(self):
        resetdetail()
        self.window.destroy()
        self.win.destroy()
        self.go = False
        status('n')
def back(x):
    if x != '':
        y = len(x)
        y = y - 1
        a = ""
        for z in range(0, y):
            a = a + x[z]
        return a
def sprint(x):
    return None;
def logged():
    if details["user"] != None:
        return True
    else:
        return False
def closewin():
    x = True
    if x == True:
        if details["user"] != None:
            temp['shutdown'] = True
            exit_save()
        root.destroy()

class wargame1():
    def __init__(self):
        try:
            status('wargame1')
            statusbar('War Mode 1')
            
            messagebox.showinfo("Instructions", "Use the right and left arrow keys on your keyboard to steel your black airplane. Try to avoid going near the red force-field equipped missiles.")

            messagebox.showinfo("Instructions", "When you press Ok, this intro will close, and the game will load. If the arrow keys don't work, try clicking the game window.")
            end = False
            self.forward = True
            self.right = False
            self.left = False
            self.down = False
            turtle.setup(640, 480)
            self.window = turtle.Screen()
            turtle.write("Loading Game. Please Wait!", align=CENTER, font=('Belwe Cn BT', 36))
            setup = turtle.Turtle()
            setup.up()
            setup.speed(0)
            setup.forward(320)
            setup.left(90)
            setup.down()
            setup.forward(245)
            setup.left(90)
            setup.forward(645)
            setup.left(90)
            setup.forward(485)
            setup.left(90)
            setup.forward(645)
            setup.left(90)
            setup.forward(245)
            setup.color('darkgreen')
            self.window.title("War Mode 1")
            a = turtle.Turtle()
            b = turtle.Turtle()
            c = turtle.Turtle()
            d = turtle.Turtle()
            e = turtle.Turtle()
            f = turtle.Turtle()
            g = turtle.Turtle()
            h = turtle.Turtle()
            i = turtle.Turtle()
            j = turtle.Turtle()
            k = turtle.Turtle()
            l = turtle.Turtle()
            m = turtle.Turtle()
            n = turtle.Turtle()
            o = turtle.Turtle()
            p = turtle.Turtle()
            q = turtle.Turtle()
            r = turtle.Turtle()
            s = turtle.Turtle()
            self.ship = turtle.Turtle()
            self.ship.shape('triangle')
            turtlelist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's']
            for y in turtlelist:
                exec(str(y) + str('.color("red")'))
                exec(str(y) + str('.speed(0)'))
                exec(str(y) + str('.shape(\'classic\')'))
                exec(str(y) + str('.up()'))
                exec(str(y) + str('.left(90)'))
                exec(str(y) + str('.forward(220)'))
                exec(str(y) + str('.left(90)'))
                exec(str(y) + str('.forward(320)'))
                exec(str(y) + str('.right(180)'))
                x = randint(0, 640)
                z = randint(0, 240)
                exec(str(y) + str('.forward(x)'))
                exec(str(y) + str('.right(90)'))
                exec(str(y) + str('.forward(z)'))
            self.ship.speed(0)
            self.ship.up()
            self.ship.right(90)
            self.ship.forward(240)
            self.ship.right(180)
            self.ship.forward(30)
            turtle.clear()
            self.window.bgcolor('darkgreen')
            self.window.onkey(self.shipright1, "Right")
            self.window.onkey(self.shipleft1, "Left")
            me = turtle.Turtle()
            me.color('darkgreen')
            self.window.listen()
            t = time()
            xy = time()
            force = 25
            speed = 10
            while 1:
                if time() - xy >= 3 and speed < 25:
                    speed = speed + 1
                    xy = time()
                    sprint(speed)
                if end == False:
                    self.ship.forward(speed)
                    for y in turtlelist:
                       exec(str(y) + str('.forward(speed)'))
                       if touching(self.ship.pos(), n.pos(), force) or touching(self.ship.pos(), o.pos(), force) or touching(self.ship.pos(), p.pos(), force) or touching(self.ship.pos(), q.pos(), force) or touching(self.ship.pos(), r.pos(), force) or touching(self.ship.pos(), s.pos(), force) or touching(self.ship.pos(), a.pos(), force) or touching(self.ship.pos(), b.pos(), force) or touching(self.ship.pos(), c.pos(), force) or touching(self.ship.pos(), d.pos(), force) or touching(self.ship.pos(), e.pos(), force) or touching(self.ship.pos(), f.pos(), force) or touching(self.ship.pos(), g.pos(), force) or touching(self.ship.pos(), h.pos(), force) or touching(self.ship.pos(), i.pos(), force) or touching(self.ship.pos(), j.pos(), force) or touching(self.ship.pos(), k.pos(), force) or touching(self.ship.pos(), l.pos(), force) or touching(self.ship.pos(), m.pos(), force): 
                            s = turtle.Turtle()
                            s.color('darkgreen')
                            s.up()
                            s.speed(0)
                            s.right(90)
                            x = wargameval
                            s.setx(x[0])
                            s.sety(x[1])
                            s.color('blue')
                            self.ship.color('blue')
                            end = True
                            t = time() - t
                            t = int(t)
                            turtle.write("Game Over! Your score is %s" % t, align=CENTER, font=('Belwe Cn BT', 36))
                            return None
                if falling(a):
                    a.sety(240.99999999999997)
                    a.setx(randint(-320, 320))
                if falling(b):
                    b.sety(240.99999999999997)
                    b.setx(randint(-320, 320))
                if falling(c):
                    c.sety(240.99999999999997)
                    c.setx(randint(-320, 320))
                if falling(d):
                    d.sety(240.99999999999997)
                    d.setx(randint(-320, 320))
                if falling(e):
                    e.sety(240.99999999999997)
                    e.setx(randint(-320, 320))
                if falling(f):
                    f.sety(240.99999999999997)
                    f.setx(randint(-320, 320))
                if falling(g):
                    g.sety(240.99999999999997)
                    g.setx(randint(-320, 320))
                if falling(h):
                    h.sety(240.99999999999997)
                    h.setx(randint(-320, 320))
                if falling(i):
                    i.sety(240.99999999999997)
                    i.setx(randint(-320, 320))
                if falling(j):
                    j.sety(240.99999999999997)
                    j.setx(randint(-320, 320))
                if falling(k):
                    k.sety(240.99999999999997)
                    k.setx(randint(-320, 320))
                if falling(l):
                    l.sety(240.99999999999997)
                    l.setx(randint(-320, 320))
                if falling(m):
                    m.sety(240.99999999999997)
                    m.setx(randint(-320, 320))
                if falling(n):
                    n.sety(240.99999999999997)
                    n.setx(randint(-320, 320))
                if falling(o):
                    o.sety(240.99999999999997)
                    o.setx(randint(-320, 320))
                if falling(p):
                    p.sety(240.99999999999997)
                    p.setx(randint(-320, 320))
                if falling(q):
                    q.sety(240.99999999999997)
                    q.setx(randint(-320, 320))
                if falling(r):
                    r.sety(240.99999999999997)
                    r.setx(randint(-320, 320))
                if falling(s):
                    s.sety(240.99999999999997)
                    s.setx(randint(-320, 320))
                if self.ship.pos()[0] > 320 and self.ship.heading() == 0:
                    self.ship.setx(-320.99999999999997)
                if self.ship.pos()[0] < -320 and self.ship.heading() == 180:
                    self.ship.setx(320.99999999999997)
                if self.ship.pos()[1] > 240 and self.ship.heading() == 90:
                    self.ship.sety(-240.99999999999997) 
        except:
            print(format_exc())
            #pass
    def shipright1(self):
        try:
            self.ship.right(90)
            if self.ship.heading() == 270:
                self.ship.left(90)
        except Exception:
            er(format_exc())
    def shipleft1(self):
        try:
            self.ship.left(90)
            if self.ship.heading() == 270:
                self.ship.right(90)
        except Exception:
            er(format_exc())

def touching(a, b, r):
    try:
        global wargameval
        x1 = a[0]
        y1 = a[1]
        x2 = b[0]
        y2 = b[1]
        x1 = x1 / r
        y1 = y1 / r
        x2 = x2 / r
        y2 = y2 / r
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        if x1 == x2 and y1 == y2:
            wargameval = b
            return True
        else:
            return False
    except Exception:
        er(format_exc())
def falling(c):
    try:
        a = c.pos()
        b = c.heading()
        if b == 270:
            x = a[1]
            x = abs(x)
            if x % 1 == 0:
                return True
            else:
                return False
    except Exception:
        er(format_exc())
def er(y):
    global heythere
    try:
        a = debug
        b = details
        c = temp
        d = heythere
    except:
        messagebox.showerror("Error", "The following error occurred during startup: " + y)
        sys.exit()
    a = None
    b = None
    c = None
    d = None
    if uname()[0] == 'Linux' or uname()[0] == 'Darwin':
        user = getuser()
        user = str('/home/') + str(user) + str('/Public/uthronium/')
    else:
        if debug["os"] == True:
            user = "C:\\Documents and settings\\all users\\Documents\\uthronium\\"
        else:
            user = "C:\\users\\public\\Documents\\uthronium\\"
    if debug["status"] == "cheat.enter":
        messagebox.showerror("Error", "Cheat code not found.")
        cheat()
    elif debug["status"] == 'exsave':
        pass
    elif debug["status"] == "m17.help":
        messagebox.showerror("Error", "You did not enter anything!")
        Casey(17)
    elif heythere >= 2:
        messagebox.showerror("CRITICAL ERROR", "A CRITICAL ERROR HAS OCCURED. PLEASE SEND DATA ON WHAT YOU WERE DOING TO THE CORRECT PERSONS!")
        sys.exit()
    elif debug["status"] == 'exsave222':
        heythere = heythere + 1
        statusbar("A fatal error has occurred")
        colorpass = details["colorpass"]
        pas = details["pass"]
        details["colorpass"] = "Not included in this report"
        details["pass"] = "Not included in this report"
        dev = open(str(user) + str("debug.txt"))
        devr = str(user) + str("debug.txt")
        dev = dev.read()
        deb = open(str(user) + str("debug.txt"), 'w')
        deb.write(dev)
        deb.write('''
''')
        deb.write(str(asctime()))
        deb.write('''
''')
        deb.write(y)
        deb.write('''
''')
        deb.write('An error has been encountered. See above information.')
        s = getuser()
        x = messagebox.showerror("Error", "Sorry %s, but something's gone wrong in here (also known as ERROR). Technical info for nerds: %s" % (s, y))
        deb.close()
        sprint(x)
        details["pass"] = pas
        details["colorpass"] = colorpass
        if details["user"] != None:
            try:
                exit_save2()
            except:
                pass
        #messagebox.showinfo("Cleaning Up", "Ok %s, we're going to reset uThronium's brain so that you can continue playing! Your kingdom file will be saved with the autosave feature (your original kingdom will not be saved). When you press OK, uThronium will close for about 2 seconds, we will reset the brain, and then it should come back up." % getuser())
        exit_save2()
        restart()
    else:
        heythere = heythere + 1
        statusbar("A fatal error has occurred")
        colorpass = details["colorpass"]
        pas = details["pass"]
        details["colorpass"] = "Not included in this report"
        details["pass"] = "Not included in this report"
        dev = open(str(user) + str("debug.txt"))
        devr = str(user) + str("debug.txt")
        dev = dev.read()
        deb = open(str(user) + str("debug.txt"), 'w')
        deb.write(dev)
        deb.write('''
''')
        deb.write(str(asctime()))
        deb.write('''
''')
        deb.write(y)
        deb.write('''
''')
        deb.write('An error has been encountered. See above information.')
        s = getuser()
        x = messagebox.showerror("Error", "Sorry %s, but something's gone wrong in here (also known as ERROR). uThronium will now restart. Technical info for nerds: %s" % (s, y))
        deb.close()
        sprint(x)
        details["pass"] = pas
        details["colorpass"] = colorpass
        if details["user"] != None:
            try:
                exit_save2()
            except:
                pass
        #messagebox.showinfo("Cleaning Up", "Ok %s, we're going to reset uThronium's brain so that you can continue playing! Your kingdom file will be saved with the autosave feature (your original kingdom will not be saved). When you press OK, uThronium will close for about 2 seconds, we will reset the brain, and then it should come back up." % getuser())
        restart()
def setup():
    

    global setu
    setu = True
    
    try:
        if uname()[0] != 'Linux' and uname()[0] != 'Windows' and uname()[0] != 'Darwin':
            messagebox.showerror("Operating System Not Supported", "uThronium can only be run on Windows, Mac, and Linux. Your operating system is %s." % uname()[0])
            setu = False
        sprint('YEAAAAAAAAA')
        if uname()[4] == 'AMD64':
            debug["bit"] = False
        else:
            debug["bit"] = True
        if uname()[2] == 'xp' or uname()[2] == 'Xp' or uname()[2] == 'XP':
            debug["os"] = True
        else:
            debug["os"] = False
    except Exception:
        er(format_exc())
    try:
        if debug["os"] == True:
            me = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\debug.txt")
            messagebox.showinfo('wrong1', 'wrong1')
        else:
            me = open("C:\\users\\public\\Documents\\uthronium\\debug.txt")
    except:
        setup2()
    
        
def setup2():
    
    if uname()[0] != 'Linux' and uname()[0] != 'Darwin':
        try:
            
            global hold
            hold = '''if debug["bit"] == True:
                z = 'C:\\program files\\uthronium\\'
            else:
                z = 'C:\\program files (x86)\\uthronium\\'
            exec(str('y = open(') + str(z) + str('protect.dat)'))
            y = y.read()'''
            if debug["os"] == True:
                makedirs("C:\\Documents and settings\\all users\\Documents\\uthronium")
                
                makedirs("C:\\Documents and settings\\all users\\Documents\\uthronium\\temp")
                me2 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\debug.txt", 'w')
                me3 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak1.vbs", 'w')
                me4 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak2.vbs", 'w')
                me5 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak3.vbs", 'w')
                me6 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak4.vbs", 'w')
                me7 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak5.vbs", 'w')
                me8 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak6.vbs", 'w')
                me9 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak7.vbs", 'w')
                me10 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak8.vbs", 'w')
                me41 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak9.vbs", 'w')
                me51 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak10.vbs", 'w')
                me61 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak11.vbs", 'w')
                me71 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak12.vbs", 'w')
                me81 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak13.vbs", 'w')
                me91 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak14.vbs", 'w')
                me31 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak15.vbs", 'w')
                me42 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak16.vbs", 'w')
                me52 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak17.vbs", 'w')
            else:
                
                makedirs("C:\\users\\public\\Documents\\uthronium")
                makedirs("C:\\users\\public\\Documents\\uthronium\\temp")
                me2 = open("C:\\users\\public\\Documents\\uthronium\\debug.txt", 'w')
                me3 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak1.vbs", 'w')
                me4 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak2.vbs", 'w')
                me5 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak3.vbs", 'w')
                me6 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak4.vbs", 'w')
                me7 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak5.vbs", 'w')
                me8 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak6.vbs", 'w')
                me9 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak7.vbs", 'w')
                me10 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak8.vbs", 'w')
                me41 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak9.vbs", 'w')
                me51 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak10.vbs", 'w')
                me61 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak11.vbs", 'w')
                me71 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak12.vbs", 'w')
                me81 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak13.vbs", 'w')
                me91 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak14.vbs", 'w')
                me31 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak15.vbs", 'w')
                me42 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak16.vbs", 'w')
                me52 = open("C:\\Documents and settings\\all users\\Documents\\uthronium\\speak17.vbs", 'w')
            me2.close()
            me3.close()
            me4.close()
            me5.close()
            me6.close()
            me7.close()
            me8.close()
            me9.close()
            me42.close()
            me52.close()
            me10.close()
            me31.close()
            me41.close()
            me51.close()
            me61.close()
            me71.close()
            me81.close()
            me91.close()
        except Exception:
            
            System.out.println('help')
    else:
        status('setup2')
        makedirs(str('/home/') + str(getuser()) + str('/Public/uthronium'))
        makedirs(str('/home/') + str(getuser()) + str('/Public/uthronium/temp'))
        me2 = open(str('/home/') + str(getuser()) + str('/Public/uthronium/debug.txt'), 'w')
        me2 = open(str('/home/') + str(getuser()) + str('/Public/uthronium/speak.txt'), 'w')
        me2.close()
        me3.close()
def goagain():
    try:
        a = open("C:\Documents and Settings\All Users\Documents\\debug.txt")
        return a
    except Exception:
        er(format_exc())
def scramble(x):
    try:
        a = ''
        if 1 == 2:
            pass
        else:
            y = len(x)
            sprint(y)
            for z in range(0, y):
                if x[z] == 'a':
                    a = a + 't'
                elif x[z] == 'b':
                    a = a + '0'
                elif x[z] == 'c':
                    a = a + 'a'
                elif x[z] == 'd':
                    a = a + 'c'
                elif x[z] == 'e':
                    a = a + 'd'
                elif x[z] == 'f':
                    a = a + 'x'
                elif x[z] == 'g':
                    a = a + 'u'
                elif x[z] == 'h':
                    a = a + 's'
                elif x[z] == 'i':
                    a = a + 'j'
                elif x[z] == 'j':
                    a = a + 'r'
                elif x[z] == 'k':
                    a = a + 'n'
                elif x[z] == 'l':
                    a = a + 'b'
                elif x[z] == 'm':
                    a = a + 'z'
                elif x[z] == 'n':
                    a = a + 'k'
                elif x[z] == 'o':
                    a = a + 'm'
                elif x[z] == 'p':
                    a = a + 'i'
                elif x[z] == 'q':
                    a = a + 'l'
                elif x[z] == 'r':
                    a = a + 'q'
                elif x[z] == 's':
                    a = a + 'o'
                elif x[z] == 't':
                    a = a + 'v'
                elif x[z] == 'u':
                    a = a + 'e'
                elif x[z] == 'v':
                    a = a + 'h'
                elif x[z] == 'w':
                    a = a + 'f'
                elif x[z] == 'x':
                    a = a + 'w'
                elif x[z] == 'y':
                    a = a + 'y'
                elif x[z] == 'z':
                    a = a + 'g'
                elif x[z] == 'A':
                    a = a + 'T'
                elif x[z] == 'B':
                    a = a + ')'
                elif x[z] == 'C':
                    a = a + 'A'
                elif x[z] == 'D':
                    a = a + 'C'
                elif x[z] == 'E':
                    a = a + 'D'
                elif x[z] == 'F':
                    a = a + 'X'
                elif x[z] == 'G':
                    a = a + 'U'
                elif x[z] == 'H':
                    a = a + 'S'
                elif x[z] == 'I':
                    a = a + 'J'
                elif x[z] == 'J':
                    a = a + 'R'
                elif x[z] == 'K':
                    a = a + 'N'
                elif x[z] == 'L':
                    a = a + 'B'
                elif x[z] == 'M':
                    a = a + 'Z'
                elif x[z] == 'N':
                    a = a + 'K'
                elif x[z] == 'O':
                    a = a + 'M'
                elif x[z] == 'P':
                    a = a + 'I'
                elif x[z] == 'Q':
                    a = a + 'L'
                elif x[z] == 'R':
                    a = a + 'Q'
                elif x[z] == 'S':
                    a = a + 'O'
                elif x[z] == 'T':
                    a = a + 'V'
                elif x[z] == 'U':
                    a = a + 'E'
                elif x[z] == 'V':
                    a = a + 'H'
                elif x[z] == 'W':
                    a = a + 'F'
                elif x[z] == 'X':
                    a = a + 'W'
                elif x[z] == 'Y':
                    a = a + 'Y'
                elif x[z] == 'Z':
                    a = a + 'G'
                elif x[z] == ' ':
                    a = a + '2'
                elif x[z] == '0':
                    a = a + ' '
                elif x[z] == '1':
                    a = a + '('
                elif x[z] == '2':
                    a = a + '*'
                elif x[z] == '3':
                    a = a + '&'
                elif x[z] == '4':
                    a = a + '^'
                elif x[z] == '5':
                    a = a + '%'
                elif x[z] == '6':
                    a = a + '$'
                elif x[z] == '7':
                    a = a + '#'
                elif x[z] == '8':
                    a = a + '@'
                elif x[z] == '9':
                    a = a + '!'
                elif x[z] == ' ':
                    a = a + '/'
                else:
                    a = a + x[z]
            return a
    except:
        return x
def singleLine(x):
    x = x.splitlines()
    z = ''
    a = 0
    for y in x:
        a = a + 1
        if a != 1:
            z = z + str(' ') + y
        else:
            z = z + y
    return z
def mone(x):
    if debug["status"] == 'pass' or debug["status"] == 'colorpass':
        print('stat')
        return None
    try:
        statusbar('Processing Money Transaction')
        sprint(str('Transaction: Add ') + str(x))
        details["money"] = x + details["money"]
        sprint(details["money"])
        drawroomt(None)
        debt()
        autosave(None)
    except Exception:
        er(format_exc())
def unscramble(x):
    try:
        a = ''
        if 1 == 1:
            y = len(x)
            for z in range(0, y):
                if x[z] == 't':
                    a = a + 'a'
                elif x[z] == '/':
                    a = a + ' '
                elif x[z] == '0':
                    a = a + 'b'
                elif x[z] == 'a':
                    a = a + 'c'
                elif x[z] == 'c':
                    a = a + 'd'
                elif x[z] == 'd':
                    a = a + 'e'
                elif x[z] == 'x':
                    a = a + 'f'
                elif x[z] == 'u':
                    a = a + 'g'
                elif x[z] == 's':
                    a = a + 'h'
                elif x[z] == 'j':
                    a = a + 'i'
                elif x[z] == 'r':
                    a = a + 'j'
                elif x[z] == 'n':
                    a = a + 'k'
                elif x[z] == 'b':
                    a = a + 'l'
                elif x[z] == 'z':
                    a = a + 'm'
                elif x[z] == 'k':
                    a = a + 'n'
                elif x[z] == 'm':
                    a = a + 'o'
                elif x[z] == 'i':
                    a = a + 'p'
                elif x[z] == 'l':
                    a = a + 'q'
                elif x[z] == 'q':
                    a = a + 'r'
                elif x[z] == 'o':
                    a = a + 's'
                elif x[z] == 'v':
                    a = a + 't'
                elif x[z] == 'e':
                    a = a + 'u'
                elif x[z] == 'h':
                    a = a + 'v'
                elif x[z] == 'f':
                    a = a + 'w'
                elif x[z] == 'w':
                    a = a + 'x'
                elif x[z] == 'y':
                    a = a + 'y'
                elif x[z] == 'g':
                    a = a + 'z'
                elif x[z] == 'T':
                    a = a + 'A'
                elif x[z] == ')':
                    a = a + 'B'
                elif x[z] == 'A':
                    a = a + 'C'
                elif x[z] == 'C':
                    a = a + 'D'
                elif x[z] == 'D':
                    a = a + 'E'
                elif x[z] == 'X':
                    a = a + 'F'
                elif x[z] == 'U':
                    a = a + 'G'
                elif x[z] == 'S':
                    a = a + 'H'
                elif x[z] == 'J':
                    a = a + 'I'
                elif x[z] == 'R':
                    a = a + 'J'
                elif x[z] == 'N':
                    a = a + 'K'
                elif x[z] == 'B':
                    a = a + 'L'
                elif x[z] == 'Z':
                    a = a + 'M'
                elif x[z] == 'K':
                    a = a + 'N'
                elif x[z] == 'M':
                    a = a + 'O'
                elif x[z] == 'I':
                    a = a + 'P'
                elif x[z] == 'L':
                    a = a + 'Q'
                elif x[z] == 'Q':
                    a = a + 'R'
                elif x[z] == 'O':
                    a = a + 'S'
                elif x[z] == 'V':
                    a = a + 'T'
                elif x[z] == 'E':
                    a = a + 'U'
                elif x[z] == 'H':
                    a = a + 'V'
                elif x[z] == 'F':
                    a = a + 'W'
                elif x[z] == 'W':
                    a = a + 'X'
                elif x[z] == 'Y':
                    a = a + 'Y'
                elif x[z] == 'G':
                    a = a + 'Z'
                elif x[z] == ' ':
                    a = a + '0'
                elif x[z] == '(':
                    a = a + '1'
                elif x[z] == '*':
                    a = a + '2'
                elif x[z] == '&':
                    a = a + '3'
                elif x[z] == '^':
                    a = a + '4'
                elif x[z] == '%':
                    a = a + '5'
                elif x[z] == '$':
                    a = a + '6'
                elif x[z] == '#':
                    a = a + '7'
                elif x[z] == '@':
                    a = a + '8'
                elif x[z] == '!':
                    a = a + '9'
                elif x[z] == '2':
                    a = a + ' '
                else:
                    a = a + x[z]
            return a
    except:
        return x
def statusbar(x):
    try:
        autosave(None)
        sprint(str('Status Bar is now:') + x)
        statusb.config(text=x)
        statusb.pack(side=BOTTOM, fill=X)
    except Exception:
        er(format_exc())
def status(x):
    try:
        debug["status"] = x
    except Exception:
        er(format_exc())
def statmurph(x):
    statusbar(str('What\'s Up, Casey? #') + str(x))
def Casey(x):
    if debug["status"] == 'color':
        messagebox.showerror("ENTER PASSWORD", "ENTER YOUR PASSWORD FIRST!")
    try:
        abcd = False
        if debug["status"] == 'colorpass':
            abcd = True
        if details["user"] == None or abcd == True:
            messagebox.showerror("Account Required", "An account is required for this feature.")
        else:
            money = details["money"]
            if x == False:
                x = randint(1, 64)
                #sprint(x)
            me = details["murph"]
            if me == x:
                Casey(False)
                return None
            else:
                details["murph"] = x
            if details["money"] == 0:
                x = 64
            statmurph(x)
            if x == 63:
                Casey_yesno("The roads around your country are in very bad shape. Instead of looking like roads with some potholes, they look more like potholes with some road!!! Would you like to pave new roads?", -10000000, "The new roads cost 10 million dollars to pave.", False, -20000, "OK. But your citizens are very unhappy about this. Many of them have left the country in anger, and we have lost $20,000 in tax money.", False)

            elif x == 1:
                Casey_yesno("The country of Fiji has declared war on you! They want 100 miles of land. Would you just like to give it to them? If not, we must go to war.", 10000000000, "You have saved the country from war. Fiji is giving you 10 billion for the land.", True, -10000000000, "You have asked for war. This war will be expensive. You must pay 10b.", False)
            elif x == 2:
                if money < 0:
                    Casey_yesno("The country is in debt and the poor are hungry. Would you like to donate 10 thousand dollars to the food pantry?", -10000, "Congratulations. You are helping the poor. However, you have more debt.", False, 0, "Pershaps its good you didn't indulge in more debt. But the people are still hungry.", False)
                else:
                    Casey(3)
            elif x == 3:
                speak("The police have just caught the developer of a major computer virus. However, the suspect is your cousin! Would you like to capture him anyway?")
                y = messagebox.askyesno("What's Up, Casey?", "The police have just caught the developer of a major computer virus. However, the suspect is your cousin! Would you like to capture him anyway?")
                if y == True:
                    mone(-300)
                    speak("The people are happy now because the cousin is in jail. But your family is angry! They have stolen 300 dollars from you!")
                    messagebox.showwarning("What's Up, Casey?", "The people are happy now because the cousin is in jail. But your family is angry! They have stolen 300 dollars from you!")
                else:
                    speak("Your family is happy because your cousin is free. But the people are furious! Some of them received the virus and their computers are now destroyed. They have hired an assasain to kill you! Would you like to place your bodyguards on high alert?")
                    y = messagebox.askyesno("What's Up, Muprhy?", "Your family is happy because your cousin is free. But the people are furious! Some of them received the virus and their computers are now destroyed. They have hired an assasain to kill you! Would you like to place your bodyguards on high alert?")
                    if y == True:
                        speak("Good choice. Your bodyguards have killed the assasain and it doesn't look like more are coming.")
                        messagebox.showinfo("What's Up, Casey?", "Good choice. Your bodyguards have killed the assasain and it doesn't look like more are coming.")
                    else:
                        details["kill1"] = True
                        speak("Very well. But your life is now in danger!")
                        messagebox.showwarning("What's Up, Muprhy?", "Very well. But your life is now in danger!")
            elif x == 4:
                Casey_info("The people have sent a gift to express their gratitude towards you as Ruler. The gift is 75 thousand dollars!", 75000, True)
            elif x == 5:
                Casey_yesno("There is a fire in the palace! Your stuff is burning up. However, the chef responsible will soon have the fire out. Would you like to activate the sprinklers anyway?", -10000, "The fire is put out. Unfortunately, the sprinkler system destroyed ten thousand dollars!", False, -20000, "Yay! The chef put the fire out. However, some of the fire spread to the money vault, which is next to the kitchen. Twenty thousand dollars were burned!", False)
            elif x == 6:
                speak("It is the end of the year, and I want a bonus. May I have it?")
                me = messagebox.askyesno("What's Up, Casey?", "It is the end of the year, and I want a bonus. May I have it?")
                if me == False:
                    speak("very well, sir")
                    messagebox.showinfo("What's Up, Casey?", "Very well, sir.")
                elif me == True:
                    speak("How much is my bonus?")
                    me2 = simpledialog.askfloat("What's Up, Casey?", "How much is my bonus?")
                    me2 = int(me2)
                    if me2 < 0:
                        speak("Hey, you can't do that!")
                        messagebox.showwarning("What's Up, Casey?", "Sorry King, it doesn't work that way!")
                    else:
                        details["money"] = details["money"] - me2
                        speak("Thank you, sir")
                        messagebox.showinfo("What's Up, Casey?", "Thank you, sir!")
            elif x == 7:
                Casey_info("Your uncle, Joe Smith, has died. In his will, he left 200 thousand dollars to you!", 200000, True)
            elif x == 8:
                Casey_yesno("A storm is going to strike your palace. Would you like to buy a generator for the throne room?", -2000, "The generator will be expensive. You must pay 2 thousand dollars.", False, 0, "Good news, you saved money by not buying a generator. Bad news, the power's out!", False)
            elif x == 9:
                Casey_yesno("You have received a gift of 1 million dollars from Germany. Would you like to invest it in the stock market? If not, I will put it in the vault.", 2000000, "The stock market is in your favor. Your 1 million turned into 2 million!", True, 1000000, "Ok. Your money is being added to the vault.", True)
            elif x == 10:
                Casey_yesno("The day is gloomy and the people are bored. Would you like to set up the county fair today?", -5000, "It cost 5 thousand dollars to set up the county fair.", False, 200, "Well, it is gloomy today anyway. But some of the kids are disappointed. They've vandalized your palace. Repairs cost 200 dollars.", False)
            elif x == 11:
                Casey_yesno("A major malware program has taken the internet offline! (hard to believe). The malware has a suicide chain which will destroy itself in a week. Would you like to hire Bill Gates and friends to repair the internet anyway?", -3000000000, "Bill Gates and Microsoft TM are charging 3 billion dollars for repairing the internet.", False, -2000000, "Well, you will save a lot of money this way. However, the people are very upset. They are threatening you with lawsuits! Your royal court is asking for 2 million dollars to appease them.", False)
            elif x == 12:
                Casey_yesno("A TV producer has offered to make a commercial advertising your country. Will you accept?", 5000000, "The commercial is a large success! You have made 5 million dollars!", True, 0, "Oh, man! The company offered California the commercial and they've made 5 million dollars!", False)
            elif x == 13:
                Casey_info("A submarine crew has discovered a 400 year old pirate ship! You have received some of the booty.", 1000000, True)
            elif x == 14:
                speak("Your palace's carbon manoxide alarm has broken! Would you like to fix it?")
                y = messagebox.askyesno("What's Up, Casey?", "Your palace's carbon manoxide alarm has broken! Would you like to fix it?")
                if y == True:
                    details["money"] = details["money"] - 500
                    speak("Good choice! However, the systems cost 500 dollars.")
                    messagebox.showwarning("What's Up, Casey?", "Good choice! However, the systems cost 500 dollars.")
                elif y == False:
                    details["kill1"] = True
                    speak("Well, if you say so. But without an alarm, we will not know if there is a carbon manoxide leak, which would kill us.")
                    messagebox.showwarning("What's Up, Casey?", "Well, if you say so. But without an alarm, we will not know if there is a carbon manoxide leak, which would kill us.")
            elif x == 15:
                Casey_yesno("The main computer system in the palace has crashed. You could replace the system...it's old, anyway. If not you can repair the computer system. So would you like to replace it?", -15000, "Good choice. However, the new system cost 15 thousand dollars!", False, -700, "Ok. The computer repair man is charging 700 dollars. He says royal computers \"take more time\".", False)
            elif x == 16:
                Casey_yesno("It is Easter today. Would you like to go to church?", -200, "Good choice. However, the cost of your security will be 200 dollars.", False, -700, "The Pope isn't very happy about this. He has started a riot outside your palace! Police have stopped it, but you now owe them 700 dollars.", False)
            elif x == 17:
                speak('''
You have just won a war with Mexico! You are
entitled to some money. However, if you ask for too much money, Mexico might get angry and go back to war. 
How much would you like to take from Mexico?''')
                y = simpledialog.askfloat("What's Up, Casey?", '''
You have just won a war with Mexico! You are
entitled to some money. However, if you ask for too much money, Mexico might get angry and go back to war. 
How much would you like to take from Mexico?''')
                status("m17.help")
                if y > random.randint(100000, 100000000000):
                    speak("Mexico does not agree. The war is back on!")
                    messagebox.showwarning("What's Up, Casey?", "Mexico does not agree. The war is back on!")
                elif y < 0:
                    speak("Sorry, but you can't give Mexico negative dollars")
                    messagebox.showerror("Hey!", "Why on earth did you do that? You're supposed to take money, not give money!")
                    Casey(17)
                else:
                    mone(y)
                    speak("Mexico agrees. The money is being added to your vault.")
                    messagebox.showinfo("What's Up, Casey?", "Mexico agrees. The money is being added to your vault.")
            elif x == 18:
                Casey_info("A project you invested in has gone bankrupt. You have lost 200 thousand dollars.", -200000, False)
            elif x == 19:
                Casey_info("We are out of apple juice.", 0, True)
            elif x == 20:
                Casey_info("Not really much going on right now.", 0, True)
            elif x == 21:
                Casey_info("Zzz...Zzz...Zzz...", 0, True)
            elif x == 22:
                Casey_yesno("The USA wants to make a deal with you. They will give you 3 billion dollars if you advertise their product on TV. Will you accept?", 3000000000, "Good choice. The 3 billion dollars will be added to your vault.", True, 0, "Well, I don't see why you did that, but ok.]]]Well, I don't see why you did that, but ok.", True)
            elif x == 23:
                Casey_yesno("The President of the United States wants you to help them pay off their debt. Will you give them $500,000?", -500000, "Ok.", True, -10000000000, "The President is not happy about this. He has cancelled our trade deal with America, and we have lost 10 billion dollars.", True)
            elif x == 24:
                Casey_yesno("A movie company wants to make a movie about you. Do you accept?", 5000000, "You have received a share of the profits of the movie. Specifically, you have received 5 million dollars!", True, 0, "Well, the film crews would be a bother anyway. And they'd probably stretch the truth.", True)
            elif x == 25:
                speak('''
It is time to collect monthly taxes in one of your
cities. The population of this city is 25, 000. (Not to be confused with the population of your country).
How much would you like to charge each citizen?''')
                y = simpledialog.askfloat("What's Up, Casey?", '''
It is time to collect monthly taxes in one of your
cities. The population of this city is 25, 000. (Not to be confused with the population of your country).
How much would you like to charge each citizen?''')
                if y > 500:
                    speak("The people are angry at you for charging so high a tax! They are revolting! They have broken into your palace and stolen half of your money!")
                    messagebox.showwarning("What's Up, Casey?", "The people are angry at you for charging so high a tax! They are revolting! They have broken into your palace and stolen half of your money!")
                    details["money"] = details["money"] / 2
                else:
                    mone(y * 25000)
                    speak('ok')
                    messagebox.showinfo("What's Up, Casey?", "Ok.")
            elif x == 26:
                Casey_yesno("A hurricane is coming! Would you like to evacuate part of the country?", -1000000, "Good choice. However, this cost 1 million dollars.", False, -3000000, "The hurricane caused a lot of damage. Repairs cost 3 million dollars.", False)
            elif x == 27:
                speak("There is a flood in the streets and the water is in your palace! You can run out of the palace. Or, swim out of the palace. Would you like to run out?")
                y = messagebox.askyesno("What's Up, Casey?", "There is a flood in the streets and the water is in your palace! You can run out of the palace. Or, swim out of the palace. Would you like to run out?")
                if y == True:
                    mone(-200000000)
                    speak("Good choice! However, your palace was damaged. Repairs cost 200 million dollars.")
                    messagebox.showwarning("What's Up, Casey?", "Good choice! However, your palace was damaged. Repairs cost 200 million dollars.")
                elif y == False:
                    speak("The waters have swept you away! You have been hit by debris! You die unless you have another life.")
                    messagebox.showwarning("What's Up, Casey?", "The waters have swept you away! You have been hit by debris! You die unless you have another life.")
                    exit_save_death()
            elif x == 28:
                Casey_yesno("A virus has been found on your computer system. Would you like to remove it?", -100, "This is a complex virus. Removal will cost 100 dollars.", False, -15000, "The virus destroyed your system! A new one cost 15 thousand dollars.", False)
            elif x == 29:
                Casey_yesno("We haven't had a royal party in a while. Would you like a royal party?", -2000, "The royal party cost 2 thousand dollars to set up.", False, 0, "Ok.", True)
            elif x == 30:
                Casey_yesno("The plumbing department went on strike! They want 40 thousand dollars! Will you give it to them?", -40000, "Good choice.", True, -1000000, "Ok. But without plumbing, your pipes have run dry and must be replaced. New pipes cost 1 million dollars.", True)
            elif x == 31:
                speak("There is a plague spreading throughout your kingdom. Would you like to build more hospitals?")
                y = messagebox.askyesno("What's Up, Casey?", "There is a plague spreading throughout your kingdom. Would you like to build more hospitals?")
                if y == True:
                    mone(-10000000)
                    speak("Very good. However, this cost 10 million dollars.")
                    messagebox.showwarning("What's Up, Casey?", "Very good. However, this cost 10 million dollars.")
                else:
                    z = randint(0, 101)
                    if z < 51:
                        speak("The people are very angry about all of this! You must flee the country for a while.")
                        messagebox.showwarnning("What's Up, Casey?", "The people are very angry about all of this! You must flee the country for a while.")
                        exit_save2()
                    else:
                        mone(-50000000)
                        speak("OH NO! YOU HAVE CAUGHT THE PLAGUE! You are being rushed to a hospital in the United States since all the hospitals in your kingdom our full. This cost 50 million dollars!")

                        messagebox.showwarning("What's Up, Casey?", "OH NO! YOU HAVE CAUGHT THE PLAGUE! You are being rushed to a hospital in the United States since all the hospitals in your kingdom our full. This cost 50 million dollars!")
            elif x == 32:
                Casey_3opt('''Budget Alert - We're spending more money than
we're making! At this rate we'll soon be in
debt. Option 1: Raise taxes in the small towns
(their taxes are cheap). Option 2: Reduce spending
on transportation systems. Option 3: Do nothing at
all! Type 1, 2, or 3.''', -2000, "Good choice. However, some townspeople are unhappy and have started a revolt by burning picures of you! This is highly illegal, and they must be arrested. Your police have demanded 2 thousand dollars.", False, -1000, "Ok. However, there is now more traffic around town. Which means more accidents! Old traffic lights are being upgraded. These cost 1 thousand dollars.", False, -1000000000, "Oh boy! We're losing money rappidly! In fac, we've lost 1 billion dollars!", False)
            elif x == 33:
                Casey_info("Today is National Bacon Egg And Cheese Sandwhich Day in your kingdom! Have a sandwhich, king. Have a sandwhich.", 0, True)
            elif x == 34:
                Casey_info("Hey King! Just thought I'd let you know that...I QUIT! APRIL FOOLS!!", 0, True)
            elif x == 35:
                Casey_yesno("There is someone at the door of your palace. He is wearing a ski mask. I don't blame him...it's cold out there. Then again, he could be an assassin! Would you like to let him in?", -20000000, "OH NO! HE'S BROKEN INTO THE VAULT! HE'S STOLEN 20 MILLION DOLLARS!", False, 0, "Good choice.", True)
            elif x == 36:
                Casey_yesno("You have no more waffles and bacon. And that was your only breakfast. Would you like to buy more?", -30, "You have bought your waffles and bacon. But, your freezer is so full that we can't fit them in! And your breakfast cost 30 dollars!", False, 0, "You may do as you wish. But your stomach is so angry that you just threw up!", False)
            elif x == 37:
                Casey_yesno("A nuclear reactor power plant in your kingdom is suffering a meltdown! You can keep it running anyway. But would you like to shut it down?", -650000, "Good choice. However, we need a new power plant to keep up with energy demand. This will cost 650 thousand dollars.", False, -1000000000, "OH NO! THE REACTOR IS LEAKING! YOUR KINGDOM IS EXPOSED TO RADIATION! You must evacuate part of your country and close off the infected area, which will cost 1 billion dollars!", False)
            elif x == 38:
                voice("There is much pollution in your kingdom. Would you like to plant more trees?")
                y = messagebox.askyesno("What's Up, Casey?", "There is much pollution in your kingdom. Would you like to plant more trees?")
                if y == True:
                    voice('''How many trees would you like to plant? Each tree costs 100 dollars.''')
                    z = simpledialog.askfloat("What's Up, Casey?", '''How many trees would you like to plant?
Each tree costs 100 dollars.''')
                    if z < 0:
                        voice("You cannot chop down trees!")
                        messagebox.showerror("What's Up, Casey?", "You cannot chop down trees!")
                    else:
                        z = z * 100
                        z2 = z
                        z = z * -1
                        mone(z)
                        voice("Ok. The trees have been planted. It cost %s dollars.")
                        messagebox.showinfo("What's Up, Casey?", "Ok. The trees have been planted. It cost %s dollars." % z2)
                else:
                    voice("OK. But the air is getting (gulp) hard to (gulp) breathe! (gulp)")
                    messagebox.showwarning("What's Up, Casey?", "OK. But the air is getting (gulp) hard to (gulp) breathe! (gulp)")
            elif x == 39:
                Casey_info("Your kingdom has been named as having the lowest number of government scandals! This is a big honor.", 0, True)
            elif x == 40:
                Casey_yesno("Si, writer of \"Namgang Style\", has offered an invitation to visit him. Will you accept?", -400, "Ok. But your security cost 400 bucks.", False, 0, "Uh-oh. Si is not happy about this. He has written a song making fun of the way your fingernail looks pink.", False)
            elif x == 41:
                Casey_yesno("You have been invited to host a weekly talk show on a famous radio station. Do you accept?", 1000000, "Ok. Because of this talk show, many people found out about your country and have come to visit. You have made 1 million dollars.", True, 0, "Ok. You're busy this week anyway...we have to negotiate that treaty with the Canadians about claims to the Bering Sea.", True)
            elif x == 42:
                Casey_3opt('''Garbage is in abundant
supply in your kingdom,
but there's not enough
systems to dispose of it!
Option 1: Dig a landfill.
Option 2: Ship it to our
neighbors. Option 3: Turn
it into electricity. Type
1, 2 or 3.''', -100000, "Ok. It cost 100 thousand dollars to dig up a landfill.", True, -50000, "Ok. Some garbage has been removed. However, this cost 50 thousand dollars.", False, -75000, "Cool! However, the power plant cost 75 thousand dollars to set up.", False)
            elif x == 43:
                Casey_info("It's a slow day, king. The only exciting thing going on around here is listening to the advisor advise the 2nd advisor who's advising the 1st advisor.", 0, True)
            elif x == 44:
                Casey_yesno("You are going to the United Nations Annual Conference next month. Would you like to learn a foreign language so you can understand what is being said?", -500, "Ok. But your curriculum cost 500 dollars.", False, 0, "Ok. Here, take this \"Goggle Translate\" app instead.", True)
            elif x == 45:
                Casey_yesno("Your snoring at night is keeping everyone in the palace awake. You can give everybody else earplugs. Or would you like to buy an anti-snore device?", -50, "Ok. This cost 50 bucks.", True, -110, "Alright. This cost 110 dollars.", True)
            elif x == 46:
                Casey_3opt('''Your palace's power
plant is on its last
legs. You must replace
it with: Option 1: Coal
power plant. Option 2:
Oil power plant. Option
3: Solar power plant. T
ype 1 2 or 3.''', -10000, "This plant only cost 10 thousand dollars and is very efficient moneywise. But there is a lot of polution (cough cough).", False, -20000, "Well, this cost 20 thousand dollars. But pollution isn't that bad.", False, -15000, "This plant's cost is in between the other's 15 thousand. And no pollution at all! Good choice.", True)
            elif x == 47:
                Casey_yesno("Spies we sent to a secret military base have disappeared. You can send more, or send the navy to blast them out. Would you like to send more?", -1000000, "It cost one million dollars to send more spies.", False, -1200000, "It cost 1 million dollars to send the navy...and their mission failed! The navy officer is very angry, and has went on strike! You must pay 200 thousand to get him back.", False)
            elif x == 48:
                status('m48')
                statmurph(48)
                voice("You're ruling this kingdom extremely well! There are protesters everywhere - protesting against people who hate you! They've rewarded you with a gift - a new throne room (room 3)! Do you accept?")
                y = messagebox.askyesno("What's Up, Casey?", "You're ruling this kingdom extremely well! There are protesters everywhere - protesting against people who hate you! They've rewarded you with a gift - a new throne room (room 3)! Do you accept?")
                if y == True:
                    drawtr023(3)
                    voice("You have been moved into your new throne room!")
                    messagebox.showinfo("What's Up, Casey?", "You have been moved into your new throne room!")
                else:
                    voice("OK")
                    messagebox.showinfo("What's Up, Casey?", "Ok.")
            elif x == 49:
                voice("The people love you! They want to thank you for the wonderful job you're doing. But they don't have a lot of money, so they sent you some picture frames (frame 3). Do you accept?")
                y = messagebox.askyesno("What's Up, Casey?", "The people love you! They want to thank you for the wonderful job you're doing. But they don't have a lot of money, so they sent you some picture frames (frame 3). Do you accept?")
                if y:
                    drawtr0232(3)
                    voice("The new frames have been installed in your throne room.")
                    messagebox.showinfo("What's Up, Casey?", "The new frames have been installed in your throne room.")
                else:
                    voice("Very well. I took the frames since you don't want them - it looks great on my wall!")
                    messagebox.showinfo("What's Up, Casey?", "Very well. I took the frames since you don't want them - it looks great on my wall!")
            elif x == 50:
                Casey_yesno("You have worked very hard. Would you like a vacation?", -1000000, "Ok. Your vacation and security cost 1 million dollars.", True, 0, "Ok.", True)
            elif x == 51:
                Casey_yesno("There has been a terrorist attack in your kingdom. 6 people died! Would you like to lower the palace flag to half mast?", 0, "Good choice.", True, -2800, "The people are furious about this! Some of them have climbed up your palace and took the flag down! They threw it in the trash. It costs 500 dollars for a new flag, 2000 dollars for roof repairs, and 300 dollars to arrest the crooks.", False)
            elif x == 52:
                Casey_yesno("There is a MOOSE in your FRONT YARD! You can call pest control. Would you like me to shoot it instead?", 0, "Ok. He's dead. But your council is mad! They've taken my shotgun!", False, -1000000000, "The pest control failed, and they're now in the hospital being treated for critical injuries. They've sued you! You owe them 1 billion in damages.", False)
            elif x == 53:
                Casey_info("Someone who won the lottery gave their money to you. You have received 600 million dollars.", 600000000, True)
            elif x == 54:
                y = randint(100, 350000000000)
                Casey_info("You have won %s dollars in a contest!" % y, y, True)
            elif x == 55:
                Casey_info("Your bathtub has flooded and the water ruined your shag carpet. New shag carpet costs 2 thousand dollars.", -2000, True)
            elif x == 56:
                y = randint(0, 1000000)
                y = y * -1
                Casey_info("Because of a banking error, you have lost %s dollars!" % abs(y), y, False)
            elif x == 57:
                voice("There is a carbon manoxide leak. Would you like to evacuate?")
                x = messagebox.askyesno("What's Up, Casey?", "There is a carbon manoxide leak. Would you like to evacuate?")
                if x:
                    voice("Good choice.")
                    messagebox.showinfo("What's Up, Casey?", "Good choice.")
                else:
                    voice("THE CARBON MANOXIDE HAS KILLED YOU!")
                    messagebox.showwarning("What's Up, Casey?", "THE CARBON MANOXIDE HAS KILLED YOU!")
                    exit_save_death()
            elif x == 58:
                voice("Nothing is up right now.")
                messagebox.showinfo("What's Up, Casey?", "Nothing is up right now.")
            elif x == 59:
                voice("Your mom called again. Said to tell you to brush your teeth better.")
                messagebox.showinfo("What's Up, Casey?", "Your mom called again. Said to tell you to brush your teeth better.")
            elif x == 60:
                voice("The 3rd floor of your palace is a mess! I'm sending up the cleaning crew.")
                messagebox.showinfo("What's Up, Casey?", "The 3rd floor of your palace is a mess! I'm sending up the cleaning crew.")
            elif x == 61:
                Casey_yesno("Your head caught on fire this morning, and the flames ruined your hair. Option 1: You can buy a wig and wear it until your hair grows back. Option 2: Wear a hat all the time. Would you like to buy a wig?", -100, "It cost one hundred dollars to buy a wig. But you now look just like George Washington, and as a result, more tourists are visitng your country.", False, 0, "OK.", False)
 
            elif x == 62:
                Casey_yesno("Ever since that latest news report has come out, people have started worrying about climate change in your country. There is a protest outside the palace - people want us to be more enviornmentally friendly. Would you like to plant more trees? If no, you can just make a speech to calm them down.", -1000000, "It cost one million dollars to plant more trees.", False, 0, "OK. There are still a few people protesting outside, but the police have them under control.", False)
            elif x == 64:
                Casey_info("We have collected the annual tax on one of your large cities. You have received 10 million dollars.", 10000000, False)
            else:
                Casey(False);
            sprint(details["money"])
            sprint(x)
            drawroomf()
    except Exception:
        er(format_exc())
def Casey_yesno(question, money1, message1, icon1, money2, message2, icon2):
    try:
        voice(question)
        y = messagebox.askyesno("What's Up, Casey?", question)
        if y == True:
            answer(True)
            mone(money1)
            voice(message1)
            if icon1 == True:
                messagebox.showinfo("What's Up, Casey?", message1)
            elif icon1 == False:
                messagebox.showwarning("What's Up, Casey?", message1)
        elif y == False:
            answer(False)
            details["answer"] = False
            mone(money2)
            voice(message2)
            if icon2 == True:
                messagebox.showinfo("What's Up, Casey?", message2)
            elif icon2 == False:
                messagebox.showwarning("What's Up, Casey?", message2)
    except Exception:
        er(format_exc())
def Casey_info(announcement, money, icon):
    try:
        details["money"] = details["money"] + money
        voice(announcement)
        if icon == True:
            messagebox.showinfo("What's Up, Casey?", announcement)
        elif icon == False:
            messagebox.showwarning("What's Up, Casey?", announcement)
    except Exception:
        er(format_exc())
def Casey_3opt(question, money1, message1, icon1, money2, message2, icon2, money3, message3, icon3):
    try:
        voice(singleLine(question))
        x = simpledialog.askfloat("What's Up, Casey?", question)
        if x == 1:
            details["money"] = details["money"] + money1
            voice(message1)
            if icon1 == False:
                messagebox.showwarning("What's Up, Casey?", message1)
            elif icon1 == True:
                messagebox.showinfo("What's Up, Casey?", message1)
        elif x == 2:
            details["money"] = details["money"] + money2
            voice(message2)
            if icon2 == False:
                messagebox.showwarning("What's Up, Casey?", message2)
            elif icon2 == True:
                messagebox.showinfo("What's Up, Casey?", message2)
        elif x == 3:
            voice(message3)
            details["money"] = details["money"] + money3
            if icon3 == False:
                messagebox.showwarning("What's Up, Casey?", message3)
            elif icon3 == True:
                messagebox.showinfo("What's Up, Casey?", message3)
        else:
            voice("You did not type 1, 2, or 3. Please try again.")
            messagebox.showerror("Error", "You did not type 1, 2, or 3. Please try again.")
            Casey_3opt(question, money1, message1, icon1, money2, message2, icon2, money3, message3, icon3)
    except Exception:
        er(format_exc())

def cheat():
    try:
        statusbar("Cheat Box")
        cheata = simpledialog.askstring('Cheat Box', 'Enter your code or type cheat code "Cancel" (case sensitive).')
        if cheata == None:
            pass
        elif cheata == '':
            cheat()
            return None
        else:
            if cheata == 'accessmore':
                statusbar("Cheat Code: accessmore")
            cheata = str("cheathings.") + str(cheata) + str("()")
            status('cheat.enter')
            exec(cheata)
            status('none')
    except Exception:
        er(format_exc())
class cheathings:
    def somethingiswrong():
        status('exsave222')
        raise Exception
    def outofcash():
        try:
            statusbar("Cheat Code: outofcash")
            details["money"] = 0
            drawroom()
        except Exception:
            er(format_exc())
    def whatsgoingon():
        try:
            statusbar("Cheat Code: whatsgoingon")
            x = simpledialog.askfloat("More Details", "Which Casey?")
            x = int(x)
            Casey(x)
        except Exception:
            er(format_exc())
    def imnotdead():
        try:
            statusbar("Cheat Code: imnotdead")
            details["lives"] = 1
        except Exception:
            er(format_exc())
    def Cancel():
        try:
            statusbar("Cheat Box cancelled")
        except Exception:
            er(format_exc())
    def removetheproblems():
        try:
            statusbar("Cheat Code: removetheproblems")
            me = open("C:\\uthronium\\debug.txt", 'w')
            me.write("")
            me.close()
        except Exception:
            er(format_exc())
    def accessmore():
        try:
            while 1:
                me = simpledialog.askstring("Command Line", "Type your commands below.                                   ")
                if me == None:
                    break
                else:
                    exec(me)
        except Exception:
            messagebox.showerror("Error", "The following error occurred in your last command: %s. Command line will now restart." % format_exc())
            cheathings.accessmore()
    def iamstressed():
        try:
            statusbar("Cheat Code: iamstressed")
            details["money"] = details["money"] + 500000
        except Exception:
            er(format_exc())
    def takemeshopping():
        drawstore2(False)
    def makemerich():
        try:
            statusbar("Cheat Code: makemerich")
            y = simpledialog.askfloat("Money", "Enter money to be added.")
            mone(y)
        except Exception:
            er(format_exc())
    def iamdead():
        statusbar("The program will now crash!")
        while 1:
            sleep(5)
    def constantwar():
        while 1:
            wargame1()
            sleep(5)
    def whatcanido():
        try:
            statusbar("Cheat Code: whatcanido")
        except Exception:
            er(format_exc())
        messagebox.showinfo("List", '''somethingiswrong: causes error
outofcash: makes cash 0
whatsgoingon: play a Casey of your choice
imnotdead: makes lives 1
Cancel: what it says
removetheproblems: erases debug.txt
accessmore: access python command line
iamstressed: adds 500 thousand dollars
iamdead: crash the program
makemegrow: allow program size to be changeable
takemeshopping: open store without logging in
constantwar: warmode 1 over and over
''')
    def makemegrow():
        try:
            statusbar("Cheat Code: makemegrow")
            root.resizable(True, True)
        except Exception:
            er(format_exc())
def exit_save():
    s = 0
    try:
        if details["user"] == None:
            messagebox.showerror("Cannot Save", "There is nothing to save! Log in to an account first.")
            return None
        sprint(temp["user"])
        sure = messagebox.askyesnocancel("Save Changes", "Would you like to save changes? Guest Accounts cannot save changes.")
        sprint(sure)
        if sure == True:
            exit_save2()
            if debug["os"] == True:
                initit = "C:\\Documents and settings\\all users\\Documents\\uthronium\\"
            else:
                initit = "C:\\users\\public\\Documents\\uthronium\\"
            if uname()[0] == 'Linux' or uname()[0] == 'Darwin':
                user = getuser()
                initit = str('/home/') + str(user) + str('/Public/uthronium/')
        elif sure == None:
            drawroom()
            return None
                
        else:
            if debug["os"] == True:
                initit = "C:\\Documents and settings\\all users\\Documents\\uthronium\\"
            else:
                initit = "C:\\users\\public\\Documents\\uthronium\\"
            if uname()[0] == 'Linux' or uname()[0] == 'Darwin':
                user = getuser()
                initit = str('/home/') + str(user) + str('/Public/uthronium/')
    except Exception:
        er(format_exc())
    try:
       pass 
    except OSError:
        s = 1
    except Exception:
        if s == 0:
            er(format_exc())
    try:
        if temp["shutdown"] == False:
            resetdetail()
            drawmain()
            temp["guest"] = False
    except Exception:
            er(format_exc())
def exit_save2():
    try:
        if temp["guest"] == False:
            print('guest')
            if temp["shutdown"] == False:
                statusbar("Logging off")
            details["kill1"] = scramble(details["kill1"])
            details["kill2"] = scramble(details["kill2"])
            details["pass"] = scramble(details["pass"])
            details["colorpass"] = scramble(details["colorpass"])
            file2 = temp["user"]
            file = open(file2, "wb")
            pickle.dump(details, file)
            file.close()
            if temp["shutdown"] == False:
                drawcan()
                drawmain()
            temp['guest'] = False
            resetdetail()
        else:
            print('nguest')
            resetdetail()
            drawmain()
            temp["guest"] = False
        if temp["shutdown"] == True:
            root.destroy()
    except Exception:
        er(format_exc())
def autosave(e):
    pass
def exit_save_death():
    try:
        details["lives"] = details["lives"] - 1
        if details["lives"] < 1:
            statusbar("Dying...")
            voice("You have no lives left. You will now die!")
            messagebox.showwarning("Death Alert", "You have no lives left. You will now die!")
            will()
            file2 = temp["user"]
            file = open(file2, "wb")
            pickle.dump("dead", file)
            file.close()
            details["new"] = False
            details["user"] = None
            resetdetail()
            drawmain()
        else:
            voice("You had enough lives! You have not died!")
            messagebox.showinfo("Death Alert", "You had enough lives! You have not died!")
            drawroom()
            
    except Exception:
        er(format_exc())
def load_kingdom():
    statusbar("Loading kingdom...")
    try:
        if debug["os"] == True:
            initit = "C:\\Documents and settings\\all users\\Documents\\uthronium\\"
        else:
            initit = "C:\\users\\public\\Documents\\uthronium\\"
        if uname()[0] == 'Linux' or uname()[0] == 'Darwin':
            user = getuser()
            initit = str('/home/') + str(user) + str('/Public/uthronium/')
        file = askopenfilename(filetypes=(("uThronium Kingdoms", ".utr"),), initialdir=initit)
        f = file
        sprint(file)
        file = open(file, 'rb')
    except:
        pass
    try:
        temp["user"] = f
        file = pickle.load(file)
    except:
        return None
    try:
        detail = file
        if detail == "dead":
            messagebox.showerror("Kingdom Deleted", "This kingdom has been deleted and cannot be loaded.")
        else:
            details["money"] = detail["money"]
            sprint(detail["money"])
            details["lives"] = detail["lives"]
            details["user"] = detail["user"]
            details["tr0"] = detail["tr0"]
            details["tr1"] = detail["tr1"]
            details["tr2"] = detail["tr2"]
            details["tr3"] = detail["tr3"]
            details["tr4"] = detail["tr4"]
            details["tr5"] = detail["tr5"]
            details["tr6"] = detail["tr6"]
            details["person"] = detail["person"]
            details["f1"] = detail["f1"]
            details["f2"] = detail["f2"]
            details["f3"] = detail["f3"]
            details["pass"] = unscramble(detail["pass"])
            details["colorpass"] = unscramble(detail["colorpass"])
            details["kill1"] = unscramble(detail["kill1"])
            details["kill2"] = unscramble(detail["kill2"])
            details["new"] = detail["new"]
            if details["pass"] != None:
                loadpass()
                
            else:
                if details["colorpass"] == None:
                    drawroom()
                    speak("Welcome back! Here is the current status of your kingdom: " + details["News"])
                else:
                    colorpa(False)
                    
            
    except Exception:
        er(format_exc())
def loadpass():
    password_input(True)
def debt():
    try:
        me = details["money"]
        if me < 0:
            voice("Alert: The country is now in debt! If you let your debt get higher than 10 billion you will be assasinated!")
            messagebox.showwarning("Debt Warning", "Alert: The country is now in debt! If you let your debt get higher than 10 billion you will be assasinated!")
        if me < -10000000000:
            voice( "You have over 10 billion dollars in debt. The people are not happy about this. They have assasinated you! You will now lose all progress in the game unless you have another life.")
            messagebox.showerror("Debt Warning", "You have over 10 billion dollars in debt. The people are not happy about this. They have assasinated you! You will now lose all progress in the game unless you have another life.")
            exit_save_death()
        rand = randint(0, 100)
        if rand > 70 and details["kill1"] == True:
            voice("Remember how earlier you declined to put your bodyguards on high alert? Well, too late now, they're dead. The assasain has arrived and")
            messagebox.showerror("Death", "Remember how earlier you declined to put your bodyguards on high alert? Well, too late now, they're dead. The assasain has arrived and...AAGH!!!! ...........")
            exit_save_death()
        killme2()
    except Exception:
        er(format_exc())
def answer(x):
    try:
        debug["answer"] = x
    except Exception:
        er(format_exc())
def confirm():
    try: 
        statusbar("Confirmation Pending")
        me = messagebox.askokcancel("Confirmation Required", "Are you sure you would like to proceed?")
        return me
    except Exception:
        er(format_exc())
def create_king():
    if confirm() != True:
        return None
    try:
        statusbar("Creating kingdom")
        details["new"] = True
        details["user"] = True
        drawroom()
    except Exception:
        er(format_exc())
def aboutit():
    statusbar("About")
    messagebox.showinfo("About", '''
uThronium was created by Tobias Park.
Throne room photos are taken from the English Wikipedia.
Most images are in the public domain.
Assistant Artist is Lily Park
''')
def randmurph():
    Casey(False)
def z(x):
    messagebox.showinfo("Details About This Item", x)
def sdpas1():
    z("Protect your account with words, numbers, and symbols.")
def sdpas2():
    z("Traditional password too boring? Use a system of clicking colored buttons instead!")
def drawpas():
    try:
        statusbar('Drawing Store - Password')
        drawcan()
        canvas.create_rectangle(0, 0, 800, 600, fill="#F1EEE5")
        canvas.create_text(400, 50, text="Passwords", font=('Belwe Cn BT', 72), fill='black')
        bac = Button(root, text="<- Back to Store", command=drawstore)
        bac.place(relx=.050, rely=.850)
        a = Button(root, text="Traditional", command=pas)
        a.place(relx=.42, rely=.4, anchor=NE)
        b = Button(root, text="Color", command=colorp)
        b.place(relx=.6, rely=.4, anchor=NW)
        b1 = Button(root, text="Details", command=sdpas2, padx=50)
        b1.place(relx=.54, rely=.45, anchor=NW)
        b2 = Button(root, text="Details", command=sdpas1, padx=50)
        b2.place(relx=.465, rely=.45, anchor=NE)
        canvas.create_text(310, 310, text="Price: $5,000,000", font=('Belwe Cn BT', 12), fill='black')
        canvas.create_text(510, 310, text="Price: $5,200,000", font=('Belwe Cn BT', 12), fill='black')
    except Exception:
        er(format_exc())
def df1():
    z('''Buy this nice contemporary picture frame, complete with colored squares!''')
def df2():
    z("Check out this awesome frame with an ocean background!")
def df3():
    z("Take this wooden frame! It also already has a hole for hanging! (who cares)")
def drawframe():
    try:
        statusbar('Drawing Store - Picture Frames')
        drawcan()
        canvas.create_rectangle(0, 0, 800, 600, fill="#F1EEE5")
        canvas.create_text(400, 50, text="Picture Frames", font=('Belwe Cn BT', 72), fill='black')
        bac = Button(root, text="<- Back to Store", command=drawstore)
        bac.place(relx=.050, rely=.850)
        a = Button(root, image=f1, command=drawf1)
        a.place(relx=.075, rely=.3)
        b = Button(root, image=f2, command=drawf2)
        b.place(relx=.375, rely=.3)
        c = Button(root, image=f3, command=drawf3)
        c.place(relx=.675, rely=.3)
        canvas.create_text(160, 300, text="Frame 1", fill='black', font=('Belwe Cn BT', 16))
        canvas.create_text(400, 300, text="Frame 2", fill='black', font=('Belwe Cn BT', 16))
        canvas.create_text(640, 300, text="Frame 3", fill='black', font=('Belwe Cn BT', 16))
        
        a1 = Button(root, text="Details", command=df1, padx=50)
        a1.place(relx=.11, rely=.52)
        b1 = Button(root, text="Details", command=df2, padx=50)
        b1.place(relx=.41, rely=.52)
        canvas.create_text(160, 350, text="Price: $150", font=('Belwe Cn BT', 12), fill='black')
        c1 = Button(root, text="Details", command=df3, padx=50)
        c1.place(relx=.71, rely=.52)
        canvas.create_text(400, 350, text=" Price: $200", font=('Belwe Cn BT', 12), fill='black')
        canvas.create_text(640, 350, text="Price: $300", font=('Belwe Cn BT', 12), fill='black')
    except Exception:
        er(format_exc())
def drawf12(roomtobe, money):
    try:
        if confirm():
            if True:
                
            
                statusbar(str('Buying Throne Room ') + str(roomtobe))
                mone(money)
                for x in range(0, 3):
                    x = x + 1
                    if roomtobe != x:
                        if details[str("f") + str(x)] == 'y':
                            details[str("f") + str(x)] = True
                details[str("f") + str(roomtobe)] = 'y'
                drawroom()
    except Exception:
        er(format_exc())
def drawtr0232(roomtobe):
    try:
        for x in range(1, 4):
            if roomtobe != x:
                if details[str("f") + str(x)] == 'y':
                    details[str("f") + str(x)] = True
        statusbar(str('Buying Picture Frame ') + str(roomtobe))
        details[str("f") + str(roomtobe)] = 'y'
        sprint(roomtobe)
        drawroom()
    except Exception:
        er(format_exc())
def drawf10():
    drawtr0232(1)
def drawf20():
    drawtr0232(2)
def drawf30():
    drawtr0232(3)
def drawf1():
    drawf12(1, -150)
def drawf2():
    drawf12(2, -200)
def drawf3():
    drawf12(3, -300)
def colorp():
    try:
        me = True
        if details["pass"] != None or details["colorpass"] != None:
            messagebox.showerror("Password Already Bought", "You already have a password in your possesion. To return it, go to the store's \"Front Desk\".")
            me = False
        if me:
            if confirm():
                colorpa(True)
    except Exception:
        er(format_exc())
def drawmains():
    resetdetail()
    drawmain()
def colorpa(x):
    try:
        status('color')
        global countp
        countp = 0
        drawcan()
        a = Button(root, image=c_1, command=cp1)
        a.place(relx=.0, rely=.0, anchor=NW)
        b = Button(root, image=c_2, command=cp2)
        b.place(relx=.33, rely=.0, anchor=NW)
        c = Button(root, image=c_3, command=cp3)
        c.place(relx=.66, rely=.0, anchor=NW)

        a = Button(root, image=c_4, command=cp4)
        a.place(relx=.0, rely=.3, anchor=NW)
        b = Button(root, image=c_5, command=cp5)
        b.place(relx=.33, rely=.3, anchor=NW)
        c = Button(root, image=c_6, command=cp6)
        c.place(relx=.66, rely=.3, anchor=NW)

        d = Button(root, image=c_7, command=cp7)
        d.place(relx=.0, rely=.6, anchor=NW)
        e = Button(root, image=c_8, command=cp8)
        e.place(relx=.33, rely=.6, anchor=NW)
        f = Button(root, image=c_9, command=cp9)
        f.place(relx=.66, rely=.6, anchor=NW)
        back = Button(root, text="Back to Login Screen", command=drawmains)
        back.place(relx=.45, rely=.950, anchor=W)
        passtemp["setup"] = x
        passtemp["pass"] = ""
        passtemp["colors"] = ""
        go = Button(root, text="Go", command=gopass)
        go.place(relx=.45, rely=.950, anchor=E)
        if x == True:
            messagebox.showinfo("How to Use", "Each button has a different color. Click the buttons to set your password to the colors of your choice.")
        else:
            messagebox.showinfo("How to Use", "Each button has a different color. Click the buttons to enter the password with the colors you chose earlier.")
    except Exception:
        er(format_exc())
def cp1():
    passtemp["pass"] = str(passtemp["pass"]) + str('1')
    passtemp["colors"] = str(passtemp["colors"]) + str('Black. ')
def cp2():
    passtemp["pass"] = str(passtemp["pass"]) + str('2')
    passtemp["colors"] = str(passtemp["colors"]) + str('Red. ')
def cp3():
    passtemp["pass"] = str(passtemp["pass"]) + str('3')
    passtemp["colors"] = str(passtemp["colors"]) + str('Dark Blue. ')
def cp4():
    passtemp["pass"] = str(passtemp["pass"]) + str('4')
    passtemp["colors"] = str(passtemp["colors"]) + str('Purple/Pink. ')
def cp5():
    passtemp["pass"] = str(passtemp["pass"]) + str('5')
    passtemp["colors"] = str(passtemp["colors"]) + str('Green. ')
def cp6():
    passtemp["pass"] = str(passtemp["pass"]) + str('6')
    passtemp["colors"] = str(passtemp["colors"]) + str('White. ')
def cp7():
    passtemp["pass"] = str(passtemp["pass"]) + str('7')
    passtemp["colors"] = str(passtemp["colors"]) + str('Yellow. ')
def cp8():
    passtemp["pass"] = str(passtemp["pass"]) + str('8')
    passtemp["colors"] = str(passtemp["colors"]) + str('Light Blue. ')
def cp9():
    passtemp["pass"] = str(passtemp["pass"]) + str('9')
    passtemp["colors"] = str(passtemp["colors"]) + str('Orange. ')
def gopass():
    if passtemp["setup"] == True:
        x = messagebox.askyesno("Confirm Password", str(passtemp["colors"]) + str('Is that the color password you entered?'))
        if x:
            gopass3(passtemp)
        else:
            messagebox.showinfo("Repeating Action", "Ok. Please try again. You will not be charged twice.")
            colorp()
    else:
        gopass3(passtemp)
def gopass3(x):
    try:
        passtemp = x
        if passtemp["setup"] == False:
            if passtemp["pass"] != "":
                if passtemp["pass"] == details["colorpass"]:
                    drawroom()
                    
                    speak("Welcome back! here are the latest updates on your kingdom: " + details["News"])
                else:
                    messagebox.showerror("Wrong Password", "Incorrect color password.")
                    passtemp["pass"] = ""
        else:
            mone(-5200000)
            details["colorpass"] = passtemp["pass"]
            status('drawroom')
            drawroom()
            passtemp = None
            
    except Exception:
        er(format_exc())
def a1131():
    z('''Are you afraid of dying? Buy the best life insuranse around - another life!''')
def a1132():
    z('''See what Casey looks like by having him stand in your throne room!''')
def a1133():
    z('''Help the poor by donating any amount!''')
def a1134():
    z('''Click to invest 5000 dollars in the stock market. We will buy/ sell for you!''')
def drawother():
    try:
        statusbar("Drawing Store - Other")
        drawcan()
        canvas.create_rectangle(0, 0, 800, 600, fill="#F1EEE5")
        canvas.create_text(400, 50, text="Other", font=('Belwe Cn BT', 72), fill='black')
        bac = Button(root, text="<- Back to Store", command=drawstore)
        bac.place(relx=.050, rely=.850)
        a = Button(root, text="Buy Another Life", command=newlife)
        a.place(relx=.1, rely=.4)
        b = Button(root, image=personprev, command=visual)
        canvas.create_text(275, 170, text="Visual Person Casey", fill='black', font=('Belwe Cn BT', 16))
        b.place(relx=.3, rely=.3)
        c = Button(root, text="Donate to the Poor", command=useless)
        c.place(relx=.5, rely=.4)
        d = Button(root, text="Invest Money in the Stock Market", command=stock)
        d.place(relx=.7, rely=.4)
        a1 = Button(root, text="Details", command=a1131)
        a1.place(relx=.135, rely=.45)
        a2 = Button(root, text="Details", command=a1132)
        a2.place(relx=.325, rely=.59)
        a3 = Button(root, text="Details", command=a1133)
        a3.place(relx=.54, rely=.45)
        a4 = Button(root, text="Details", command=a1134)
        a4.place(relx=.775, rely=.45)
        canvas.create_text(135, 320, text="Price: $5 Billion", font=('Belwe Cn BT', 12), fill='black')
        canvas.create_text(280, 400, text="Price: $10 Thousand", font=('Belwe Cn BT', 12), fill='black')
        canvas.create_text(455, 320, text="Price: Your Choice", font=('Belwe Cn BT', 12), fill='black')
        canvas.create_text(650, 320, text="Price: $5,000 Initial Cost", font=('Belwe Cn BT', 12), fill='black')
    except Exception:
        er(format_exc())
def stock():
    try:
        if confirm():
            statusbar("Investing Money in the Stock Market")
            
            drawother()
            messagebox.showinfo("Stock Update", "5000 dollars have been invested. I am managing the stocks, so you do not have to worry about all the details.")
            x = randint(0, 100)
            y = randint(0, 5000)
            if x < 52:
                z = details["money"] + 5000 + y
                messagebox.showinfo("Stock Update", "You have gained %s dollars!" % y)
            else:
                z = details["money"] + 5000 - y
                messagebox.showinfo("Stock Update", "You have lost %s dollars!" % y)
            details["money"] = z
            drawroomt(None)
    except Exception:
        er(format_exc())
def useless():
    try:
        if confirm():
            statusbar("Donating to the Poor")
            x = simpledialog.askfloat("Donate to the Poor", "Type in amount to donate to the poor.")
            if x < 0:
                messagebox.showerror("Transaction Rejected", "Your transaction was not properly filed.")
                return None
            x = x * -1
            mone(x)
    except:
        y = messagebox.askretrycancel("Nothing Entered", "You did not enter a number. Try again?")
        if y == True:
            useless()
def visual():
    try:
        if confirm() and details["person"] == False:
            statusbar('Buying Visual Person Casey')
            mone(-10000)
            details["person"] = True
            drawroom()
        elif details["person"] == True:
            messagebox.showerror("Already Bought", "You have already bought this item.")
    except Exception:
        er(format_exc())
def newlife():
    try:
        if confirm() == True:
            statusbar('Buying New Life')
            mone(-5000000000)
            details["lives"] = details["lives"] + 1
            drawroom()
    except Exception:
        er(format_exc())
def drawstore():
    drawstore2(True)
def drawstore2(x):
    try:
        if details["user"] == None and x != False or debug["status"] == 'color':
            messagebox.showerror("Login Required", "Please log in to your account to access the store.")
        else:
            statusbar("Drawing Store")
            drawcan()
            canvas.create_rectangle(0, 0, 800, 600, fill="#F1EEE5")
            b = Button(root, text="<- Back to Throne Room", command=drawroom)
            b.place(relx=.050, rely=.850)
            canvas.create_text(400, 50, text="Store", font=('Belwe Cn BT', 72), fill='black')
            a = Button(root, image=trprev, command=drawtroom)
            a.place(relx=.050, rely=.300)
            canvas.create_text(120, 320, text="Throne Rooms", font=('Belwe Cn BT', 16), fill='black')
            p = Button(root, image=puz, command=drawpas)
            p.place(relx=.300, rely=.270)
            canvas.create_text(320, 330, text="Passwords", font=('Belwe Cn BT', 16), fill='black')
            frame = Button(root, image=fprev, command=drawframe)
            frame.place(relx=.520, rely=.330)
            canvas.create_text(520, 330, text="Picture Frames", font=('Belwe Cn BT', 16), fill='black')
            oth = Button(root, image=other, command=drawother)
            oth.place(relx=.85, rely=.250)
            canvas.create_text(720, 330, text="Other", font=('Belwe Cn BT', 16), fill='black')
            d = Button(root, text="Return Passwords//Visual Casey", command=drawdesk)
            d.place(relx=.4, rely=.75, anchor=W)
            
    except Exception:
        er(format_exc())
def drawdesk():
    try:
        statusbar("Drawing Store - Return Item")
        drawcan()
        canvas.create_rectangle(0, 0, 800, 600, fill="#F1EEE5")
        b = Button(root, text="<- Back to Store", command=drawstore)
        b.place(relx=.050, rely=.850)
        canvas.create_text(400, 50, text="Return An Item", font=('Belwe Cn BT', 72), fill='black')
        canvas.create_text(390, 150, text="Choose an item to return.", font=('Belwe Cn BT', 30), fill='black')
        
        p = Button(root, text="Password", command=returnpas)
        p.place(relx=.300, rely=.30)
        
        
        oth = Button(root, text="Visual Casey", command=returnother)
        oth.place(relx=.60, rely=.30)
        
    except Exception:
        er(format_exc())

def returnpas():
    x = True
    if confirm() == True and (details["pass"] != None or details["colorpass"] != None):
        if details["pass"] != None:
            details["pass"] = None
            mone(5000000)
        else:
            x = False
            details["colorpass"] = None
            mone(5200000)
        if x:
            messagebox.showinfo("Refund Amount", "You have been refunded 5 million dollars for Traditional Password.")
        else:
            messagebox.showinfo("Refund Amount", "You have been refunded 5.2 million dollars for Color Password.")
    else:
        drawroom()
def returnother():
    
    if details["person"] == True:
        details["person"] = False
        mone(10000)
    else:
        drawroom()
def returntroom():
    try:
        if confirm():
            statusbar('Returning Throne Room')
            y = False
            x = simpledialog.askfloat('Enter Room Number', "Enter the number of the room you would like to return. Example: To return Throne Room 1, type \"1\".")
            x = int(x)
            z = details[str('tr') + str(x)]
            if z == False:
                messagebox.showerror("Not Bought", "You cannot return an item you have not bought!")
                y = True
            if z == 'y':
                messagebox.showerror("Using This Room", "You are currently using this room! Please select another room from the storeroom or buy another room before continuing. The storeroom is located in the 'Throne Rooms' section of the store.")
            
            if y == False:
                if x == 0:
                    mone(250000)
                if x == 1:
                    mone(100000)
                if x == 2:
                    mone(300000)
                if x == 3:
                    mone(500000)
                if x == 4:
                    mone(200000)
                if x == 5:
                    mone(100000000)
                if x == 6:
                    mone(150000000)
                details[str('tr') + str(x)] = False
    except Exception:
        if debug["status"] != 'returntroom':
            er(format_exc())
        else:
            messagebox.showerror("Invalid Answer", "Your answer did not conform to specifications. Please try again.")
def drawtr0():
    drawtr23(-250000, 0)
def drawtr1():
    drawtr23(-100000, 1)
def drawtr2():
    drawtr23(-300000, 2)
def drawtr3():
    drawtr23(-500000, 3)
def drawtr4():
    drawtr23(-200000, 4)
def drawtr023(roomtobe):
    try:
        statusbar(str('Buying Throne Room ') + str(roomtobe))
        for x in range(0, 7):
            if roomtobe != x:
                if details[str("tr") + str(x)] == 'y':
                    details[str("tr") + str(x)] = True
        details[str("tr") + str(roomtobe)] = 'y'
        sprint(roomtobe)
        drawroom()
    except Exception:
        er(format_exc())
def drawtr01():
    drawtr023(1)
def drawtr02():
    drawtr023(2)
def drawtr03():
    drawtr023(3)
def drawtr04():
    drawtr023(4)
def drawtr00():
    drawtr023(0)
def drawtr05():
    drawtr023(5)
def drawtr06():
    drawtr023(6)
def drawstoreroom():
    try:
        statusbar('Drawing Store - Throne Rooms - Storeroom')
        drawcan()
        canvas.create_rectangle(0, 0, 800, 600, fill="#F1EEE5")
        canvas.create_text(400, 50, text="Throne Rooms - Storeroom", font=('Belwe Cn BT', 48), fill='black')
        canvas.create_text(400, 300, text="A shaded button means that that room has not be bought, or is being used.", font=('Belwe Cn BT', 19), fill='black')
        back = Button(root, text="<- Back to Throne Rooms", command=drawtroom)
        back.place(relx=.050, rely=.8)
        a = Button(root, image=fp0, command=drawtr00)
        a.place(relx=.050, rely=.200)
        canvas.create_text(120, 260, text="Room 0", font=('Belwe Cn BT', 16), fill='black')
        b = Button(root, image=fp1, command=drawtr01)
        b.place(relx=.270, rely=.200)
        canvas.create_text(300, 260, text="Room 1", font=('Belwe Cn BT', 16), fill='black')
        c = Button(root, image=fp2, command=drawtr02)
        c.place(relx=.49, rely=.2)
        canvas.create_text(480, 260, text="Room 2", font=('Belwe Cn BT', 16), fill='black')
        d = Button(root, image=fp3, command=drawtr03)
        d.place(relx=.71, rely=.2)
        canvas.create_text(650, 260, text="Room 3", font=('Belwe Cn BT', 16), fill='black')
        e = Button(root, image=fp4, command=drawtr04)
        e.place(relx=.27, rely=.575)
        canvas.create_text(300, 490, text="Room 4", font=('Belwe Cn BT', 16), fill='black')
        f = Button(root, image=fp5, command=drawtr05)
        f.place(relx=.49, rely=.575)
        canvas.create_text(475, 490, text="Room 5", font=('Belwe Cn BT', 16), fill='black')
        g = Button(root, image=fp6, command=drawtr06)
        g.place(relx=.71, rely=.575)
        canvas.create_text(650, 490, text="Room 6", font=('Belwe Cn BT', 16), fill='black')
        y = 0
        for x in range(0, 7):
            h = str(details[str('tr') + str(x)])
            sprint(h)
            if h != 'True' or h == 'y':
                if x == 0:
                    z = 'a'
                if x == 1:
                    z = 'b'
                if x == 2:
                    z = 'c'
                if x == 3:
                    z = 'd'
                if x == 4:
                    z = 'e'
                if x == 5:
                    z = 'f'
                if x == 6:
                    z = 'g'
                exec(str(z) + str('.config(state=DISABLED)'))
            y = y + 1
    except Exception:
        er(format_exc())
def drawtr23(money, roomtobe):
    try:
        statusbar(str('Buying Throne Room ') + str(roomtobe))
        if confirm():
            
            mone(money)
            for x in range(0, 7):
                if roomtobe != x:
                    if details[str("tr") + str(x)] == 'y':
                        details[str("tr") + str(x)] = True
            details[str("tr") + str(roomtobe)] = 'y'
            drawroom()
    except Exception:
        er(format_exc())
def drawtr6():
    drawtr23(-1500000, 6)
def drawtr5():
    drawtr23(-1000000, 5)
def drs1():
    z('''You'll love this luxurious red velvet throne room!''')
def drs2():
    z('''You'll love this luxurious red velvet throne room!''')
def drs3():
    z('''Enjoy this ancient-style throne room!''')
def drs4():
    z('''Enjoy this court like throne room''')
def drs5():
    z('''Enjoy this gold-embroidered throne room!''')
def drs6():
    z('''Have a REAL throne room, complete with red carpet!''')
def drs7():
    z('''Put your throne room in front of the White House!''')
def drawtroom():
    try:
        statusbar('Drawing Store - Throne Rooms')
        drawcan()
        canvas.create_rectangle(0, 0, 800, 600, fill="#F1EEE5")
        back = Button(root, text="<- Back to Store", command=drawstore)
        back.place(relx=.050, rely=.8)
        
        canvas.create_text(400, 50, text='''Throne Rooms''', font=('Belwe Cn BT', 72), fill='black')
        
        b = Button(root, image=fp1, command=drawtr1)
        b.place(relx=.270, rely=.200)
        
        b = Button(root, image=fp1, command=drawtr1)
        b.place(relx=.270, rely=.200)
        canvas.create_text(300, 260, text="Room 1", font=('Belwe Cn BT', 16), fill='black')
        
        canvas.create_text(300, 320, text="Price: $100,000", font=('Belwe Cn BT', 12), fill='black')
        c = Button(root, image=fp2, command=drawtr2)
        c.place(relx=.49, rely=.2)
        canvas.create_text(480, 260, text="Room 2", font=('Belwe Cn BT', 16), fill='black')
        b1 = Button(root, text="Details", command=drs2)
        b1.place(relx=.33, rely=.45)
        c1 = Button(root, text="Details", command=drs3)
        c1.place(relx=.56, rely=.45)
        canvas.create_text(480, 320, text="Price: $300,000", font=('Belwe Cn BT', 12), fill='black')
        d = Button(root, image=fp3, command=drawtr3)
        d.place(relx=.71, rely=.2)
        d1 = Button(root, text="Details", command=drs4)
        d1.place(relx=.77, rely=.45)
        canvas.create_text(650, 260, text="Room 3", font=('Belwe Cn BT', 16), fill='black')
        canvas.create_text(650, 320, text="Price: $500,000", font=('Belwe Cn BT', 12), fill='black')
        e = Button(root, image=fp4, command=drawtr4)
        e.place(relx=.27, rely=.575)
        e1 = Button(root, text="Details", command=drs5)
        e1.place(relx=.335, rely=.84)
        canvas.create_text(300, 490, text="Room 4", font=('Belwe Cn BT', 16), fill='black')
        canvas.create_text(300, 550, text="Price: $200,000", font=('Belwe Cn BT', 12), fill='black')
        f = Button(root, image=fp5, command=drawtr5)
        f.place(relx=.490, rely=.575)
        f1 = Button(root, text="Details", command=drs6)
        f1.place(relx=.55, rely=.84)
        canvas.create_text(475, 490, text="Room 5", font=('Belwe Cn BT', 16), fill='black')
        canvas.create_text(475, 550, text="Price: $1,000,000", font=('Belwe Cn BT', 12), fill='black')
        g = Button(root, image=fp6, command=drawtr6)
        g.place(relx=.71, rely=.575)
        g1 = Button(root, text="Details", command=drs7)
        g1.place(relx=.77, rely=.841)
        canvas.create_text(650, 490, text="Room 6", font=('Belwe Cn BT', 16), fill='black')
        canvas.create_text(650, 550, text="Price: $1,500,000", font=('Belwe Cn BT', 12), fill='black')
    except Exception:
        er(format_exc())
def drawacc():
    warm()
def warm():
    try:
        if logged():
            if confirm():
                statusbar("War Mode - Choosing Mode and Transaction")
                messagebox.showinfo("War Mode Info", 'Dying in "War Mode" does not affect your uThrone account.')
                x = randint(0, 1)
                if x == 0:
                    mone(2000000)
                    messagebox.showinfo("War Mode Info", "Your rich uncle is proud of you for serving in battle with your troops. He has sent you 2 million dollars.")
                else:
                    mone(-2000000)
                    messagebox.showinfo("War Mode Info", "It cost 2 million dollars to sneak you into the army.")
                wargame1()
        else:
            messagebox.showerror("Log In", "You must have in account to play War Mode.")
    except Exception:
        er(format_exc())
def spy():
    try:
        if logged():
            messagebox.showinfo("Payment", "Payment for Spy Mode is 1 What's Up, Casey? session.")
            if confirm():
                statusbar("Spy Mode 1")
                Casey(False)
                spy1()
        else:
            messagebox.showerror("Log In", "Log in to your account to enjoy Spy Mode.")
    except Exception:
        er(format_exc())
def textm():
    messagebox.showinfo("Fee", "This call will cost 10 dollars.")
    if confirm():
        mone(-10)
        name = simpledialog.askstring("Texting", "Who do you wish to text?                      ")
        if name == None:
            return None
        x = simpledialog.askstring("Texting: %s" % name, "Hello, this is %s. How can I help you?" % name)
        if x == None:
            return None
        x = simpledialog.askstring("Texting: %s" % name, "Did you say %s? Oh, you did. I don't know." % x)
        if x == None:
            return None
        for y in range(0, 20):
            x = simpledialog.askstring("Texting: %s. Add something to the conversation. Or type code 1357 to stop texting." % name, "Yeah. %s.                        " % x)
            if x == None:
                return None
        messagebox.showinfo("Texting: %s" % name, "Well, I got to go now. Call again!")
def pas():
    try:
        me = True
        if details["pass"] != None or details["colorpass"] != None:
            messagebox.showerror("Password Already Bought", "You already have a password in your possesion. To return it, go to the store's \"Front Desk\".")
            me = False
        if me:
            if confirm():
                if details["pass"] == None:
                    statusbar("Buying Traditional Password")
                    mone(-5000000)
                    x = simpledialog.askstring("Enter Password", "Please Enter Your Password Below. Characters are shown so that you enter it correctly.")
                    y = x
                    if x == "" or x == None:
                        messagebox.showerror("Nothing Entered", "Nothing Entered. Please try again. You will be charged a 5 million dollar fine.")
                        pas()
                        return None
                    if x == y:
                        details["pass"] = x
                        drawroom()
                    else:
                        messagebox.showerror("Non-Matching", "Passwords do not match.")
                        mone(5000000)
                else:
                    messagebox.showerror("Already Bought", "You already have a password.")
    except Exception:
        er(format_exc())
        
def instruct():
    messagebox.showinfo("Instructions", '''These instructions describe what each button in your throne room does.
MONEY : Amount of money in dollars that you have in your royal treasury. Careful not to go into debt!

LIVES: Number of lives you have remaining (like in a classic video game). You can buy more lives at the Store.

NOTE: A "Picture Frame" displays the money and lives on your throne room. You can change the style of your picture frame in the store.

WHITE TICKER TAPE LOCATED ABOVE THE BUTTONS: This shows you the current status of your kingdom, including current weather, favorability ratings, and latest news.

RESIGN (DELETE ACCOUNT): Step down as ruler of your kingdom. This deletes your account permenantly.

WHAT'S UP, Casey?: Casey is your royal advisor. Press this button to ask Casey, "What's up?" Casey will then respond by telling you what is going on around your kingdom, and maybe asking you to make a decision about an important matter.

EXIT KINGDOM: The equivalent of Log Off/Log Out: Save your current progress and go back to the main menu.

STORE: Buy decorations and accessories for your throne room (or get a new throne room), buy accessories for your uThronium account (like a password), and more!

WAR MODE: War mode is a uThronium mini-game where you must steer your ship to avoid getting near the force-field equipped missiles!

UPDATE KINGDOM STATUS: This updates the little ticker tape that you see above these buttons with the latest kingdom status, including current weather, latest news, and favorability ratings

Casey'S VOICE ON/OFF: Casey can talk! Press this button to toggle his voice on or off.

NOTE: You can change the background picture of your throne room by going to the Store and selecting a new throne room!''')
def resig():
    try:
        if confirm() == True:
            details["lives"] = 1
            exit_save_death()
    except Exception:
        er(format_exc())
def showrules():
    statusbar('Displaying Rules')
    messagebox.showinfo("Rules", '''Rules:
1. A player may not use the Guest account or another kingdom to donate money to another kingdom in his/her posession.
2. A player may not change a kingdom file.
3. A player may not attempt to extract a password from a game file, even without the scramble code.

Play safe!''')
def donat():
    try:
        statusbar('Donating Money to Another User')
        if confirm() == True:
            x = simpledialog.askfloat("Donate", '''How much money would you like to donate?
You may choose who to donate money to
after entering amount.''')
            if x < 0:
                messagebox.showerror("Error", "The transaction you requested has been rejected.")
            else:
                if debug["os"] == True:
                    initit = "C:\\Documents and settings\\all users\\Documents\\uthronium\\"
                else:
                    initit = "C:\\users\\public\\Documents\\uthronium\\"
                file = askopenfilename(filetypes=(("uThronium Kingdoms", ".utr"),), initialdir=initit)
                z = open(file, 'rb')
                sprint(file)
                z = pickle.load(z)
                z["money"] = z["money"] + x
                if debug["os"] == True:
                    file2 = str("C:\\Documents and settings\\all users\\Documents\\uthronium\\") + str(z["user"]) + str(".utr")
                else:
                    file2 = str("C:\\users\\public\\Documents\\uthronium\\") + str(z["user"]) + str(".utr")
                file3 = open(file2, "wb")
                pickle.dump(z, file3)
                file3.close()
                statusbar(str('Donating ') + str(x) + str(' amount of money to the poor'))
                x = -1 * x
                mone(x)
    except Exception:
        er(format_exc())
def drawroom():
    drawroomt(True)
def update():
    drawroom()
    speak("Here are the latest updates on your kingdom. " + details["News"])
def toggle():
    if details["tr0"] == True:
        messagebox.showinfo("Casey's Voice Off", "Casey's voice has been turned off. If Casey is currently speaking, his voice will turn off after he is finished.")
        details["tr0"] = False
    else:
        messagebox.showinfo("Casey's Voice On", "Casey's voice has been turned on. Note: If your system does not support the functions needed for Casey's voice, it will not work.")
        details["tr0"] = True
def drawroomt(x):
    print(debug["status"])
    if debug["status"] == 'pass' or debug["status"] == 'colorpass':
        return None
    try:
        status('drawroom')
        statusbar('Drawing Throne Room')
        if x == False:
            sprint('hi')
            temp["guest"] = True
        if details["user"] == None and x != False:
            messagebox.showerror("No Account", "You are currently not logged on to an account!")
        else:
            drawcan()
            if 1:
                if details["tr1"] == 'y':
                    drawtr(tr1f)
                
                elif details["tr2"] == 'y':
                    drawtr(tr2f)
                elif details["tr3"] == 'y':
                    drawtr(tr3f)
                elif details["tr4"] == 'y':
                    drawtr(tr4f)
                elif details["tr5"] == 'y':
                    drawtr(tr5f)
                elif details["tr6"] == 'y':
                    drawtr(tr6f)
                else:
                    details["new"] = True
                    z = randint(1, 6)
                    y = str('tr') + str(z)
                    details[y] = 'y'
                    drawroomt(x)
                    return None
            lo = Button(canvas, text='''Exit
Kingdom''', font=('Belwe Cn BT', 15), anchor=W, command=exit_save)
            lo.place(relx=.47, rely=.84)
            store = Button(canvas, text="Store", font=('Belwe Cn BT', 15), anchor=W, command=drawstore)
            store.place(relx=.581, rely=.84)
            i = Button(canvas, text="Instructions", font=('Belwe Cn BT', 15), anchor=W, command=instruct)
            i.place(relx=.204, rely=.84)
            r = Button(canvas, text='''Resign
(Delete Account)''', font=('Belwe Cn BT', 15), anchor=W, command=resig)
            r.place(relx=.02, rely=.84)
            
            news = ["Robot Destroys Village", "Explosion in Taco Field", "King Sleeps In", "Casey Trips on Stairs", "Royal Pen Runs Dry", "Tourist Campaign Successful", "Terrorist Attack Foiled", "No News Today"]
            wx = ["Sunny", "Cloudy", "Rainy", "Snowy", "Hot", "Cold", "Thunderstorms", "Windy", "Tornados", "Hurricanes"]
            people = ["Hungry", "Sleepy", "Grumpy", "Grouchy", "Happy", "Sad", "Angry", "Frustrated", "Hopeful", "Optimistic", "Pessimistic", "Tired", "Bored", "Excited"]
    
            accb = Button(canvas, text='''War Mode
Minigame''', font=('Belwe Cn BT', 15), anchor=W, command=drawacc)
            accb.place(relx=.655, rely=.84)

            up = Button(canvas, text='''Update Kingdom
Status
(Ticker Tape)''', font=('Belwe Cn BT', 15), anchor=W, command=update)
            up.place(relx=.775, rely=.84)
            wum = Button(canvas, text='''What's Up,
Casey?''', font=('Belwe Cn BT', 15), command=randmurph)#, anchor=W)
            wum.place(relx=.345, rely=.84)
            canvas.create_image(0, 467, anchor=W, image=whitespace_room)
            details["News"] = "News: " + news[random.randint(0, 7)] + ", Weather: " + wx[random.randint(0, 9)] + ", Citizens feel: " + people[random.randint(0, 13)] + ", Approval rating: " + str(random.randint(60, 100)) + "%, Bacon Vault: Empty :("
            canvas.create_text(390, 460, text=details["News"], font=('Belwe Cn BT', 12))
            
            dothing = Button(canvas, text='''Casey's Voice
On/Off''', font=('Belwe Cn BT', 15), anchor=W, command=toggle)
            dothing.place(relx=.775, rely=.6)
            
            if details["f1"] == 'y':
                frame = f1p
            elif details["f2"] == 'y':
                frame = f2p
            elif details["f3"] == 'y':
                frame = f3p
            else:
                details["new"] = True
                z = randint(1, 3)
                y = str('f') + str(z)
                details[y] = 'y'
                drawroomt(x)
                return None
            y = x
            canvas.create_image(680, 70, image=frame)
            canvas.create_image(680, 185, image=frame)
            canvas.create_text(680, 50, text="Money:", font=('Belwe Cn BT', 18))
            temp["money"] = canvas.create_text(680, 70, text=details["money"], font=('Belwe Cn BT', 14))
            canvas.create_text(680, 165, text="Lives:", font=('Belwe Cn BT', 18))
            canvas.create_text(680, 185, text=details["lives"], font=('Belwe Cn BT', 14))
            if details["person"] == True:
                canvas.create_image(100, 400, image=person, anchor=S)
            if details["new"] == True:
                x = simpledialog.askstring("Welcome!", '''Welcome to your Kingdom! You are now the
Ruler of a vast land. I am your advisor,
Casey Robertson! Your Kingdom is not yet
named. What is your Kingdom's name?''')
                if x == None:
                    resetdetail()
                    drawmain()
                    return None
                details["user"] = x
                instruct()
                if uname()[0] == 'Linux' or uname()[0] == 'Darwin':
                    user = getuser()
                    initit = str('/home/') + str(user) + str('/Public/uthronium/') + str(details["user"]) + str('.utr')
                else:
                    if debug["os"] == True:
                        initit = str("C:\\Documents and settings\\all users\\Documents\\uthronium\\") + str(details["user"]) + str('.utr')
                    else:
                        initit = str("C:\\users\\public\\Documents\\uthronium\\") + str(details["user"]) + str('.utr')
                temp["user"] = initit
            
                
            details["new"] = False
            
    except Exception:
        er(format_exc())
def guesta():
    x = messagebox.askyesno("Confirmation Recquired", "Are you sure? Changes cannot be saved in the Guest account!")
    if x:
        drawroomt(False)
def drawroomf():
    drawroomt(None)
def drawmain():
    try:
        drawcan()
        status('drawmain')
        statusbar("Drawing Login Screen")
        
        
        canvas.create_rectangle(0, 0, 800, 600, fill="#D7423C")
        #canvas.create_image(0, 0, anchor=NW, image=test)
        login = Button(root, text="Open Existing Kingdom", command=load_kingdom)
        login.place(relx=.335, rely=.4)
        new = Button(root, text='''Create New Kingdom
(New Users Click Here)''', command=create_king)
        new.place(relx=.535, rely=.4)
        
        canvas.create_text(400, 150, text="Welcome to uThronium!", font=('Belwe Cn BT', 48), fill='white')
        canvas.create_text(400, 350, text="Press a button to begin your adventure.", font=('Belwe Cn BT', 20), fill='white')
        
    except Exception:
        er(format_exc())

def killme2():
    try:
        x = randint(0, 100)
        if x > 70 and details["kill2"] == True:
            voice("Remember how earlier you declined to replace the carbon manoxide alarms? Well, the heating system doesn't seem to be working and I feel a bit drowsy")
            messagebox.showwarning("Death Alert", "Remember how earlier you declined to replace the carbon manoxide alarms? Well, the heating system doesn't seem to be working and I feel a bit drowsy..............................")
            exit_save_death()
    except Exception:
        er(format_exc())
def ex():
    root.destroy()
def drawtr(x):
    try:
        y = False
        for z in range(0, 7):
            if details[str('tr') + str(z)] == 'y':
                y = True
        temp["room"] = y
        #This to make background image
        canvas.create_image(0, 0, anchor=NW, image=x)
    except Exception:
        er(format_exc())
def drawroom323():
    if debug["status"] != 'color':
        drawroom()
    else:
        statusbar('Waiting for password...')
        messagebox.showerror("Enter Password", "Please enter your color password and press \"Go\".")
def resetdetail():
    #reset details map to original state
    try:
        details["money"] = 0
        details["lives"] = 1
        details["user"] = None
        details["tr0"] = False
        details["tr1"] = False
        details["tr2"] = False
        details["tr3"] = False
        details["tr4"] = False
        details["tr5"] = False
        details["tr6"] = False
        details["person"] = False
        details["f1"] = False
        details["f2"] = False
        details["f3"] = False
        details["kill"] = False
        details["kill2"] = False
        details["pass"] = None
        details["colorpass"] = None
        details["new"] = False
        details["messenger"] = False
    except Exception:
        er(format_exc())
try:
    global heythere
    global a
    a = True
    heythere = 0
    #defining details and debug maps
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
    "new" : False,
    "murph" : 0,
    "messenger" : False,
    "News" : "Error: Latest Happenings is not working."
    }
    debug = {
    "status" : "load.modules",
    "answer" : None,
    "os" : None,
    "bit" : None,
    "version" : 0.0
    }
    passtemp = {
    "setup" : None,
    "pass" : "",
    "colors" : ""
    }
    #importing modules and commands
    
    
    root = Tk()
    root.update()
    root.update_idletasks()
    w = 800
    h = 620
    if uname()[0] == 'Linux' or uname()[0] == 'Darwin':
        h = 600
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2) - 32
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    root.title("uThronium - Version 1.0")
    
    root.resizable(0, 0)
    
    def drawcan():
        canvas.destroy()
        firstdrawcan()
    def firstdrawcan():
        global canvas
        canvas = Canvas(root, width=800, height=600, bd=0, highlightthickness=0)
        canvas.pack()
        canvas.create_text(400, 300, text="uhoh", font=('Belwe Cn BT', 72))
    def newinhere():
        statusbar("New In This Version...")
        messagebox.showinfo("New In This Version", '''New In This Version of uThronium (as opposed to uThrone):

Everything....this is the first release! :)
''')
    def cheatcall(event):
        sprint(event)
        if debug["status"] != 'color' and debug["status"] != 'pass':
            cheat()
        else:
            messagebox.showerror("Enter Password", "The cheat box cannot be opened while entering a password.")
    
    firstdrawcan()
    statusb = Label(root, text="status bar", bd=1, relief=SUNKEN, anchor=W)
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New...Ctrl+N", command=create_king)
    filemenu.add_command(label="Open...Ctrl+O", command=load_kingdom)
    filemenu.add_command(label="Save...Ctrl+S", command=exit_save)
    filemenu.add_separator()
    actionmenu = Menu(menu)
    menu.add_cascade(label="Action", menu=actionmenu)
    actionmenu.add_command(label="What's Up, Casey?...Ctrl+Alt+M", command=randmurph)
    actionmenu.add_separator()
    actionmenu.add_command(label="War Mode...Ctrl+Alt+W", command=warm)
    
    placemenu = Menu(menu)
    menu.add_cascade(label="Go To", menu=placemenu)
    placemenu.add_command(label="Store...Alt+S", command=drawstore)
    placemenu.add_command(label="Games...Alt+A", command=drawacc)
    placemenu.add_separator()
    placemenu.add_command(label="Throne Room...Home", command=drawroom323)
    placemenu.add_command(label="Login Screen...Alt+L", command=drawmain)
    filemenu.add_command(label="Exit...Alt+F4", command=ex)
    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)


 
    helpmenu.add_command(label="About...F2", command=aboutit)
    
    setup()
    
    if setu == True:
        #Comment below line when compiling with cx_Freeze
        debug["bit"] = None
        statusbar('Loading images...')
        if uname()[0] != 'Linux':
            if debug["bit"] == None:
                root.iconbitmap(default='uthronium.ico')
                bit = ""
            elif debug["bit"] == True:
                root.iconbitmap(default='C:\\program files\\uThronium\\uthronium.ico')
                bit= "C:\\program files\\uThronium\\"
            else:
                root.iconbitmap(default='C:\\program files (x86)\\uThronium\\uthronium.ico')
                bit= "C:\\program files (x86)\\uThronium\\"
            if debug["bit"] == None:
                abc = ""
            elif debug["bit"] == True:
                abc = "C:\\program files\\uThronium\\"
            else:
                abc = "C:\\program files (x86)\\uThronium\\"
            abc="C:\\users\\tobias\\documents\\python\\uthronium\\"
            tr1f = PhotoImage(file=str(abc) + str('1.gif'))
            tr2f = PhotoImage(file=str(abc) + str('2.gif'))
            tr3f = PhotoImage(file=str(abc) + str("tr3f.gif"))
            tr4f = PhotoImage(file=str(abc) + str('4.gif'))
            tr5f = PhotoImage(file=str(abc) + str("tr5f.gif"))
            tr6f = PhotoImage(file=str(abc) + str("tr6f.gif"))
            f1 = PhotoImage(file=str(abc) + str("f1.gif"))
            f2 = PhotoImage(file=str(abc) + str("f2.gif"))
            f3 = PhotoImage(file=str(abc) + str("f3.gif"))
            fprev = f3
            
            trprev = PhotoImage(file=str(abc) + str("trprev.gif"))
            fp5 = trprev
            puz = PhotoImage(file=str(abc) + str("puz.gif"))
            fp1 = PhotoImage(file=str(abc) + str('1c.gif'))
            fp2 = PhotoImage(file=str(abc) + str('2c.gif'))
            fp3 = PhotoImage(file=str(abc) + str('fp3.gif'))
            fp4 = PhotoImage(file=str(abc) + str('4c.gif'))
            fp6 = PhotoImage(file=str(abc) + str('fp6.gif'))
            f1p = f1
            f2p = f2
            f3p = f3
            whitespace_room = PhotoImage(file=str(abc) + str('whitespace_room.gif'))
            person = PhotoImage(file=str(abc) + str('person.gif'))
            personprev = PhotoImage(file=str(abc) + str('personprev.gif'))
            other = personprev
            
        else:
            debug["bit"] = None
            abc = ""
            abc="C:\\users\\tobias\\documents\\python\\uthronium\\"
            tr1f = PhotoImage(file=str(abc) + str('1.gif'))
            tr2f = PhotoImage(file=str(abc) + str('2.gif'))
            tr3f = PhotoImage(file=str(abc) + str("tr3f.gif"))
            tr4f = PhotoImage(file=str(abc) + str('4.gif'))
            tr5f = PhotoImage(file=str(abc) + str("tr5f.gif"))
            tr6f = PhotoImage(file=str(abc) + str("tr6f.gif"))
            f1 = PhotoImage(file=str(abc) + str("f1.gif"))
            f2 = PhotoImage(file=str(abc) + str("f2.gif"))
            f3 = PhotoImage(file=str(abc) + str("f3.gif"))
            fprev = f3
            
            trprev = PhotoImage(file=str(abc) + str("trprev.gif"))
            fp5 = trprev
            puz = PhotoImage(file=str(abc) + str("puz.gif"))
            fp1 = PhotoImage(file=str(abc) + str('1c.gif'))
            fp2 = PhotoImage(file=str(abc) + str('2c.gif'))
            fp3 = PhotoImage(file=str(abc) + str('fp3.gif'))
            fp4 = PhotoImage(file=str(abc) + str('4c.gif'))
            fp6 = PhotoImage(file=str(abc) + str('fp6.gif'))
            f1p = f1
            f2p = f2
            f3p = f3
            whitespace_room = PhotoImage(file=str(abc) + str('whitespace_room.gif'))
            person = PhotoImage(file=str(abc) + str('person.gif'))
            personprev = PhotoImage(file=str(abc) + str('personprev.gif'))
            other = personprev
            b64 = None
        drawmain()
        
        statusbar("Welcome to uThronium!")
        def create_king_k(s):
            create_king()
        def load_kingdom_k(s):
            load_kingdom()
        def exit_save_k(s):
            exit_save()
        def drawstore_k(s):
            drawstore()
        def drawacc_k(s):
            drawacc()
        def drawroom_k(s):
            drawroom323()
        def drawmain_k(s):
            drawmain()
        def randmurph_k(s):
            randmurph()
        def warm_k(s):
            sprint('warm')
            warm()
       
        def instruct_k(s):
            instruct()
        def aboutit_k(s):
            aboutit()
        def newinhere_k(s):
            newinhere()
        canvas.bind_all('<Control-A>', cheatcall)
        
        temp = {
            'guest' : False,
            'shutdown' : False,
            'user' : None,
            'money' : None,
            'room' : False
            }
        root.protocol('WM_DELETE_WINDOW', closewin)
        root.mainloop()
    else:
        root.destroy()
except Exception:
    er(format_exc())
