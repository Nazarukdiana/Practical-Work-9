from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x100+600+400")
str_var = StringVar()  

def button_click(event=None):     
    name = str_var.get()
    messagebox.showinfo("Привітання", "Вітаю " + name + "!")  

label = Label(text="Введіть ім'я:")
label.pack()  

edit = Entry(root, textvariable=str_var)
edit.pack()  

button = Button(root, text="Ok!", command=button_click)  
button.pack()  

root.bind("<Return>", button_click)  

root.mainloop()

