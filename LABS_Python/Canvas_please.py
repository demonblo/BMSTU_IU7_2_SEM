from math import *
from tkinter import *
from random import *

global counter

counter = 0
global Dots
Dots = []
for i in range(25):
    Dots.append([])
    Dots[i].append(0)
    Dots[i].append(0)
global Circles
Circles = []
for i in range(10):
    Circles.append([])
    Circles[i].append(0)
    Circles[i].append(0)
    Circles[i].append(0)


root = Tk()
root.geometry("1200x700")
root.resizable(width=False, height=False)
root.configure(bg='cyan4')

c_1 = Canvas(root, width=700, height=700, cursor="pencil", bg="white")
c_1.place(x=500, y=0)

def Randomize(Event):
    global Dots
    global Circles
    print("lol ", Dots)
    c_1 = Canvas(root, width=700, height=700, cursor="pencil", bg="white")
    c_1.place(x=500, y=0)
    
    for i in range(25):
        Dots[i][0] = (randint(-25, 25) * 7 + 350)
        Dots[i][1] = (randint(-25, 25) * 7 + 350)

    for i in range(10):
        Circles[i][0] = (randint(-25, 25) * 7 + 350)
        Circles[i][1] = (randint(-25, 25) * 7 + 350)
        Circles[i][2] = (randint(1, 5) * 7)

    c_1.create_line(350, 0, 350, 700, width=1, fill="black")
    c_1.create_line(0, 350, 700, 350, width=1, fill="black")
    
    for i in range(len(Dots)):
        c_1.create_oval(Dots[i][0] - 1, Dots[i][1] - 1, Dots[i][0] + 2, Dots[i][1] + 2, width=1, fill="black")

    for i in range(len(Circles)):
        c_1.create_oval(Circles[i][0] - Circles[i][2] , Circles[i][1] - Circles[i][2], Circles[i][0] + Circles[i][2], Circles[i][1] + Circles[i][2], width=1)

def Clear(Event):
    global Dots
    global Circles
    for i in range(25):
        Dots[i][0] = 0
        Dots[i][1] = 0
    for i in range(10):
        Circles[i][0] = 0
        Circles[i][1] = 0
        Circles[i][2] = 0
        

Button_1 = Button(root, text='Randomize',width=15,heigh=3)
Button_1.place(x=70,y=580)
Button_1.bind('<Button-1>', Randomize)

Button_2 = Button(root, text='Clear Dots',width=15,heigh=3)
Button_2.place(x=170,y=580)
Button_2.bind('<Button-1>', Clear)





