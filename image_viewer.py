from tkinter import *
from PIL import ImageTk, Image




def next(image_number):
    global my_label
    global button_next
    global button_previous

    my_label.grid_forget()
    my_label = Label(image=images[image_number - 1])
    button_next = Button(root, text=">>", command=lambda: next(image_number + 1))
    button_previous = Button(root, text="<<", command=lambda: previous(image_number - 1))

    if image_number == 5:
        button_next = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_next.grid(row=1, column=2)
    button_previous.grid(row=1, column=0)


def previous(image_number):
    global my_label
    global button_next
    global button_previous

    my_label.grid_forget()
    my_label = Label(image=images[image_number - 1])
    button_next = Button(root, text=">>", command=lambda: next(image_number + 1))
    button_previous = Button(root, text="<<", command=lambda: previous(image_number - 1))

    if image_number == 1:
        button_previous = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_next.grid(row=1, column=2)
    button_previous.grid(row=1, column=0)

root = Tk()
root.title("Usages of Images")
root.iconbitmap("list.ico")

my_image1 = ImageTk.PhotoImage(Image.open("Cat_Photos/cat.jpeg"))
my_image2 = ImageTk.PhotoImage(Image.open("Cat_Photos/cat2.jpg"))
my_image3 = ImageTk.PhotoImage(Image.open("Cat_Photos/cat3.jpg"))
my_image4 = ImageTk.PhotoImage(Image.open("Cat_Photos/cat4.png"))
my_image5 = ImageTk.PhotoImage(Image.open("Cat_Photos/cat5.png"))
images = [my_image1, my_image2, my_image3, my_image4, my_image5]


my_label = Label(image=images[0])
my_label.grid(row=0, column=0, columnspan=3)

button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.grid(row=1, column=1)
button_next = Button(root, text=">>", command=lambda: next(2))
button_next.grid(row=1, column=2)

button_previous = Button(root, text="<<", command=previous)
button_previous.grid(row=1, column=0)



root.mainloop()
