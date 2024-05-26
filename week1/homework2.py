plan = 1,2
plan = int(input("please enter the number of plan : "))
minute = int(input("please enter the number of minutes you spent : "))
x = minute - 200
y = minute - 500
if (plan == 1):
    if (minute > 200 and x <= 100):
        charge1 = 399 + x
        print("you use plan 1", minute, "minutes, your charge is", charge1 , "baht")
    elif (minute > 200 and x > 100):
        charge2 = (x/2) + 399
        print("you use plan 1", minute, "minutes, your charge is", charge2 , "baht")
    else:
        print("you use plan 1", minute, "minutes, your charge is 399 baht")
else:
    if (minute > 500):
        charge3 = 499 + (y*0.5)
        print("you use plan 2", minute, "minutes, your charge is", charge3 , "baht")
    elif (minute <= 500 and minute > 200):
        charge4 = 499 - ((499*3)/100)
        print("you use plan 2", minute, "minutes, your charge is", charge4 , "baht")
    elif (minute <= 200):
        charge5 = 499 - ((499*5)/100)
        print("you use plan 2", minute, "minutes, your charge is", charge5 , "baht")
    else:
        print("you use plan 2", minute, "minutes, your charge is 499 baht")


        
