import os
f=open("text.txt","a+",encoding="utf-8")
noidung = input("Nhap nd can ghi vao file :  ")
f.write(noidung)
f.close()
f=open("text.txt","r",encoding="utf-8")
print("noi dung dk ghi la: ")
print(f.readline())
f.close()