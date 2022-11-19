import mysql.connector as mysql

menu = 0
cnx = mysql.connect(host='localhost',port='3306', user='root', passwd='', database='kinhbac')
my_cursor = cnx.cursor()


def insert():
    id = input('nhap ID: ')
    diachi = input('nhap ho ten: ')
    val=(str(id),str(diachi))
    query4 = "INSERT INTO sinhvien (ID, name) VALUES (%s, %s)"
    my_cursor.execute(query4,val)
    query5 = 'SELECT * FROM sinhvien'
    my_cursor.execute(query5)
    for i in my_cursor:
        print(i)
    cnx.commit()


def delete():
    id = input('nhap ID cần xóa: ')
    val=(str(id),)
    query4 = "DELETE FROM sinhvien WHERE sinhvien.ID= %s"
    my_cursor.execute(query4, val)
    cnx.commit()



def update():
    id = input('nhap ID cần sửa: ')
    diachi = input('nhap ho ten: ')
    val=(str(diachi),str(id))
    query4 = "UPDATE sinhvien SET sinhvien.name= %s WHERE sinhvien.ID= %s"
    my_cursor.execute(query4,val)
    cnx.commit()


def hienthi():
    my_cursor.execute("SELECT * FROM sinhvien")
    records = my_cursor.fetchall()
    for i in records:
        print(i)



while menu < 5:
    print(" 1. insert  \n 2. Delete \n 3. update \n 4.show \n 5.quit")
    menu = int(input("Select 1->4 : "))
    if menu == 1:
        insert()
    if menu == 2:
        delete()
    if menu == 3:
        update()
    if menu == 4:
        hienthi()
    if menu == 5:
        break
