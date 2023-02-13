from tkinter import *
from tkinter import messagebox

def btn_click():
    v1 = label1.get()
    v2 = label2.get()
    txt = f'label1={str(v1)}, label2={str(v2)}'
    messagebox.showinfo(title='Мой заголовок', message=txt)

def btn_click_create_file():

    file_name = 'd:\\tmp\\tmp_text_file.txt'
    f = open(file_name,'w') # 'r+' для чтения и записи
    try:
        print('Test text to writing to text file\n\n  str2', file=f)
    finally:
        f.close()

    messagebox.showinfo(title='Мой заголовок', message= f'Создан файл с именем [{file_name}]')

root = Tk()
root['bg'] = '#fafa80'
root.title('Помощник windows')
root.geometry('300x250')
root.resizable(width=True, height=True) # возможность изменять размеры окна

canvas = Canvas(root, height=300, width=250)
canvas.pack()

frame = Frame(root, bg='red')
frame.place(relx=0.15, rely=0.15, relwidth=0.70, relheight=0.70)

title = Label(frame, text='Текст подсказка', bg='gray', font=40)
title.pack()

btn1= Button(frame, text='Кнопка с длинным текстом', bg='yellow', command=btn_click)
btn1.pack()

label1 = Entry(frame)
label1.insert(0, '777')
label1.pack()

label2 = Entry(frame)
label2.insert(0, '888')
label2.pack()

btn2= Button(frame, text='Создать файл', bg='yellow', command=btn_click_create_file)
btn2.pack()


root.mainloop()
