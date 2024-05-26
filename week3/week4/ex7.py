my_list = []

def f2(a, b):
    for i in range(b):
        my_list.append(a)
    return my_list

a = input("a = ")
b = int(input("b = "))

print(f2(a, b))
