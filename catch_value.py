import pandas as pd
import numpy as np
import json

df = pd.read_csv('payment record.csv')

# ==== turn csv to json ====
student = {}
# row, col = df.shape
# print(row, col)
for row in range(0,7956,3):
    temp = []
    for col in range(75):
        if not df.isnull().iloc[row, col]:
            value = df.iloc[row:row+3, col].dropna().values
            if len(value) == 3:
                if value[0] == value[1] == value[2]:
                    value = value[0]
                    if type(value) == np.int64:
                        id = int(value)
                        student[id] = {}
                    else:
                        student[id]['name'] = value
                elif value[0] != '日期':
                    temp.append(value.tolist())
            elif col == 2:
                student[id]['phone_number'] = value.tolist()        

        student[id]['class'] = temp

# print(student)

with open('student_info.json', 'w', encoding='utf8') as f:
    json.dump(student, f, ensure_ascii=False)

            
    
