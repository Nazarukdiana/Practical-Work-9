from tkinter import *

root = Tk()
root.title("Привітання")
root.geometry('400x100')
root['bg'] = 'red'

def welcome(event=None):
    name = edit1.get()
    return Label(text=f'Вітаю {name}', bg='white').grid(row=2, column=0, columnspan=2)

label1 = Label(text="Введіть ім'я", width=20, bg='pink')
edit1 = Entry(width=20)
button1 = Button(text="OK", width=10)

root.bind('<space>', welcome)

label1.grid(row=0, column=0)
edit1.grid(row=0, column=1)
button1.grid(row=1, column=0, columnspan=2)

root.mainloop() 

root.mainloop()


root.mainloop()

