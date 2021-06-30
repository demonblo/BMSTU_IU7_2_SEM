from tkinter import *
from tkinter.messagebox import *
root = Tk()
#Размер проги
root.geometry("610x500")
root.resizable(width=False, height=False)
root.title("Calculator")
root.configure(bg="BLUE")


def calculate(event):
    main_string = Entry_1.get()  
    chisla = main_string.split(' ')
    otvet = ''
    for i in chisla:
        current = 0
        length = len(i) - 1
        for j in i:
            if j == '1':
                current += 3**length
            elif j == 'i':
                current += (3**length) * (-1)
            length -= 1
        otvet += str(current) + ' '
    Label_5['text'] = otvet
                    
            
        

#Frames
left_frame = Frame(root, width=550, heigh=400, bg='grey')

left_frame.place(x=30, y= 30)


Entry_1 = Entry(left_frame, width=30)
Entry_1.place(x=80, y=50)
Label_1 = Label(left_frame, width=6, text='Ввод', bg='grey',font=('UBUNTU',10))
Label_1.place(x=20, y=50)



Label_4 = Label(left_frame, width=10, text='Ответ', bg='grey',font=('UBUNTU',10))
Label_4.place(x=10, y=100)


Button_1 = Button(left_frame, text='Calculate',width=10,heigh=2)
Button_1.place(x=270,y=90)
Button_1.bind('<Button-1>', calculate)

Label_5 = Label(left_frame, width=20, heigh=1, bg='white', font=('UBUNTU',10) )
Label_5.place(x=80, y=100)

root.mainloop()

