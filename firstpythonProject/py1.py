# import os
# tmp=input("nhap file can xoa: ")
# if os.path.exists(tmp):
#     os.remove(tmp)
#     print("deleted")
# else:
#     print("not exist")
import os
import shutil
#tao file
name = input("Nhap ten file moi ")
f = open(name,'w',encoding="utf-8")
f.close()
#nhap ND
f=open(name,"a+",encoding="utf-8")
noidung = input("Nhap nd can ghi vao file :  ")
f.write(noidung)
f.close()
#in ra thuoc tinh cua file
f = open(name,'wb')
print("Tên File: ",f.name)
print("Chế độ mở của file ",f.name," ",f.mode)
if f.closed:
    print(f.name," đang đóng")
else:
    print(f.name, " đang mở")
f.close()
#đọc nội dung của file trên màn hình
f = open(name,"r",encoding="utf-8")
print("noi dung cua file : ")
print(f.readline())
f.close()
#đổi tên file với tên mới được nhập từ bàn phím
newname = input("Nhập tên mới cho file:  ")
while os.path.exists(newname):
    newname = input("File đã tồn tại vui lòng nhập lại:  ")
os.rename(name,newname)
# copy file vừa đổi sang ổ D
shutil.copy(os.path.abspath(newname),'D:/')





