import csv

def check_grade(score):
    if score >= 80:
        return "A"
    elif score >= 75:
        return "B+"
    elif score >= 70:
        return "B"
    elif score >= 65:
        return "C+"
    elif score >= 60:
        return "C"
    elif score >= 55:
        return "D+"
    elif score >= 50:
        return "D"
    else:
        return "F"
    
with open('student.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        number, name, score = row
        print("เลขที่", number, "ชื่อ", name, "คะแนน", score, "ได้เกรด", check_grade(int(score)))