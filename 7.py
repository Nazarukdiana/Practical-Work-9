from tkinter import *

def Factorial(event=None):  
    try:
        N = int(edit1.get())
        f = 1
        for i in range(1, N + 1):
            f *= i
        label2['text'] = f"Факторіал числа {N}! = {f}"
    except ValueError:
        label2['text'] = "Введіть ціле число!"

root = Tk()
root.geometry("400x150")
root.title("Факторіал")

label1 = Label(root, text="Введіть число N:")
label1.grid(column=0, row=0, padx=10, pady=10, sticky="e")

edit1 = Entry(root)
edit1.grid(column=1, row=0, padx=10, pady=10)

label2 = Label(root, text="", fg="blue")
label2.grid(column=1, row=1, padx=10, pady=5)

btn = Button(root, text="Обчислити факторіал")
btn.grid(column=1, row=2, padx=10, pady=10)
btn.bind("<Button-1>", Factorial)  

root.mainloop()

