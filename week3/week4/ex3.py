def FindEvenNumber(x):
    if x % 2 == 0:
        return True
    else:
        return False

list_of_even_number = []
for i in range(5):
    x = int(input("โปรดกรอกตัวเลข : "))
    if (FindEvenNumber(x)):
        list_of_even_number.append(x)

total = len(list_of_even_number)

print("จำนวนที่เป็นเลขคู่มีทั้งหมด", total, "ตัว คือ", list_of_even_number)


square = lambda x = 5 : x ** 2
print(square())
