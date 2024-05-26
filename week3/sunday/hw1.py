x = []
y = []
for i in range(7):
    myinput1 = int(input("please input the numbers of the first set : "))
    x.append(myinput1)

for i in range(7):
    myinput2 = int(input("please input the numbers of the second set : "))
    y.append(myinput2)

xx = set(x)
yy = set(y)

print(xx)
print(yy)

intersection_set = xx & yy
different_set = (xx - yy) | (yy - xx)
sym_diff_set = xx.symmetric_difference(yy)

print("จำนวนสมาชิกที่เหมือนกันใน set ทั้งสองคือ", len(intersection_set))
print("จำนวนสมาชิกที่แตกต่างกันใน set ทั้งสองคือ", len(different_set))
print("สมาชิกที่ปรากฏใน set ใด set หนึ่ง แต่ไม่ได้ปรากฏในอีก set หนึ่งคือ", sym_diff_set)