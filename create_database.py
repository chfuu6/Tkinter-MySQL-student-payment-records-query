import mysql.connector

# ==== practice using python to connect mySQL ====
connection = mysql.connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='jimmy8689',
                                     database = 'student')

cursor = connection.cursor()
# cursor.execute('CREATE DATABASE `student`;')
cursor.execute('SHOW DATABASES;')
records = cursor.fetchall()
for r in records:
    print(r)

cursor.close()
connection.close()