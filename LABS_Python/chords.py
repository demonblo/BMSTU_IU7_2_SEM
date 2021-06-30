from tkinter import *
from tkinter.messagebox import *
from math import *
import matplotlib.pyplot as plt


root = Tk()
# Справка
def codes(event):
    information = '0 - нет ошибок\n2 - превышен лимит итераций'
    showinfo('Информация о программе', information)

def codes_01():
    information = '0 - нет ошибок\n2 - превышен лимит итераций'
    showinfo('Информация о программе', information)

def info(event):
    information = 'Данная программа формирует таблицу корней функции f(x) = sin(x) на отрезке [a, b] с шагом h и точностью eps, которые вводятся пользователем.\nРазработано студентом ИУ7-22Б\nБлохиным Дмитрием.'
    showinfo('Информация о программе', information)

def info_01():
    information = 'Данная программа формирует таблицу корней функции f(x) = sin(x) на отрезке [a, b] с шагом h и точностью eps, которые вводятся пользователем.\nРазработано студентом ИУ7-22Б\nБлохиным Дмитрием.'
    showinfo('Информация о программе', information)

def output_of_corner(number, otrezok_out, x_out, f_out, counter_out, code_out, cur_y):
    label_output = Label(output_frame, width=3, text=number, height=1, bg='seashell3')
    label_output.place(x=0, y=cur_y)
    label_output = Label(output_frame, width=10, text=otrezok_out, height=1, bg='seashell3')
    label_output.place(x=38, y=cur_y)
    label_output = Label(output_frame, width=10, text=x_out, height=1, bg='seashell3')
    label_output.place(x=140, y=cur_y)
    label_output = Label(output_frame, width=8, text=f_out, height=1, bg='seashell3')
    label_output.place(x=241, y=cur_y)
    label_output = Label(output_frame, width=5, text=counter_out, height=1, bg='seashell3')
    label_output.place(x=325, y=cur_y)
    label_output = Label(output_frame, width=5, text=code_out, height=1, bg='seashell3')
    label_output.place(x=382, y=cur_y)
    cur_y += 20

    return cur_y

def f(x):
    y = sin(x)

    return y

def f_pr(x):
    y = cos(x)

    return y

def f_sec_pr(x):
    y = - sin(x)

    return y

# Calculate
def Calculate(event):
    a = input_a.get()
    b = input_b.get()
    h = input_h.get()
    eps = input_eps.get()
    max_it = input_max_it.get()
    output_frame.place(x=30, y=150)
    label_output = Label(output_frame, width=55, height=50, bg='seashell3')
    label_output.place(x=0, y=0)

    try:
        a = float(a)
        b = float(b)
        h = float(h)
        eps = float(eps)
        max_it = int(max_it)
        number = 1
        cur_y = 5
        s = []
        t = []
        a_copy = a
        i = 0

        while a_copy <= b:
            t.append(a_copy)
            a_copy += 0.001

        while i < len(t):
            s.append(f(t[i]))
            i += 1

        plt.plot(t, s, 'r', label='f(x) = sin(x)\nГолубые точки - точки перегиба.')
        plt.legend()
        for i in range(0, len(s)):
            if round(f_sec_pr(t[i]), 2) == - 0.0 or round(f_sec_pr(t[i]), 2) == 0.0:
                plt.plot(t[i], round(s[i], 2), 'bo')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(color='grey', linestyle='-', linewidth=1)
        plt.show()

        if h <= 0:
            showwarning('Ошибка!', 'Некорректный ввод шага.')
        elif b <= a:
            showwarning('Ошибка!', 'Некорректный ввод границ.')
        else:
            left = a
            right = a + h
            if right > b:
                right = b
            while right <= b:
                code = 10
                if f(left) <= 0 and f(right) >= 0 or f(left) >= 0 and f(right) <= 0:
                    code = 0
                    counter_of_it = 0
                    x = [right, left, right - (left - right) * f(right) / (f(left) - f(right))]
                    i = 2
                    prev = x[i - 1]
                    cur = x[i]
                    while counter_of_it < max_it and abs(cur - prev) > eps:
                        i += 1
                        x.append(x[i - 1] - f(x[i - 1]) * (x[i - 1] - x[0]) / (f(x[i - 1]) - f(x[0])))
                        cur = x[i]
                        prev = x[i - 1]
                        counter_of_it += 1
                        print('x = ', x[i], ' f(x) = ', f(x[i]))

                    if counter_of_it == max_it and abs(cur - prev) > eps:
                        code = 2
                if code != 10:
                    otrezok_out = '[' + ("%5.1f" % left) + ' ,' + ("%5.1f" % right) + ']'
                    x_out = ("%5.5f" % cur)
                    f_out = f(cur)
                    if f_out != 0.0:
                        f_out = ("%5.3e" % f_out)
                    if code == 2:
                        x_out = '-'
                        f_out = '-'
                    counter_out = str(counter_of_it)
                    code_out = str(code)
                    cur_y = output_of_corner(number, otrezok_out, x_out, f_out, counter_out, code_out, cur_y)
                    number += 1
                left = right
                if right + h > b and left < b:
                    right = b
                else:
                    right += h

            if number == 1:
                label_output = Label(output_frame, width=55, height=50, bg='seashell3')
                label_output.place(x=0, y=0)
                label_output = Label(output_frame, width=20, text='Нет корней!', height=2, bg='seashell3')
                label_output.place(x=160, y=0)

    except ValueError:
        showwarning('Ошибка!', 'Некорректный ввод!')

def Calculate_01():
    a = input_a.get()
    b = input_b.get()
    h = input_h.get()
    eps = input_eps.get()
    max_it = input_max_it.get()
    output_frame.place(x=30, y=150)
    label_output = Label(output_frame, width=55, height=50, bg='seashell3')
    label_output.place(x=0, y=0)

    try:
        a = float(a)
        b = float(b)
        h = float(h)
        eps = float(eps)
        max_it = int(max_it)
        number = 1
        cur_y = 5
        s = []
        t = []
        a_copy = a
        i = 0

        while a_copy <= b:
            t.append(a_copy)
            a_copy += 0.001

        while i < len(t):
            s.append(f(t[i]))
            i += 1

        plt.plot(t, s, 'r', label='f(x) = sin(x)\nГолубые точки - точки перегиба.')
        plt.legend()
        for i in range(0, len(s)):
            if round(f_sec_pr(t[i]), 2) == - 0.0 or round(f_sec_pr(t[i]), 2) == 0.0:
                plt.plot(t[i], round(s[i], 2), 'bo')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(color='grey', linestyle='-', linewidth=1)
        plt.show()

        if h <= 0:
            showwarning('Ошибка!', 'Некорректный ввод шага.')
        elif b <= a:
            showwarning('Ошибка!', 'Некорректный ввод границ.')
        else:
            left = a
            right = a + h
            if right > b:
                right = b
            while right <= b:
                code = 10
                if f(left) <= 0 and f(right) >= 0 or f(left) >= 0 and f(right) <= 0:
                    code = 0
                    counter_of_it = 0
                    x = [left, right, left - (right - left) * f(left) / (f(right) - f(left))]
                    i = 2
                    prev = x[i - 1]
                    cur = x[i]
                    while counter_of_it < max_it and abs(cur - prev) > eps:
                        i += 1
                        x.append(x[i - 2] - f(x[i - 2]) * (x[i - 1] - x[i - 2]) / (f(x[i - 1]) - f(x[i - 2])))
                        cur = x[i]
                        prev = x[i - 1]
                        counter_of_it += 1
                        print('x = ', x[i], ' f(x) = ', f(x[i]))

                    if counter_of_it == max_it and abs(cur - prev) > eps:
                        code = 2
                if code != 10:
                    otrezok_out = '[' + ("%5.1f" % left) + ' ,' + ("%5.1f" % right) + ']'
                    x_out = str(round(cur, 5))
                    f_out = f(cur)
                    if f_out != 0.0:
                        f_out = ("%5.3e" % f_out)
                    if code == 2:
                        x_out = '-'
                        f_out = '-'
                    counter_out = str(counter_of_it)
                    code_out = str(code)
                    cur_y = output_of_corner(number, otrezok_out, x_out, f_out, counter_out, code_out, cur_y)
                    number += 1
                left = right
                if right + h > b and left < b:
                    right = b
                else:
                    right += h

            if number == 1:
                label_output = Label(output_frame, width=55, height=50, bg='seashell3')
                label_output.place(x=0, y=0)
                label_output = Label(output_frame, width=20, text='Нет корней!', height=2, bg='seashell3')
                label_output.place(x=160, y=0)

    except ValueError:
        showwarning('Ошибка!', 'Некорректный ввод!')

# Размер проги
root.geometry("640x600")
root.resizable(width=False, height=False)
root.title("Корни")
root.configure(bg="cyan4")
# Frames
left_frame = Frame(root, width=580, height=550, bg='white')
left_frame.place(x=30, y=30)
output_frame = Frame(left_frame, width=433, height=385, bg='seashell3')
output_frame.place(x=30, y=150)
# Input
# Input a
label_input_from = Label(left_frame, width=10, text='Отрезок от', height=2, bg='white')
label_input_from.place(x=20, y=20)
input_a = Entry(left_frame, width=6)
input_a.place(x=110, y=25)
# Input b
label_input_to = Label(left_frame, width=2, text='до', height=2, bg='white')
label_input_to.place(x=185, y=20)
input_b = Entry(left_frame, width=6)
input_b.place(x=215, y=25)
# Input h
label_input_h = Label(left_frame, width=5, text='  Шаг =', height=2, bg='white')
label_input_h.place(x=290, y=20)
input_h = Entry(left_frame, width=6)
input_h.place(x=350, y=25)
# Input eps
label_input_eps = Label(left_frame, width=5, text='  eps =', height=2, bg='white')
label_input_eps.place(x=420, y=20)
input_eps = Entry(left_frame, width=6)
input_eps.place(x=480, y=25)
# Input max_it
label_input_max_it = Label(left_frame, width=20, text='  Max итераций =', height=2, bg='white')
label_input_max_it.place(x=318, y=60)
input_max_it = Entry(left_frame, width=6)
input_max_it.place(x=480, y=65)
# Output_in_frame
label_number = Label(left_frame, width=3, text='#', height=1, bg='seashell3')
label_number.place(x=30, y=121)
label_otrezok = Label(left_frame, width=10, text='[xi , xi+h]', height=1, bg='seashell3')
label_otrezok.place(x=68, y=121)
label_x = Label(left_frame, width=10, text='x', height=1, bg='seashell3')
label_x.place(x=170, y=121)
label_fx = Label(left_frame, width=8, text='f(x)', height=1, bg='seashell3')
label_fx.place(x=271, y=121)
label_iter = Label(left_frame, width=5, text='Итер.', height=1, bg='seashell3')
label_iter.place(x=355, y=121)
label_code = Label(left_frame, width=5, text='Code', height=1, bg='seashell3')
label_code.place(x=412, y=121)
# Calculate
Button_info = Button(left_frame, text='Calculate', width=10, heigh=2)
Button_info.place(x=466, y=109)
Button_info.bind('<Button-1>', Calculate)
# Справка
Button_info = Button(left_frame, text='Справка', width=10, heigh=2)
Button_info.place(x=466, y=149)
Button_info.bind('<Button-1>', info)
# Codes
Button_code = Button(left_frame, text='Коды ошибок', width=10, heigh=2)
Button_code.place(x=30, y=64)
Button_code.bind('<Button-1>', codes)
# Menu
main_menu = Menu(root)
root.configure(menu=main_menu)
first_item = Menu(main_menu)
main_menu.add_cascade(label="Commands", menu=first_item)
first_item.add_command(label="Info", command=info_01)
first_item.add_command(label="Codes", command=codes_01)
first_item.add_command(label="Calculate", command=Calculate_01)
# mainloop
root.mainloop()
