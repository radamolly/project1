x = int(input("โปรดกรอกข้อมูลคะแนนสอบปลายภาคของนักเรียน : "))
y = list()
while x != -1:
    y.append(x)
    x = int(input("โปรดกรอกข้อมูลคะแนนสอบปลายภาคของนักเรียน : "))
ma = max(y)
mi = min(y)
c = y.index(ma)
d = y.index(mi)
n = len(y)
p = 0
f = 0
j = 0
average = sum(y)/len(y)
z = ''

zero = y.count('0')
one = y.count('1')
two = y.count('2')
three = y.count('3')
four = y.count('4')
five = y.count('5')
six = y.count('6')
seven = y.count('7')
eight = y.count('8')
nine = y.count('9')
ten = y.count('10')

ze = len(str(zero))
on = len(str(one))
tw = len(str(two))
th = len(str(three))
fo = len(str(four))
fi = len(str(five))
si = len(str(six))
se = len(str(seven))
ei = len(str(eight))
ni = len(str(nine))
te = len(str(ten))

a = 0

for a in y:
    if (ze > 1):
        a = a + 1
        z = ''
    elif(on > 1):
        a = a + 1
        z = ''
    elif(tw > 1):
        a = a + 1
        z = ''
    elif(th > 1):
        a = a + 1
        z = ''
    elif(fo > 1):
        a = a + 1
        z = ''
    elif(fi > 1):
        a = a + 1
        z = ''
    elif(si > 1):
        a = a + 1
        z = ''
    elif(se > 1):
        a = a + 1
        z = ''
    elif(ei > 1):
        a = a + 1
        z = ''
    elif(ni > 1):
        a = a + 1
        z = ''
    elif(te > 1):
        a = a + 1
        z = ''
    else:
        print("no")



for i in y:
    if(i > 8):
        j = j + 1
        print("คนที่", j, "ได้", i, "คะแนน เกรด A")
        p = p + 1
    elif(8 >= i and i > 5):
        j = j + 1
        print("คนที่", j, "ได้", i, "คะแนน เกรด B")
        p = p + 1
    else:
        j = j + 1
        print("คนที่", j, "ได้", i, "คะแนน เกรด F")
        f = f + 1
print("มีนักเรียนทั้งหมด", n ,"คน สอบผ่าน", p, "คน สอบตก", f, "คน มีคะแนนสูงสุด", ma, "คะแนน และคะแนนต่ำสุด", mi, "คะแนน โดยมีค่าเฉลี่ย", round(average,2) , "ผู้ที่มีคะแนนสูงสุดอยู่ตำแหน่งที่", c, "คะแนนต่ำสุดอยู่ตำแหน่งที่", d, "และมีคนได้คะแนนซ้ำกัน", a, "คน")