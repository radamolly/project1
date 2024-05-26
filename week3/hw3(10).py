# students1 = ('sam', 8)
# students2 = ('lily', 10)
# students3 = ('bob', 2)
# students4 = ('jin', 5)
# students5 = ('hannah', 7)
# students = []
# s = students1 + students2 + students3 + students4 + students5
# students.append(s)

# summary = sum(s[1:10:2])
# average = summary/5

# print("ค่าเฉลี่ยคะแนนสอบของนักเรียนทั้ง 5 คนคือ", round(average,2), "คะแนน")

number_of_student = range(2)
list_of_student = []
for i in number_of_student:
    name = input("กรอกชื่อนักเรียน")
    score = int(input("กรอกคะแนน"))
    student = (name, score)
    list_of_student.append(student)

x = [score for name, score in list_of_student]

result = sum(x)/len(number_of_student)
print("ค่าเฉลี่ยคะแนนสอบของนักเรียนทั้งหมด", result)
