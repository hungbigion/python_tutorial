import tkinter as tk
import tkinter.messagebox

window =tk.Tk()
window.title('gd nist box')
window.geometry("300x300+500+200")
# lb = tk.Label(window,text="hãy lựa chn ngôn ngữ ")
#
# listbox = tk.Listbox(window)
#
# listbox.insert(1,'PHP')
# listbox.insert(2,'C#')
# listbox.insert(3,'Python')
#
# lb.pack()
# listbox.pack()
frame1 = tk.Frame(window,width=50, height=50, bg='pink')
frame1.pack(fill=tk.Y,side="left")
frame2 = tk.Frame(window, width=50, bg='yellow')
frame2.pack(fill=tk.Y,side="left")
frame3 = tk.Frame(window, width=50, bg='gray')
frame3.pack(fill=tk.Y,side="left")

window.mainloop()