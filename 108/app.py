# модульное реешние принцип для каждой задачи тот же

from tkinter import Tk, Label, Entry, Button

window = Tk()
window.title("Вывод кратных чисел")

label1 = Label(window, text="Введите число:")
label1.grid(row=0, column=0)

input1 = Entry(window) 
input1.grid(row=0, column=1)

label2 = Label(window)
label2.grid(row=1, column=0, columnspan=2)

def calculate():
    num = int(input1.get())
    result = ""
    for i in range(1, 11):
        result += str(i * num) + " "
    label2.config(text=result)

button = Button(window, text="Вычислить", command=calculate)
button.grid(row=2, column=0, columnspan=2)

window.mainloop()