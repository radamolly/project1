score = float(input("Please enter the score: "))
summary = 0
i = 0
while score != -1:
    summary = summary + score

    i = i + 1
   # print(summary)
    # print(i)
    score = float(input("Please enter the score: "))
result = summary/i
print("ผลคะแนนเฉลี่ยของนักเรียน" , i , "คือ" , result)