from tkinter import *

root = Tk()


def myClick():
	myLabel = Label(root, text="Look! I clicked a Button!!")
	myLabel.pack()

#creating a Label Widget
myButton = Button(root, text="Click Me!", command=myClick, fg="blue", bg="red")
#myButton = Button(root, text="Click Me!", state=DISABLED, padx=50, pady=50, fg="blue", bg="red"/bg="ffffff")



#showing it onto the screen
myButton.pack()


root.mainloop()