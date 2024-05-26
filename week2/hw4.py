p = 1,2,3,4,5
p = int(input("หมุนตำแหน่งของสมาชิกในลิสต์รายชื่อผลไม้ไปทางขวากี่ตำแหน่ง : "))
a = ['mango','apple','banana','coconut','grape']
b = ['grape','mango','apple','banana','coconut']
c = ['coconut','grape','mango','apple','banana']
d = ['banana','coconut','grape','mango','apple']
e = ['apple','banana','coconut','grape','mango']

if(p == 1):
    print(a)
elif(p == 2):
    print(b)
elif(p == 3):
    print(c)
elif(p == 4):
    print(d)
else:
    print(e)
