from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog


root = Tk()
root.title('Learn To Code at Github.com')
root.iconbitmap('Martz90-Circle-Camera.ico')
root.geometry("400x400")

#Drop Down Boxes
def show():
	mylbl = Label(root, text=clicked.get()).pack()

options = [
	"Monday", 
	"Tuesday", 
	"Wednesday", 
	"Thursday", 
	"Friday",
	"Saturday"
]
clicked = StringVar()
clicked.set(options[0])


drop = OptionMenu(root, clicked, *options)
drop.pack()
mybtn = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
