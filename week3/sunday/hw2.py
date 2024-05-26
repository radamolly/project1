a = []
for i in range(5):
    x = str(input("please input the string : "))
    list_a = a.append(x)

new_set = {x for x in a if len(x) > 5}
print(new_set)