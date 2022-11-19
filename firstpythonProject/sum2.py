#nguyen huu hung
from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("SỐ CHUNG > 5")
num1 = StringVar()
num2 = StringVar()
kq = StringVar()

def chung():
    text1 = num1.get()
    text2 = num2.get()
    kk = ""
    tarr1 = text1.split("-")
    tarr2 = text2.split("-")
    arr1 = []
    arr2 = []
    for i in tarr1:
        arr1.append(int(i))
    arr1.sort()
    for i in tarr2:
        arr2.append(int(i))
    arr2.sort()
    common_s = set(arr1) & set(arr2)
    for i in common_s:
        if i>5:
          kk +=str(i)+"-"
    kk = kk[0:len(kk)-1]
    kq.set(""+kk)

Label(root, text="Mảng A").place(x=60, y=60)
Entry(root, width="35", textvariable=num1).place(x=140, y=60)
Label(root, text="Mảng B").place(x=60, y=90)
Entry(root, width="35", textvariable=num2).place(x=140, y=90)

Button(root,bg="yellow", width="15",height=2, text=("tìm số chung > 5"), command=chung).place(x=20, y=125)
Entry(root, justify=CENTER, width="35", textvariable=kq).place(x=140, y=135)




root.mainloop()
