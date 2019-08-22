from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Learn To Code at Github.com')
root.iconbitmap('Martz90-Circle-Camera.ico')

def open():
	global my_img
	top = Toplevel()
	top.title('My second Window')
	top.iconbitmap('Martz90-Circle-Camera.ico')

	lbl = Label(top, text="Hello World!").pack()
	my_img = ImageTk.PhotoImage(Image.open("images/download.png"))
	lbl = Label(top, image=my_img).pack()
	btn2 = Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text="Open Second Window", command=open).pack()



root.mainloop()
