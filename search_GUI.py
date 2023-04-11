import tkinter as tk
import mysql.connector
import tkinter.scrolledtext as tkst
from tkinter import ttk
from tkinter import messagebox

connection = mysql.connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='password',
                                     database = 'student')

cursor = connection.cursor()

# ==== function part ====

def ListClasses(name):
    cursor.execute("SELECT `date`, `amount`, `teacher`\
                    FROM `classes`\
                    WHERE `student id` = (SELECT `student id`FROM `student`WHERE `name` = '%s');" % name)
    index = cursor.fetchall()
    for index in index:
        index = list(index)
        string = '日期:{:11}${:7}老師:{}\n'.format(index[0], str(index[1]), index[2])
        text.insert(tk.END, string)
        text.tag_add('center', '1.0', 'end')

def classes_Count(name):
    cursor.execute("SELECT COUNT(`student id`) FROM `classes` WHERE `student id` = (\
                    SELECT `student id`\
                    FROM `student`\
                    WHERE `name` = '%s');" % name)
    
    index = str(cursor.fetchall()[0][0])
    count_text.set('繳費'+index+'次')

def total_amount(name):
    cursor.execute("SELECT SUM(`amount`) FROM `classes` WHERE `student id` = (\
                    SELECT `student id`\
                    FROM `student`\
                    WHERE `name` = '%s');" % name)
    
    amount = str(cursor.fetchall()[0][0])
    totalCost_text.set('總金額:$'+amount)

def find_number(name):
    cursor.execute("SELECT `phone number`\
                   FROM `student`\
                   WHERE `name` = '%s';" % name)
    record = cursor.fetchall()
    if record[0][0] == None:
        numbers = None
        phone_text.set('電話: 查無紀錄')
    else:
        numbers = record[0][0]
        numbers = numbers[1:-1]
        numbers = numbers.replace("'", '')
        phone_text.set('電話: '+numbers)

def startSearch(name):
    text.delete(1.0, tk.END)
    ListClasses(name)
    classes_Count(name)
    total_amount(name)
    find_number(name)  

def comboBox_selected(event):
    startSearch(stu_comboBox.get())

def comboBox(name_list):
    stu_comboBox['values'] = name_list
    stu_comboBox.pack()
    stu_comboBox.current(0)
    stu_comboBox.bind('<<ComboboxSelected>>', comboBox_selected)

def wildcard(name):
    cursor.execute("SELECT `name` FROM `student` WHERE `name` LIKE '%s';" % ('%'+name+'%'))
    record = cursor.fetchall()
    name_list = []
    for names in record:
        name_list.append(names[0])
    
    if len(name_list) == 1:
        startSearch(name_list[0])
    elif not name_list:
        messagebox.showinfo('Error', '查無此人')
    else:
        comboBox(name_list)

def onClick():
    text.delete(1.0, tk.END)
    stu_comboBox.pack_forget()
    count_text.set('')
    totalCost_text.set('')
    phone_text.set('')
    name = entry.get()
    wildcard(name)
    
# ==== flow chart ====
# type names in Entry and then click Search button(def onClick => def wildcard)
# func wildcard to find out if the input is unique, if not jump comboBox to select
# choose the name you want to search and it will show all the info

# ==== Tkinter part ====
window = tk.Tk()
window.title('westgolf searcher')
window.geometry('500x230')
window.resizable(False, False)

frame = tk.Frame(window)
frame.pack()
entry = tk.Entry(frame, width=10, justify='center')
entry.grid(column=0, row=0)
button = tk.Button(frame, text='search', command=onClick)
button.grid(column=1, row=0)
text = tkst.ScrolledText(window, width=40, bd=2, height=10)
text.tag_configure('center', justify='center')
text.pack()

frame1 = tk.Frame(window)
frame1.pack()
count_text = tk.StringVar()
totalCost_text = tk.StringVar()
phone_text = tk.StringVar()
countText_label = tk.Label(frame1, textvariable=count_text)
countText_label.grid(column=0, row=0)
totalCost_label = tk.Label(frame1, textvariable=totalCost_text)
totalCost_label.grid(column=1, row=0)
number_label = tk.Label(window, textvariable=phone_text)
number_label.pack()

comboBox_text = tk.StringVar()
stu_comboBox = ttk.Combobox(window, textvariable=comboBox_text, state='readonly')

window.mainloop()
