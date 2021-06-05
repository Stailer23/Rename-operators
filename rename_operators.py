import one
from tkinter import *
root=Tk()
root.title('Изменение оператора')
root.geometry('300x160')
root.resizable(False, False)

def go():
    g1=e1.get()
    g2=e2.get()
    g3=e3.get()
    one.start(g1, g2, g3)
    l4=Label(root, text='Готово!')
    l4.place(x=160, y=120)

l1=LabelFrame(root, text='Введите номер RTU')
l1.place(x=10, y=5)
e1= Entry(l1, width=30)
e1.pack()

l2=LabelFrame(root, text = 'Что заменить')
l2.place(x=10, y=50)
e2=Entry(l2, width=20)
e2.pack()

l3=LabelFrame(root, text = 'На что заменить')
l3.place(x=10, y=95)
e3=Entry(l3, width=20)
e3.pack()

l5=Label(root, text='by Nikolaev', fg='gray')
l5.place(x=230,y=140)

b1=Button(root, text = 'Заменить', command=go)
b1.place(x=160, y=80)

root.mainloop()