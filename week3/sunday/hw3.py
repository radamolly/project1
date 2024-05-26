theset1 = {"0999999999"}
theset2 = {"0888888888"}
theset3 = {"0666666666"}

mydict1 = {'Key':'Somchai', 'Value': theset1}
mydict2 = {'Key':'Somying', 'Value': theset2}
mydict3 = {'Key':'Sommai', 'Value': theset3}

print(mydict1['Key'], mydict1['Value'])
print(mydict2['Key'], mydict2['Value'])
print(mydict3['Key'], mydict3['Value'])

theset1.update(["0828282828"])
theset1.remove("0999999999")
theset3.remove("0666666666")

print("เพิ่มหมายเลขโทรศัพท์", theset1, "ใหม่ ให้กับ", mydict1['Key'])
print("จะได้", mydict1['Key'], "มีหมายเลขโทรศัพท์", mydict1['Value'])
print("ลบหมายเลขโทรศัพท์ของ", mydict3['Key'])
print("ได้", theset3)
print("เบอร์ '0888888888' มีอยู่ใน", theset2, "หรือไม่")
print("0888888888" in theset2)

print(mydict1['Key'], mydict1['Value'])
print(mydict2['Key'], mydict2['Value'])
print(mydict3['Key'], mydict3['Value'])