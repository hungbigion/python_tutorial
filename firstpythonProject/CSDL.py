import mysql.connector as mysql

cnx = mysql.connect(host='localhost',user='root',passwd='',database='kinhbac2')
my_cursor = cnx.cursor()
# query1 = 'CREATE DATABASE IF NOT EXISTS kinhbac2'
# query2 = 'SHOW DATABASES'
# query3 = "USE kinhbac2;CREATE TABLE sinhvien (id INT(6) PRIMARY KEY,diachi VARCHAR(30))"
query4 = "INSERT INTO sinhvien (sinhvien.id,sinhvien.diachi)VALUES('113', 'Nghe an')"
query5 = 'SELECT * FROM sinhvien'
my_cursor.execute(query4)
my_cursor.execute(query5)
for i in my_cursor:
    print(i)

cnx.close()