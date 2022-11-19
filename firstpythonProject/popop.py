import tkinter as tk

percentage = 0.3

def popupmsg(msg):
    popup = tk.Toplevel()
    popup.title("!")
    label = tk.Label(popup, text=msg) #Can add a font arg here
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

popupmsg('You have a discount of ' + str(percentage*100) + '%')