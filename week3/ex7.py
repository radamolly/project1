input_student = input("กรอกชื่อและคะแนนโดยคั่นด้วยเครื่องหมาย , :")

name, score = input_student.split(',')

student_score = {}

while int(input_student) != -1 :
    student_score[name] = score
    input_student = input("กรอกชื่อและคะแนนโดยคั่นด้วยเครื่องหมาย , :")
    name, score = input_student.split(',')

print(student_score)

