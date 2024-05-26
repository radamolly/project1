number_of_student = range(2)
students = {}
for i in number_of_student:
    name = input("กรอกชื่อนักเรียน")
    score = int(input("กรอกคะแนน"))
    students.update({name:score})

max_score = max(students.values())

new_students = [(name, score) for name, score in students.items() if score == max_score]

print(new_students)

for i in new_students:
    print("ผู้ที่ได้คะแนนสูงสุดคือ", i[0], "ได้คะแนน", i[1])