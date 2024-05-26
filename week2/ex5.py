x = input("please enter the word : ")

y = len(x)

z = range(y)
text = ""
for i in z:
    text = text + x[i] + x[i]
print(text)