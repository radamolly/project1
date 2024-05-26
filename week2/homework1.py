x = str(input("please enter the string : "))
y = len(x)
z = list(x)
sum = 0
j = 0
for i in z:
    i = int(i)
    if (i % 2 == 0):
        continue
    print(i, end=",")
    sum = sum + i
    j = j + 1
print("ค่าที่รับเข้ามามีจำนวน", y, "ตัว มีจำนวนเลขคี่ทั้งหมด", j , "ตัว ผลรวมของเลขคี่คือ", sum)