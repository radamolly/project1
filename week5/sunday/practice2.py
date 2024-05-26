import pandas as pd

x = input("โปรดกรอกข้อมูลของนักเรียน : ")
z = []

while x != '-1':
    name, age, score = x.split(',')
    z.append({'name': name, 'age': age, 'score': score})
    x = input("โปรดกรอกข้อมูลของนักเรียน : ")

mydict = [i for i in z if int(i['score']) > 90]

df = pd.DataFrame(mydict)
print(df)
df.to_csv("data_student.csv", index=False)

#  to json witout index
df.to_json("data_student.json", index=False, orient="records")

# mydict = pd.read_json('profile.json')
# df = pd.DataFrame(mydict)
# print(df)
# df.to_csv("profile2.csv", index=False)
