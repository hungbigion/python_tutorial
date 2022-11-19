import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="kinhbac"
)

mycursor = mydb.cursor()

sql = "INSERT INTO sinhvien (ID, name) VALUES (%s, %s)"
val = ("121", "nguyen huu hung")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")