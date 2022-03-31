from tkinter import *

root = Tk()

#creating a  label widget

myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="Rodrigo Noriega")

#shoving it into screen

#myLabel.pack()
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=7)

root.mainloop()