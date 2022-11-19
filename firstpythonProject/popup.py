# import everything from tkinter module
from tkinter import *

# import messagebox from tkinter module
import tkinter.messagebox

# create a tkinter root window
root = tkinter.Tk()

# root window title and dimension
root.title("When you press a any button the message will pop up")
root.geometry('500x300')


# Create a messagebox showinfo
def West():
    tkinter.messagebox.showinfo("Python ","Python thật thú vị")



# Create a Buttons

Button1 = Button(root, text="Hello", command=West, pady=10)
Button2 = Button(root, text="Exit", command=root.quit, pady=10)


# Set the position of buttons
Button1.pack()
Button2.pack()


root.mainloop()