# x = str(input("please input the message : "))
# charac = set(x)
# s = len(charac)
# print(s)

x = []
for i in range(10):
    myinput = int(input("please input the number : "))
    x.append(myinput)
myx = [number for number in x if x.count(number) > 1]
myset = set(myx)
print(myset)