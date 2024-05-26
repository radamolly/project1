x = int(input("please input number"))
if(x >= 45 and x <= 55):
    print("you win a first prize")
elif(x >= 15 and x <= 30 or x >= 75 and x <= 90):
    print("you win a second prize")
else:
    print("sorry, you got no prize")