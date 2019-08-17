from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="white", fg="blue", borderwidth=5)
e.pack()
e.insert(0,"Enter Your Name: ")

def myClick():
	hello = "Hello " + e.get()
	myLabel = Label(root, text=hello)
	myLabel.pack()

#creating a Label Widget
myButton = Button(root, text="Enter Your Name", command=myClick, fg="blue", bg="White")


#showing it onto the screen
myButton.pack()

root.mainloop()