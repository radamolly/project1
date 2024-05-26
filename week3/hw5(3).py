# a = (25, 8000)
# b = (36, 16000)
# c = (49, 24000)

# d = a + b + c

# my_dict1 = {'key1':'nisa', 'value':a}
# my_dict2 = {'key2':'anan', 'value':b}
# my_dict3 = {'key3':'somchai', 'value':c}

# def calculate_sum(numbers):
#     return sum(numbers)

# d = a + b + c
# result1 = calculate_sum(d[0:5:2])
# print("อายุของพนักงานทุกคนรวมกันคือ", result1, "ปี")
# result2 = calculate_sum(d[1: :2])
# print("เงินเดือนของพนักงานทุกคนรวมกันคือ", result2, "บาท")

employee = {'Nisa': (25, 8000), 'Anan': (36, 16000), 'Somchai': (49, 24000)}

all_values = employee.values()

sum_salary = 0
sum_age = 0

for i in all_values:
    sum_age = sum_age + i[0]
    sum_salary = sum_salary + i[1]

print("อายุของพนักงานทุกคนรวมกันคือ", sum_age, "ปี และเงินเดือนของพนักงานรวมกันคือ", sum_salary, "บาท")