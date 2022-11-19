import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=KANGTA\SQLEXPRESS;'
                      'Database=QLSV;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute('SELECT * FROM AccountSV')

for i in cursor:
    print(i)