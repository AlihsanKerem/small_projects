from tkinter import *

root = Tk()
root.title("Calculator")


def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def clear():
    entry.delete(0, END)




def button_add():
    number = entry.get()
    global first
    first = int(number)
    entry.delete(0, END)

def button_equal():
    number = int(entry.get())
    total = first + number
    entry.delete(0, END)
    entry.insert(0, str(total))

def button_minus():
    number = int(entry.get())
    result = first

entry = Entry(root, width=60, borderwidth=10)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# adding buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_addition = Button(root, text="+", padx=40, pady=20, command=button_add)
button_minus = Button(root, text="-", padx=40, pady=20, command=button_minus)
button_multi = Button(root, text="*", padx=40, pady=20, command=button_add)
button_division = Button(root, text="/", padx=40, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=39, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=29, pady=20, command=clear)

#making the grid
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_division.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_multi.grid(row=2, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_minus.grid(row=1, column=3)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_addition.grid(row=4, column=3)
button_equal.grid(row=4, column=2)

mainloop()