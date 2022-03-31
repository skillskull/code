import os
from tkinter import *
from turtle import width

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked the button!!")
    myLabel.pack()

def calendar():
    os.system('ssh rn177@192.168.1.110')

def script_exec():
    os.system('bash /home/rn177/Documents/shell_script/advanced_echo.sh')

def get_name():
    hello = 'Hello' + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

e = Entry(root)
e.pack()

myButton = Button(root, text="Click Me!", padx=70, pady=50, command=calendar)
myButton2 = Button(root, text="Click Me!", padx=50, pady=50, command=script_exec)
myButton3 = Button(root, text='Enter Your name', command=get_name)
myButton.pack()
myButton2.pack()
myButton3.pack()

root.mainloop()