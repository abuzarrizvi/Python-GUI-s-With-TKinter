from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog


root = Tk()
root.title('Learn To Code at Github.com')
root.iconbitmap('Martz90-Circle-Camera.ico')
root.geometry("400x400")

def show():
	mylabel = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="check this box, I dare you!", variable=var, onvalue="Pizza", offvalue="Hamburger")
c.deselect()
c.pack()

my_btn = Button(root, text="show selection", command=show).pack()

root.mainloop()
