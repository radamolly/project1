import pandas as pd

student = input("โปรดกรอกข้อมูลของนักเรียน : ")
x = []

while student != '-1':
    name, age, score = student.split(',')
    x.append({'name' : name, 'age' : age, 'score' : score})
    student = input("โปรดกรอกข้อมูลของนักเรียน : ")

mydict = [i for i in x if int(i['score']) > 70]

df = pd.DataFrame(mydict)
print(df)
df.to_csv("students.csv", index=False)

df.to_json("students.json", index=False, orient="records")