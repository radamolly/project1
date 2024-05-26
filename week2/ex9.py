x = int(input("please input the number : "))
y = list()
while x != -1:
    y.append(x)
    x = int(input("please input the number : "))
average = sum(y)/len(y)
ma = max(y)
mi = min(y)
a = y.index(ma)
b = y.index(mi)
print("ค่าเฉลี่ยคือ", average, "ค่าสูงสุดคือ", ma, "อยู่ในลำดับที่", a, "และค่าต่ำสุดคือ", mi, "อยู่ในลำดับที่", b)

