import mysql.connector as mysql

db_name = input("tên: ")
cnx = mysql.connect(host='localhost',user='root',passwd='')
my_cursor = cnx.cursor()
query1 = 'CREATE DATABASE IF NOT EXISTS {}'
query3 = "USE {};CREATE TABLE sinhvien (id VARCHAR(30) PRIMARY KEY,diachi VARCHAR(30))"
my_cursor.execute(query1.format(db_name))
my_cursor.execute('SHOW DATABASES')
for i in my_cursor:
    print(i)

cnx.close()