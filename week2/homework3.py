x = str(input("please input the word : "))
y = list(x)
z = ""
b = 0
for i in y:
    if (i == 'a'):
        if( z == 'a'):
            b = b + 1
            z=''
        else:
            z = i
    elif(i=='e'):
        if(z == 'e'):
           b = b + 1
           z=''
        else:
            z = i
    elif(i=='i'):
        if(z == 'i'):
           b = b + 1
           z=''
        else:
            z = i
    elif(i=='o'): 
        if(z == 'o'):
           b = b + 1
           z=""
        else:
            z = i
    elif(i=='u'):
        if(z == 'u'):
           b = b + 1
           z=''
        else:
            z = i
    else:
           continue
    
print("ข้อมูลที่กรอกมามีอักษรทีี่ติดกัน" , b , "คู่")
    

