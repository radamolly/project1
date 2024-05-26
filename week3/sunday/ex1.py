teacher_input = input("Please input 'T' if you want to continue : ")

students = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

students_length = len(students)

while teacher_input == 'T' and len(students) > 1:
    unlucky_student = students.pop()
    print("เสียใจด้วยกับนักเรียนเลขที่", unlucky_student)
    teacher_input = input("Please input 'T' if you want to continue : ")

print("ผู้โชคดีของเราคือ", students)