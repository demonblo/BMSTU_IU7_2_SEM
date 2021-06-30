from tkinter import *
from tkinter.messagebox import *
root = Tk()
#Размер проги
root.geometry("610x500")
root.resizable(width=False, height=False)
root.title("Calculator")

#Функции добавления символов в поля ввода
def add1(event):
    press('1')
def add2(event):
    press('2')
def add3(event):
    press('3')
def add4(event):
    press('4')
def add5(event):
    press('5')
def add6(event):
    press('6')
def add7(event):
    press('7')
def add8(event):
    press('8')
def add9(event):
    press('9')
def addA(event):
    press('A')
def addB(event):
    press('B')
def addC(event):
    press('C')
def addD(event):
    press('D')
def addE(event):
    press('E')
def addF(event):
    press('F')
def addDot(event):
    press('.')
def add0(event):
    press('0')

def press(symb):
    Entry_1.insert(END,symb)

#Функция Del
def Del(event):
    Entry_1.delete(len(Entry_1.get()) - 1)

#Функция Reset
def Reset(event):
    Entry_1.delete(0, 'end')
    Label_2['text'] = ''
def Reseted():
    Entry_1.delete(0, 'end')
    Label_2['text'] = ''

#Функция Calculate
def Calculate(event):
    Input = Entry_1.get()
    Output=[]
    OutputTXT=''
    Counter = Input.count('.')
#Обработка целых 10 чисел
    if  var.get() == 1 and Counter == 0:
        try:
            Input = int(Input)
            while Input != 0:
                if Input % 16 == 10:
                    Output.append('A')
                elif Input % 16 == 11:
                    Output.append('B')
                elif Input % 16 == 12:
                    Output.append('C')
                elif Input % 16 == 13:
                    Output.append('D')
                elif Input % 16 == 14:
                    Output.append('E')
                elif Input % 16 == 15:
                    Output.append('F')
                else:
                    Output.append(Input % 16)
                Input = Input // 16
            for i in range(len(Output)-1, -1, -1):
                OutputTXT += str(Output[i])
            Label_2['text'] = OutputTXT
        except ValueError:
            Label_2['text'] = 'Некорректный ввод!!!'
            
#Обработка дробных 10 чисел
    if  var.get() == 1 and Counter == 1:
        #Обработка целой части
        try:
            Ch = float(Input)
            Input=str(Input)
            Input = Input.split('.')
            Cel = int(Input[0])
            while Cel != 0:
                if Cel % 16 == 10:
                    Output.append('A')
                elif Cel % 16 == 11:
                    Output.append('B')
                elif Cel % 16 == 12:
                    Output.append('C')
                elif Cel % 16 == 13:
                    Output.append('D')
                elif Cel % 16 == 14:
                    Output.append('E')
                elif Cel % 16 == 15:
                    Output.append('F')
                else:
                    Output.append(Cel % 16)
                Cel = Cel // 16
            for i in range(len(Output)-1, -1, -1):
                OutputTXT += str(Output[i])
        except ValueError:
            Label_2['text'] = 'Некорректный ввод!!!'
        #Обработка дробной части
        OutputTXT += '.'
        Drob = float(int(Input[1]) / 10**len(Input[1]))
        for i in range (4):
            Drob *= 16
            if int(Drob // 1) <= 9:
                OutputTXT += str(int(Drob // 1))
            elif int(Drob // 1) == 10:
                OutputTXT += 'A'
            elif int(Drob // 1) == 11:
                OutputTXT += 'B'
            elif int(Drob // 1) == 12:
                OutputTXT += 'C'
            elif int(Drob // 1) == 13:
                OutputTXT += 'D'
            elif int(Drob // 1) == 14:
                OutputTXT += 'E'
            elif int(Drob // 1) == 15:
                OutputTXT += 'F'
            Drob = Drob - (Drob // 1)
        #Вывод
        Label_2['text'] = OutputTXT
#Больше 1 точки!!!
    elif Counter > 1:
        Label_2['text'] = 'Некорректный ввод!!!'   
#Обработка целых 16 чисел
    elif var.get() == 2 and Counter == 0:
        STEP = len(Input) - 1
        Output = 0
        for i in Input:
            if '0' <= i <= '9':
                Output += int(i) * (16**STEP)
            elif i=='A' or i == 'a':
                Output += 10 * (16**STEP)
            elif i=='B' or i == 'b':
                Output += 11 * (16**STEP)
            elif i=='C' or i == 'c':
                Output += 12 * (16**STEP)
            elif i=='D' or i == 'd':
                Output += 13 * (16**STEP)
            elif i=='E' or i == 'e':
                Output += 14 * (16**STEP)
            elif i=='F' or i == 'f':
                Output += 15 * (16**STEP)
            else:
                Output = 'Некорректный ввод!!!'
                break
            STEP -= 1
        OutputTXT = str(Output)
        Label_2['text'] = OutputTXT
#Обработка дробных 16 чисел
    elif var.get() == 2 and Counter == 1:
        
        Output = 0
        Input=str(Input)
        Input = Input.split('.')
        Cel = Input[0]
        Drob = Input[1]
        STEP = len(Cel) - 1
        for i in Cel:
            if '0' <= i <= '9':
                Output += int(i) * (16**STEP)
            elif i=='A' or i == 'a':
                Output += 10 * (16**STEP)
            elif i=='B' or i == 'b':
                Output += 11 * (16**STEP)
            elif i=='C' or i == 'c':
                Output += 12 * (16**STEP)
            elif i=='D' or i == 'd':
                Output += 13 * (16**STEP)
            elif i=='E' or i == 'e':
                Output += 14 * (16**STEP)
            elif i=='F' or i == 'f':
                Output += 15 * (16**STEP)
            else:
                Output = 'Некорректный ввод!!!'
                break
            STEP -= 1
        for i in Drob:
            if '0' <= i <= '9':
                Output += int(i) * (16**STEP)
            elif i=='A' or i == 'a':
                Output += 10 * (16**STEP)
            elif i=='B' or i == 'b':
                Output += 11 * (16**STEP)
            elif i=='C' or i == 'c':
                Output += 12 * (16**STEP)
            elif i=='D' or i == 'd':
                Output += 13 * (16**STEP)
            elif i=='E' or i == 'e':
                Output += 14 * (16**STEP)
            elif i=='F' or i == 'f':
                Output += 15 * (16**STEP)
            else:
                Output = 'Некорректный ввод!!!'
                break
            STEP -= 1
        OutputTXT = str(Output)
        Label_2['text'] = OutputTXT
 #Не выбран тип перевода
    if var.get() == 0:
        Label_2['text'] = 'Выбирите тип перевода!'

def Calculated():
    Input = Entry_1.get()
    Output=[]
    OutputTXT=''
    Counter = Input.count('.')
#Обработка целых 10 чисел
    if  var.get() == 1 and Counter == 0:
        try:
            Input = int(Input)
            while Input != 0:
                if Input % 16 == 10:
                    Output.append('A')
                elif Input % 16 == 11:
                    Output.append('B')
                elif Input % 16 == 12:
                    Output.append('C')
                elif Input % 16 == 13:
                    Output.append('D')
                elif Input % 16 == 14:
                    Output.append('E')
                elif Input % 16 == 15:
                    Output.append('F')
                else:
                    Output.append(Input % 16)
                Input = Input // 16
            for i in range(len(Output)-1, -1, -1):
                OutputTXT += str(Output[i])
            Label_2['text'] = OutputTXT
        except ValueError:
            Label_2['text'] = 'Некорректный ввод!!!'
            
#Обработка дробных 10 чисел
    if  var.get() == 1 and Counter == 1:
        #Обработка целой части
        try:
            Ch = float(Input)
            Input=str(Input)
            Input = Input.split('.')
            Cel = int(Input[0])
            while Cel != 0:
                if Cel % 16 == 10:
                    Output.append('A')
                elif Cel % 16 == 11:
                    Output.append('B')
                elif Cel % 16 == 12:
                    Output.append('C')
                elif Cel % 16 == 13:
                    Output.append('D')
                elif Cel % 16 == 14:
                    Output.append('E')
                elif Cel % 16 == 15:
                    Output.append('F')
                else:
                    Output.append(Cel % 16)
                Cel = Cel // 16
            for i in range(len(Output)-1, -1, -1):
                OutputTXT += str(Output[i])
        except ValueError:
            Label_2['text'] = 'Некорректный ввод!!!'
        #Обработка дробной части
        OutputTXT += '.'
        Drob = float(int(Input[1]) / 10**len(Input[1]))
        for i in range (4):
            Drob *= 16
            if int(Drob // 1) <= 9:
                OutputTXT += str(int(Drob // 1))
            elif int(Drob // 1) == 10:
                OutputTXT += 'A'
            elif int(Drob // 1) == 11:
                OutputTXT += 'B'
            elif int(Drob // 1) == 12:
                OutputTXT += 'C'
            elif int(Drob // 1) == 13:
                OutputTXT += 'D'
            elif int(Drob // 1) == 14:
                OutputTXT += 'E'
            elif int(Drob // 1) == 15:
                OutputTXT += 'F'
            Drob = Drob - (Drob // 1)
        #Вывод
        Label_2['text'] = OutputTXT
#Больше 1 точки!!!
    elif Counter > 1:
        Label_2['text'] = 'Некорректный ввод!!!'   
#Обработка целых 16 чисел
    elif var.get() == 2 and Counter == 0:
        STEP = len(Input) - 1
        Output = 0
        for i in Input:
            if '0' <= i <= '9':
                Output += int(i) * (16**STEP)
            elif i=='A' or i == 'a':
                Output += 10 * (16**STEP)
            elif i=='B' or i == 'b':
                Output += 11 * (16**STEP)
            elif i=='C' or i == 'c':
                Output += 12 * (16**STEP)
            elif i=='D' or i == 'd':
                Output += 13 * (16**STEP)
            elif i=='E' or i == 'e':
                Output += 14 * (16**STEP)
            elif i=='F' or i == 'f':
                Output += 15 * (16**STEP)
            else:
                Output = 'Некорректный ввод!!!'
                break
            STEP -= 1
        OutputTXT = str(Output)
        Label_2['text'] = OutputTXT
#Обработка дробных 16 чисел
    elif var.get() == 2 and Counter == 1:
        
        Output = 0
        Input=str(Input)
        Input = Input.split('.')
        Cel = Input[0]
        Drob = Input[1]
        STEP = len(Cel) - 1
        for i in Cel:
            if '0' <= i <= '9':
                Output += int(i) * (16**STEP)
            elif i=='A' or i == 'a':
                Output += 10 * (16**STEP)
            elif i=='B' or i == 'b':
                Output += 11 * (16**STEP)
            elif i=='C' or i == 'c':
                Output += 12 * (16**STEP)
            elif i=='D' or i == 'd':
                Output += 13 * (16**STEP)
            elif i=='E' or i == 'e':
                Output += 14 * (16**STEP)
            elif i=='F' or i == 'f':
                Output += 15 * (16**STEP)
            else:
                Output = 'Некорректный ввод!!!'
                break
            STEP -= 1
        for i in Drob:
            if '0' <= i <= '9':
                Output += int(i) * (16**STEP)
            elif i=='A' or i == 'a':
                Output += 10 * (16**STEP)
            elif i=='B' or i == 'b':
                Output += 11 * (16**STEP)
            elif i=='C' or i == 'c':
                Output += 12 * (16**STEP)
            elif i=='D' or i == 'd':
                Output += 13 * (16**STEP)
            elif i=='E' or i == 'e':
                Output += 14 * (16**STEP)
            elif i=='F' or i == 'f':
                Output += 15 * (16**STEP)
            else:
                Output = 'Некорректный ввод!!!'
                break
            STEP -= 1
        OutputTXT = str(Output)
        Label_2['text'] = OutputTXT
 #Не выбран тип перевода
    if var.get() == 0:
        Label_2['text'] = 'Выбирите тип перевода!'

#Функция About
def About(event):
    showinfo('About Progrma','Данная програма переводит числа \nиз 10-ой системы счисления в 16-ую и наоборот.\nПрграмма разработана студентом ИУ-7 группы 22 Б Дмитрием Блохиным.')
def Abouted():
    showinfo('About Progrma','Данная програма переводит числа \nиз 10-ой системы счисления в 16-ую и наоборот.\nПрграмма разработана студентом ИУ-7 группы 22 Б Дмитрием Блохиным.')

#Menu
main_menu = Menu(root)
root.configure(menu=main_menu, bg='blue')
main_menu.add_command(label='Calculate', command=Calculated)
main_menu.add_command(label='Reset', command=Reseted)
main_menu.add_command(label='About program', command=Abouted)

#Frames
left_frame = Frame(root, width=250, heigh=400, bg='grey')
right_frame = Frame(root, width=250, heigh=400, bg='grey')
left_frame.place(x=30, y= 30)
right_frame.place(x=330, y=30)

#Ввод Вывод
Entry_1 = Entry(left_frame, width=10)
Entry_1.place(x=80, y=50)
Label_1 = Label(left_frame, width=8, text='Ввод', bg='grey',font=('UBUNTU',10))
Label_1.place(x=10, y=50)

Label_3 = Label(left_frame, width=8, text='Вывод', bg='grey',font=('UBUNTU',10))
Label_3.place(x=10, y=100)
Label_2 = Label(left_frame, width=15, heigh=1, bg='white' )
Label_2.place(x=80, y=100)

#Кнопка Del
Button_Del = Button(left_frame, text='Del',width=5,heigh=1)
Button_Del.place(x=183,y=47)
Button_Del.bind('<Button-1>', Del)

#Кнопки справа
Button_1 = Button(right_frame, text='Calculate',width=15,heigh=3)
Button_1.place(x=70,y=80)
Button_1.bind('<Button-1>', Calculate)

Button_2 = Button(right_frame, text='Reset',width=15,heigh=3)
Button_2.place(x=70,y=180)
Button_2.bind('<Button-1>', Reset)

Button_3 = Button(right_frame, text='About program',width=15,heigh=3)
Button_3.place(x=70,y=280)
Button_3.bind('<Button-1>', About)


#From 10 to 16 and 16 to 10
var=IntVar()
var.set(0)
rbutton_1=Radiobutton(left_frame,text='from 10 to 16',variable=var,value=1)
rbutton_2=Radiobutton(left_frame,text='ftom 16 to 10',variable=var,value=2)


rbutton_1.place(x=30, y=340)
rbutton_2.place(x=30, y=360)

#Первая линия цифр
button_one = Button(left_frame, text='1',width=5,heigh=2)
button_one.place(x=30,y=135)
button_one.bind('<Button-1>', add1)

button_two = Button(left_frame, text='2',width=5,heigh=2)
button_two.place(x=80,y=135)
button_two.bind('<Button-1>', add2)

button_three = Button(left_frame, text='3',width=5,heigh=2)
button_three.place(x=130,y=135)
button_three.bind('<Button-1>', add3)

button_four = Button(left_frame, text='4',width=5,heigh=2)
button_four.place(x=180,y=135)
button_four.bind('<Button-1>', add4)
#Вторая линия цифр
button_five = Button(left_frame, text='5',width=5,heigh=2)
button_five.place(x=30,y=185)
button_five.bind('<Button-1>', add5)

button_six = Button(left_frame, text='6',width=5,heigh=2)
button_six.place(x=80,y=185)
button_six.bind('<Button-1>', add6)

button_seven = Button(left_frame, text='7',width=5,heigh=2)
button_seven.place(x=130,y=185)
button_seven.bind('<Button-1>', add7)

button_eight = Button(left_frame, text='8',width=5,heigh=2)
button_eight.place(x=180,y=185)
button_eight.bind('<Button-1>', add8)

#Третья линия цифр и букв
button_five = Button(left_frame, text='9',width=5,heigh=2)
button_five.place(x=30,y=235)
button_five.bind('<Button-1>', add9)

button_six = Button(left_frame, text='A',width=5,heigh=2)
button_six.place(x=80,y=235)
button_six.bind('<Button-1>', addA)

button_seven = Button(left_frame, text='B',width=5,heigh=2)
button_seven.place(x=130,y=235)
button_seven.bind('<Button-1>', addB)

button_eight = Button(left_frame, text='C',width=5,heigh=2)
button_eight.place(x=180,y=235)
button_eight.bind('<Button-1>', addC)

#Четвертая линия цифр и букв
button_five = Button(left_frame, text='D',width=5,heigh=2)
button_five.place(x=30,y=285)
button_five.bind('<Button-1>', addD)

button_six = Button(left_frame, text='E',width=5,heigh=2)
button_six.place(x=80,y=285)
button_six.bind('<Button-1>', addE)

button_seven = Button(left_frame, text='F',width=5,heigh=2)
button_seven.place(x=130,y=285)
button_seven.bind('<Button-1>', addF)

button_eight = Button(left_frame, text='0',width=5,heigh=2)
button_eight.place(x=180,y=285)
button_eight.bind('<Button-1>', add0)

button_nine = Button(left_frame, text='.',width=5,heigh=2)
button_nine.place(x=180,y=335)
button_nine.bind('<Button-1>', addDot)




root.mainloop()
