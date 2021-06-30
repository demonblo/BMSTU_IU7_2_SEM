from tkinter import *
from tkinter.messagebox import *


root = Tk()

# Справка
def info(event):
    information = 'Данная программа формирует таблицу корней функции f(x) = 2^(x - 1) - 1.47 на отрезке [a, b] с шагом h и точностью eps, которые вводятся пользователем.'
    showinfo('Информация о программе', information)

def info_01():
    information = 'Данная программа формирует таблицу корней функции f(x) = 2^(x - 1) - 1.47 на отрезке [a, b] с шагом h и точностью eps, которые вводятся пользователем.'

    showinfo('Информация о программе', information)
    
def f(x):
    y = 2 ** (x - 1) - 1.47

    return y

#Calculate
def Calculate(event):
    a = input_a.get()
    b = input_b.get()
    h = input_h.get()
    eps = input_eps.get()
    print(a)
    print(b)
    print(h)
    print(eps)

    try:
        a = float(a)
        b = float(b)
        h = float(h)
        eps = float(eps)

        if h > b - a or h <= 0 or b <= a or (f(a) > 0 and f(b) > 0) or (f(a) < 0 and f(b) < 0):
            showwarning('Ошибка!','Некорректный ввод!')
        else:
            print("красава")
            
            
    except ValueError :
        showwarning('ОШибка!','Некорректный ввод!')
        
    
#Размер проги
root.geometry("640x600")
root.resizable(width=False, height=False)
root.title("Сортировки")
root.configure(bg="cyan4")

#Frame
left_frame = Frame(root, width=580, height=550, bg='white')
left_frame.place(x=30, y= 30)

#Input
label_input_from = Label(left_frame, width=10, text='Отрезок от', height=2, bg='white')
label_input_from.place(x=20, y=20)
input_a = Entry(left_frame, width=6)
input_a.place(x=110, y=25)

label_input_to = Label(left_frame, width=2, text='до', height=2, bg='white')
label_input_to.place(x=185, y=20)
input_b = Entry(left_frame, width=6)
input_b.place(x=215, y=25)

label_input_h = Label(left_frame, width=5, text='  Шаг =', height=2, bg='white')
label_input_h.place(x=290, y=20)
input_h = Entry(left_frame, width=6)
input_h.place(x=350, y=25)

label_input_eps = Label(left_frame, width=5, text='  eps =', height=2, bg='white')
label_input_eps.place(x=420, y=20)
input_eps = Entry(left_frame, width=6)
input_eps.place(x=480, y=25)


#Справка
Button_info = Button(left_frame, text='Справка',width=10,heigh=2)
Button_info.place(x=465,y=60)
Button_info.bind('<Button-1>', info)

Button_info = Button(left_frame, text='Calculate',width=10,heigh=2)
Button_info.place(x=465,y=60)
Button_info.bind('<Button-1>', Calculate)

#Menu
main_menu = Menu(root)
root.configure(menu=main_menu)

first_item = Menu(main_menu)
main_menu.add_cascade(label="Commands", menu = first_item)
first_item.add_command(label="Info", command=info_01)

root.mainloop()
