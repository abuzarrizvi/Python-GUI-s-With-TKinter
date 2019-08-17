from tkinter import *

root = Tk()

#creating a Label Widget
myLabel1 = Label(root, text="Hello world!").grid(row=0, column=0)
myLabel2 = Label(root, text="My Name Is Abuzar Rizvi").grid(row=1, column=5)



#for code readablility use it
#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=1, column=5)


#no need to do it in case of grid
#showing it onto the screen
#myLabel.pack()


root.mainloop()