def calculate_grade(student_dict):
    score = student_dict.values()
    score = list(score)[0]
    name = list(student_dict.keys())[0]
    if score >= 80:
        print(name, "ได้เกรด A")
    elif score >= 70:
        print(name, "ได้เกรด B")
    elif score >= 60:
        print(name, "ได้เกรด C")
    elif score >= 50:
        print(name, "ได้เกรด D")
    else:
        print(name, "คก")

students = [{"Somchai": 84}, {'Somying': 65}, {"Sompop": 97}, {"Manob": 49}]
for i in students:
    calculate_grade(i)