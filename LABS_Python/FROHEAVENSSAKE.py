from tkinter import *
from tkinter.messagebox import *
root = Tk()
#Размер проги
root.geometry("610x500")
root.resizable(width=False, height=False)
root.title("Calculator")
root.configure(bg="BLUE")
#Функция Calculate
def calculate(event):
    first = Entry_1.get()
    second = Entry_2.get()
    action = Entry_3.get()

    F = []
    S = []
    answer = []
    ost = 0
    znak1 = 0
    znak2 = 0
    znak3 = 0
    znak4 = 0

    #Определение знака и перенос чисел в массивы
    for i in first:
        if i != '-':
            F.append(int(i))
        else:
            znak1 = 1
    for i in second:
        if i != '-':
            S.append(int(i))
        else:
            znak2 = 1

    

    #Определение размера чисел
    if len(S) < len(F):
        for i in range(len(F) - len(S)):
            S.insert(0, 0)
    else:
        for i in range(len(S) - len(F)):
            F.insert(0, 0)
    if znak1 == 1 and znak2 == 0 and action == '+':
        F, S = S, F
        first, second = second, first
        action = '-'
    elif znak1 == 0 and znak2 == 1 and action == '-':
        action = '+'
    elif znak1 == 1 and znak2 == 1 and action == '+':
        znak3 = 1
    elif znak1 == 1 and znak2 == 0 and action == '-':
        znak3 = 1
        action = '+'
    elif znak1 == 1 and znak2 == 1 and action == '-':
        F, S = S, F
        first, second = second, first
    elif znak1 == 0 and znak2 == 1 and action == '+':
        action = '-'

    first = abs(int(first))
    second = abs(int(second))

    if second > first:
        znak4 = 1
    
    if action == '+':
        for i in range(len(F) - 1, -1, -1):
            answer.insert(0, (F[i] + S[i]  + ost)% 3)
            ost = (F[i] + S[i] + ost) // 3
        if ost != 0:
            answer.insert(0, ost)
    
    elif action == '-':
        if znak4 == 1:
            F, S = S, F
            znak3 = 1
        for i in range(len(F) - 1, -1, -1):
            if F[i] <= 0 and ost != 0:
                F[i] = 2
                F[i - 1] -= 1
            else :
                F[i] = F[i] - ost
                
            if F[i] - S[i] >= 0:
                answer.insert(0, F[i] - S[i])
                ost = 0
            elif F[i] - S[i] < 0:
                answer.insert(0, 3 + (F[i] - S[i]))
                ost = 1

                
            
                
                
    OutputTXT = ''
    if znak3 == 1:
        OutputTXT += '-'
    for i in answer:
        OutputTXT += str(i)

        

    Label_5['text'] = OutputTXT
    
#Frames
left_frame = Frame(root, width=550, heigh=400, bg='grey')

left_frame.place(x=30, y= 30)


Entry_1 = Entry(left_frame, width=10)
Entry_1.place(x=80, y=50)
Label_1 = Label(left_frame, width=8, text='1 число', bg='grey',font=('UBUNTU',10))
Label_1.place(x=100, y=30)

Entry_2 = Entry(left_frame, width=10)
Entry_2.place(x=260, y=50)
Label_2 = Label(left_frame, width=8, text='2 число', bg='grey',font=('UBUNTU',10))
Label_2.place(x=270, y=30)

Entry_3 = Entry(left_frame, width=3)
Entry_3.place(x=200, y=50)
Label_3 = Label(left_frame, width=8, text='Действие', bg='grey',font=('UBUNTU',10))
Label_3.place(x=190, y=30)


Label_4 = Label(left_frame, width=8, text='Ответ', bg='grey',font=('UBUNTU',10))
Label_4.place(x=10, y=100)


Button_1 = Button(left_frame, text='Calculate',width=10,heigh=2)
Button_1.place(x=270,y=90)
Button_1.bind('<Button-1>', calculate)

Label_5 = Label(left_frame, width=20, heigh=1, bg='white', font=('UBUNTU',10) )
Label_5.place(x=80, y=100)

root.mainloop()
