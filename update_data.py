import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='jimmy8689',
                                     database = 'student')
cursor = connection.cursor()

import json
with open('student_info.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
'''
for key in data:
    name = data[str(key)]['name']
    try:
        phone_number = str(data[str(key)]['phone_number'])
    except KeyError:
        phone_number = None

    # print(key, name, phone_number)
    cursor.execute('INSERT INTO `student` VALUES(%s, %s, %s)', (key, name, phone_number))
'''
for key in data:
    classes = data[str(key)]['class']
    for each_class in classes:
        date = each_class[0]
        date = date.replace('.', '-')
        try:
            amount = int(each_class[1])
        except ValueError:
            continue
        teacher = each_class[2]
        cursor.execute('INSERT INTO `classes`(`date`, `amount`, `teacher`, `student id`) VALUES(%s, %s, %s, %s)', (date, amount, teacher, key))

cursor.close()
connection.commit()
connection.close()