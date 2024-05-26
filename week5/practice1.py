import csv
with open('student.csv', 'w') as csvfile:
    reader = csv.reader(csvfile)

    next(reader)

    new_student = [(Name, Age, Grade) for Name, Age, Grade in reader if float(Grade) > 3.5]

    with open('student_new.csv', 'w') as writfile:
        writer = csv.writer(writfile)
        writer.writerow(['Name', 'Age', 'Grade'])
        for i in new_student:
            writer.writerow([i[0], i[1], i[2]])