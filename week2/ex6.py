x = input("please enter the word : ")
y = len(x)
z = range(y)
text = ""
last_value = ""
for i in z:
    if (last_value == x[i]):
        continue
    last_value = x[i]
    text = text + x[i] + x[i]
print(text)