import mysql.connector

# ==== testing here to make sure i get the right value ====
connection = mysql.connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='jimmy8689',
                                     database = 'student')
cursor = connection.cursor()

def all_classes():
    cursor.execute("SELECT `date`, `amount`, `teacher`\
                    FROM `classes`\
                    WHERE `student id` = (SELECT `student id`FROM `student`WHERE `name` = '%s');" % '盧弘忠')

    index = cursor.fetchall()
    for index in index:
        index = list(index)
        print('日期:{:11}${:7}老師:{}'.format(index[0], str(index[1]), index[2]))

def classes_Count():
    cursor.execute("SELECT COUNT(`student id`) FROM `classes` WHERE `student id` = (\
                    SELECT `student id`\
                    FROM `student`\
                    WHERE `name` = '%s');" % '盧弘忠')
    
    index = cursor.fetchall()[0][0]

def total_amount():
    cursor.execute("SELECT SUM(`amount`) FROM `classes` WHERE `student id` = (\
                    SELECT `student id`\
                    FROM `student`\
                    WHERE `name` = '%s');" % '盧弘忠')
    
    amount = cursor.fetchall()[0][0]

def find_number():
    cursor.execute("SELECT `phone number` FROM `student` WHERE `name` = '%s';" % '林宗翰')
    record = cursor.fetchall()
    if record[0][0] == None:
        numbers = None
    else:
        numbers = record[0][0]
        numbers = numbers[1:-1]
        numbers = numbers.replace("'", '')
    print(numbers)

def wildcard():
    cursor.execute("SELECT `name` FROM `student` WHERE `name` LIKE '%s';" % ('%'+'西'+'%'))
    record = cursor.fetchall()
    print(record)
    name_list = []
    for names in record:
        name_list.append(names[0])
    

all_classes()
# classes_Count()
# total_amount()
# find_number()
# wildcard()

cursor.close()
connection.close()
