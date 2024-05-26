x = input("please input number : ")
x = int(x)
x = range(1, x+1)
result = []
for i in x :
    if ((i % 3 == 0) or (i % 5 == 0)):
        result = result.append(x)

    print(result)