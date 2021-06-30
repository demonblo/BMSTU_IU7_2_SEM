from tkinter import *
from tkinter.messagebox import *
from time import *
from random import *
root = Tk()

#Сортировка Вставкой и замер времени сортировки
def Insert_plus_time(array):
    Time_1 = time()
    for i in range (1, len(array), 1):
        k = i
        while array[k] < array[k-1] and k >0:
            array[k], array[k-1] = array[k-1], array[k]
            k -= 1
##            if k == 0:
##                break
    Time_2 = time()
    Result_Time = Time_2 - Time_1
    Result_Time = round(Result_Time, 5)
    return Result_Time

    
# Тестоовоя сортировка свставкой
def TEST(event):
    string = Entry_1.get()
    array = string.split(' ')
    try:
        for i in range(len(array)):
            array[i] = float(array[i])
        for i in range (1, len(array), 1):
            k = i
            while array[k] < array[k-1]:
                array[k], array[k-1] = array[k-1], array[k]
                k -= 1
                if k == 0:
                    break
        outputstring = ''
        for i in array:
            if i % 10 == 0:
                i = int(i)
            outputstring += str(i) + ' '
        outputtxt = 'Исходный массив: ' + string + '\nОтсортированный массив: ' + outputstring
        showinfo('Test', outputtxt)
    	
        
    except ValueError:
        showwarning("Ошибка!", "Некорректный ввод!")

def test():
    string = Entry_1.get()
    array = string.split(' ')
    try:
        for i in range(len(array)):
            array[i] = float(array[i])
        for i in range (1, len(array), 1):
            k = i
            while array[k] < array[k-1]:
                array[k], array[k-1] = array[k-1], array[k]
                k -= 1
                if k == 0:
                    break
        outputstring = ''
        for i in array:
            if i % 10 == 0:
                i = int(i)
            outputstring += str(i) + ' '
        outputtxt = 'Исходный массив: ' + string + '\nОтсортированный массив: ' + outputstring
        showinfo('Test', outputtxt)
    	
        
    except ValueError:
        showwarning("Ошибка!", "Некорректный ввод!")
        
# Справка
def info(event):
    information = 'Данная программа показывает эффективность сортировки массивов различных размерностей методом "Вставка".\n\nПрограмма так же показывает эффективность встроенной функции .sort.\n\nПрограмма написана студентом ИУ7-22Б Блохиным Дмитрием.'

    showinfo('Информация о программе', information)

def info_01():
    information = 'Данная программа показывает эффективность сортировки массивов различных размерностей методом "Вставка".\n\nПрограмма так же показывает эффективность встроенной функции .sort.\n\nПрограмма написана студентом ИУ7-22Б Блохиным Дмитрием.'

    showinfo('Информация о программе', information)
    
#main
def main(event):
    try:
        N1 = int(Entry_r1.get())
        N2 = int(Entry_r2.get())
        N3 = int(Entry_r3.get())

        upor_N1 = []
        upor_N2 = []
        upor_N3 = []
        rev_upor_N1 = []
        rev_upor_N2 = []
        rev_upor_N3 = []
        random_N1 = []
        random_N2 = []
        random_N3 = []

        for i in range (N1):
            upor_N1.append(i+1)
            random_N1.append(randint(1, N1 * 2))
            rev_upor_N1.append(N1 - i)
        
        for i in range (N2):
            upor_N2.append(i+1)
            random_N2.append(uniform(1, N2 * 2))
            rev_upor_N2.append(N2 - i)
        
        for i in range (N3):
            upor_N3.append(i+1)
            random_N3.append(uniform(1, N3 * 2))
            rev_upor_N3.append(N1 - i)

        sort_N1 = random_N1
        sort_N2 = random_N2
        sort_N3 = random_N3

#Упорядоченный массив
        Result_Time = Insert_plus_time(upor_N1)
        OutputTXT = str(Result_Time)
        Label_upor_N1['text'] = OutputTXT

        Result_Time = Insert_plus_time(upor_N2)
        OutputTXT = str(Result_Time)
        Label_upor_N2['text'] = OutputTXT

        Result_Time = Insert_plus_time(upor_N3)
        OutputTXT = str(Result_Time)
        Label_upor_N3['text'] = OutputTXT

#Случайный массив
        Result_Time = Insert_plus_time(random_N1)
        OutputTXT = str(Result_Time)
        Label_random_N1['text'] = OutputTXT

        Result_Time = Insert_plus_time(random_N2)
        OutputTXT = str(Result_Time)
        Label_random_N2['text'] = OutputTXT

        Result_Time = Insert_plus_time(random_N3)
        OutputTXT = str(Result_Time)
        Label_random_N3['text'] = OutputTXT

#Обратно упорядоченный массив
        Result_Time = Insert_plus_time(rev_upor_N1)
        OutputTXT = str(Result_Time)
        Label_rev_upor_N1['text'] = OutputTXT

        Result_Time = Insert_plus_time(rev_upor_N2)
        OutputTXT = str(Result_Time)
        Label_rev_upor_N2['text'] = OutputTXT

        Result_Time = Insert_plus_time(rev_upor_N3)
        OutputTXT = str(Result_Time)
        Label_rev_upor_N3['text'] = OutputTXT
    
#.sort
        Time_1 = time()
        sort_N1.sort()
        Time_2 = time()
        Result_Time = Time_2 - Time_1
        Result_Time = round(Result_Time, 5)
        OutputTXT = str(Result_Time)
        Label_sort_N1['text'] = OutputTXT

        Time_1 = time()
        sort_N2.sort()
        Time_2 = time()
        Result_Time = Time_2 - Time_1
        Result_Time = round(Result_Time, 5)
        OutputTXT = str(Result_Time)
        Label_sort_N2['text'] = OutputTXT

        Time_1 = time()
        sort_N3.sort()
        Time_2 = time()
        Result_Time = Time_2 - Time_1
        Result_Time = round(Result_Time, 5)
        OutputTXT = str(Result_Time)
        Label_sort_N3['text'] = OutputTXT
    except ValueError or N1 < 0 or N2 < 0 or N3 < 0:
        showwarning("Ошибка!", "Некорректный ввод!")

def calculate():
    try:
        N1 = int(Entry_r1.get())
        N2 = int(Entry_r2.get())
        N3 = int(Entry_r3.get())

        upor_N1 = []
        upor_N2 = []
        upor_N3 = []
        rev_upor_N1 = []
        rev_upor_N2 = []
        rev_upor_N3 = []
        random_N1 = []
        random_N2 = []
        random_N3 = []

        for i in range (N1):
            upor_N1.append(i+1)
            random_N1.append(randint(1, N1 * 2))
            rev_upor_N1.append(N1 - i)
        
        for i in range (N2):
            upor_N2.append(i+1)
            random_N2.append(uniform(1, N2 * 2))
            rev_upor_N2.append(N2 - i)
        
        for i in range (N3):
            upor_N3.append(i+1)
            random_N3.append(uniform(1, N3 * 2))
            rev_upor_N3.append(N1 - i)

        sort_N1 = random_N1
        sort_N2 = random_N2
        sort_N3 = random_N3

#Упорядоченный массив
        Result_Time = Insert_plus_time(upor_N1)
        OutputTXT = str(Result_Time)
        Label_upor_N1['text'] = OutputTXT

        Result_Time = Insert_plus_time(upor_N2)
        OutputTXT = str(Result_Time)
        Label_upor_N2['text'] = OutputTXT

        Result_Time = Insert_plus_time(upor_N3)
        OutputTXT = str(Result_Time)
        Label_upor_N3['text'] = OutputTXT

#Случайный массив
        Result_Time = Insert_plus_time(random_N1)
        OutputTXT = str(Result_Time)
        Label_random_N1['text'] = OutputTXT

        Result_Time = Insert_plus_time(random_N2)
        OutputTXT = str(Result_Time)
        Label_random_N2['text'] = OutputTXT

        Result_Time = Insert_plus_time(random_N3)
        OutputTXT = str(Result_Time)
        Label_random_N3['text'] = OutputTXT

#Обратно упорядоченный массив
        Result_Time = Insert_plus_time(rev_upor_N1)
        OutputTXT = str(Result_Time)
        Label_rev_upor_N1['text'] = OutputTXT

        Result_Time = Insert_plus_time(rev_upor_N2)
        OutputTXT = str(Result_Time)
        Label_rev_upor_N2['text'] = OutputTXT

        Result_Time = Insert_plus_time(rev_upor_N3)
        OutputTXT = str(Result_Time)
        Label_rev_upor_N3['text'] = OutputTXT
    
#.sort
        Time_1 = time()
        sort_N1.sort()
        Time_2 = time()
        Result_Time = Time_2 - Time_1
        Result_Time = round(Result_Time, 5)
        OutputTXT = str(Result_Time)
        Label_sort_N1['text'] = OutputTXT

        Time_1 = time()
        sort_N2.sort()
        Time_2 = time()
        Result_Time = Time_2 - Time_1
        Result_Time = round(Result_Time, 5)
        OutputTXT = str(Result_Time)
        Label_sort_N2['text'] = OutputTXT

        Time_1 = time()
        sort_N3.sort()
        Time_2 = time()
        Result_Time = Time_2 - Time_1
        Result_Time = round(Result_Time, 5)
        OutputTXT = str(Result_Time)
        Label_sort_N3['text'] = OutputTXT
    except ValueError or N1 < 0 or N2 < 0 or N3 < 0:
        showwarning("Ошибка!", "Некорректный ввод!")
   
#Размер проги
root.geometry("610x600")
root.resizable(width=False, height=False)
root.title("Сортировки")
root.configure(bg="cyan4")

#Frame
left_frame = Frame(root, width=550, height=550, bg='grey')
left_frame.place(x=30, y= 30)

#Справка
Button_info = Button(left_frame, text='Справка',width=10,heigh=2)
Button_info.place(x=354,y=160)
Button_info.bind('<Button-1>', info)

#Ввод массива
Entry_1 = Entry(left_frame, width=40)
Entry_1.place(x=80, y=50)

Label_1 = Label(left_frame, width=18, text='Введите массив', bg='grey',font=('UBUNTU',15))
Label_1.place(x=170, y=13)

Button_1 = Button(left_frame, text='Test',width=10,heigh=2)
Button_1.place(x=215,y=90)
Button_1.bind('<Button-1>', TEST)

#3 размера массивов
Label_1 = Label(left_frame, width=25, text='Введите 3 размера массивов.\nРекомендуемый размер <= 9000.', bg='grey',font=('UBUNTU',14))
Label_1.place(x=83, y=155)

Entry_r1 = Entry(left_frame, width=10)
Entry_r1.place(x=80, y=210)
Entry_r2 = Entry(left_frame, width=10)
Entry_r2.place(x=215, y=210)
Entry_r3 = Entry(left_frame, width=10)
Entry_r3.place(x=350, y=210)

#Таблица
Label_clear = Label(left_frame, width=10, height=2, bg='white')
Label_clear.place(x=70, y=280)
Label_N1 = Label(left_frame, width=10, height=2, text = '№1', bg='white')
Label_N1.place(x=170, y=280)
Label_N2 = Label(left_frame, width=10, height=2, text = '№2', bg='white')
Label_N2.place(x=270, y=280)
Label_N3 = Label(left_frame, width=10, height=2, text = '№3', bg='white')
Label_N3.place(x=370, y=280)

Label_upor = Label(left_frame, width=10, text='Упоряд.', height=2, bg='white')
Label_upor.place(x=70, y=325)
Label_upor_N1 = Label(left_frame, width=10, height=2, bg='white')
Label_upor_N1.place(x=170, y=325)
Label_upor_N2 = Label(left_frame, width=10, height=2, bg='white')
Label_upor_N2.place(x=270, y=325)
Label_upor_N3 = Label(left_frame, width=10, height=2, bg='white')
Label_upor_N3.place(x=370, y=325)

Label_random = Label(left_frame, width=10, text='Случайный', height=2, bg='white')
Label_random.place(x=70, y=370)
Label_random_N1 = Label(left_frame, width=10, height=2, bg='white')
Label_random_N1.place(x=170, y=370)
Label_random_N2 = Label(left_frame, width=10, height=2, bg='white')
Label_random_N2.place(x=270, y=370)
Label_random_N3 = Label(left_frame, width=10, height=2, bg='white')
Label_random_N3.place(x=370, y=370)

Label_rev_upor = Label(left_frame, width=10, text='Обр. упоряд.', height=2, bg='white')
Label_rev_upor.place(x=70, y=415)
Label_rev_upor_N1 = Label(left_frame, width=10, height=2, bg='white')
Label_rev_upor_N1.place(x=170, y=415)
Label_rev_upor_N2 = Label(left_frame, width=10, height=2, bg='white')
Label_rev_upor_N2.place(x=270, y=415)
Label_rev_upor_N3 = Label(left_frame, width=10, height=2, bg='white')
Label_rev_upor_N3.place(x=370, y=415)

Label_sort = Label(left_frame, width=10, text='.sort', height=2, bg='white')
Label_sort.place(x=70, y=460)
Label_sort_N1 = Label(left_frame, width=10, height=2, bg='white')
Label_sort_N1.place(x=170, y=460)
Label_sort_N2 = Label(left_frame, width=10, height=2, bg='white')
Label_sort_N2.place(x=270, y=460)
Label_sort_N3 = Label(left_frame, width=10, height=2, bg='white')
Label_sort_N3.place(x=370, y=460)

Button_ok = Button(left_frame, text='OK',width=10,heigh=1)
Button_ok.place(x=218,y=250)
Button_ok.bind('<Button-1>', main)

#Menu
main_menu = Menu(root)
root.configure(menu=main_menu)

first_item = Menu(main_menu)
main_menu.add_cascade(label="Commands", menu = first_item)
first_item.add_command(label="Test", command=test)
first_item.add_command(label="Calculate", command=calculate)
first_item.add_command(label="Info", command=info_01)


root.mainloop()
