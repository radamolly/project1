def get_min_max(mytuple):
    max_number = max(mytuple)
    min_number = min(mytuple)
    return (max_number, min_number)

x = (1,2,6,7,9,5,4)

max, min = get_min_max(x)

print("ค่าที่มากที่สุดคือ",max)
print("ค่าที่น้อยที่สุดคือ",min)

