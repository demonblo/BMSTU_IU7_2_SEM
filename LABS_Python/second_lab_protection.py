from tkinter import*

root = Tk()
entry_window = Entry(width = 50)
output_window = Label(width = 50)
root.geometry("500x150")
root.resizable(width=False, height=False)
root.title("Шейкер-Сортировка")
root.configure(bg="cyan4")

def sort():
#Sorting
    a = entry_window.get().split()
    for i in range(len(a)):
        a[i] = float(a[i])    

    k = len(a)-1
    ub = len(a)-1
    lb = 1
    while (lb < ub): 
        for j in range (ub, lb-1, -1):
            if a[j-1] > a[j]: 
                a[j-1], a[j] = a[j], a[j-1]
                k = j
            lb = k
        for j in range (lb, ub+1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                k = j
            ub = k
            
    if len(a) == 2 and a[0] > a[1]:
        a[0], a[1] = a[1], a[0]        
#Output
    output = ''
    for i in range(len(a)):
        if (a[i] * 10)%10 == 0:
            output += str(int(a[i])) + ' '
        else:
            output += str(a[i]) + ' '

    output_window['text'] = output
#Placing    
button_sort = Button(text = 'Sort', width = 10, height = 1, command = sort)
button_sort.place(x = 185, y = 65)
entry_window.place(x = 5, y = 5)
output_window.place(x = 7, y = 35)
root.mainloop()
    

