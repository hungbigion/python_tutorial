import tkinter as tk
import wx as w
# app = w.App()
# frame = w.Frame(parent=None, title="Chuong trinh PYTHON")
# contend = w.StaticText(parent=frame, lable="!!!")
#
# frame.Show()
# app.MainLoop()
#tạo cửa sổ
window = tk.Tk()
window.title("OK GUI")
window.geometry("600x300+500+200")
lb = tk.Label(window, text="Hello Python")
lb.pack()
btn1 = tk.Button()
window.mainloop()