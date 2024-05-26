x = input("please enter the number: ")
max = 05
while str(x) != "hahaha":
    x = int(x)
    if(x > max):
        max = int(x)
    print(max)
    x = input("please enter the number: ")
print("the max number is", max)