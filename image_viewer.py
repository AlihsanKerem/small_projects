from tkinter import *
from PIL import ImageTk, Image


global screen
screen = 0

def next(number):
    global screen
    screen = number + 1
def previous(number):
    global screen
    screen = number - 1

root = Tk()
root.title("Usages of Images")
root.iconbitmap("list.ico")

button_next = Button(root, text=">>", command=lambda: next(screen))
button_next.pack()

button_previous = Button(root, text="<<", command=lambda: previous(screen))
button_previous.pack()

my_image1 = ImageTk.PhotoImage(Image.open("Cat_Photos/cat.jpeg"))
my_image2 = ImageTk.PhotoImage(Image.open("Cat_Photos/cat2.jpg"))
my_image3 = ImageTk.PhotoImage(Image.open("Cat_Photos/cat3.jpg"))
my_image4 = ImageTk.PhotoImage(Image.open("Cat_Photos/cat4.png"))
my_image5 = ImageTk.PhotoImage(Image.open("Cat_Photos/cat5.png"))
images = [my_image1, my_image2, my_image3, my_image4, my_image5]


my_label = Label(image=images[screen])
my_label.pack()





button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()



root.mainloop()
