from tkinter import *
from PIL import ImageTk, Image



root = Tk()
root.title("Usages of Images")
root.iconbitmap("icon.ico")

my_image = ImageTk.PhotoImage(Image.open("cat.jpeg"))
my_label = Label(image=my_image)
my_label.pack()





button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()




root.mainloop()
