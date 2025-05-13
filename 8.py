from tkinter import *

def Dobutok(event=None):  
    try:
        N = int(edit1.get())
        d = 1
        for i in range(1, N + 1):
            d *= i
        label2['text'] = f"Добуток чисел 1 * 2 * ... * {N} = {d}"
    except ValueError:
        label2['text'] = "Введіть ціле число!"

root = Tk()
root.geometry("480x180")
root.title("Добуток чисел")

label1 = Label(root, text="Введіть число:")
label1.grid(row=0, column=0, padx=10, pady=10, sticky="e")

edit1 = Entry(root)
edit1.grid(row=0, column=1, padx=10, pady=10)

label2 = Label(root, text="", fg="blue")
label2.grid(row=1, column=1, padx=10, pady=5)

btn = Button(root, text="Обчислити добуток")
btn.grid(row=2, column=1, padx=10, pady=10)
btn.bind("<Button-1>", Dobutok)

root.mainloop()
