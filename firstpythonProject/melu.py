import tkinter as tk
window = tk.Tk()
#khai báo thanh menu
menubar= tk.Menu(window)
window.config(menu=menubar)
# khai báo menu file va add vao menubar
menufile = tk.Menu(menubar, tearoff=0)
menuview = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="File", menu=menufile)
menubar.add_cascade(label="View", menu=menuview)
#khai bao cac menu con  va add vao menu file
menufile.add_command(label='New')
menufile.add_command(label='Open')
menufile.add_command(label='Save')
menufile.add_command(label='Save As')
menufile.add_separator()
menufile.add_command(label="Exit", command=window.quit)
#
menuview.add_command(label='ZoomIn')
menuview.add_command(label='ZoomOut')
menuview.add_command(label='ZoomExtend')

window.mainloop()