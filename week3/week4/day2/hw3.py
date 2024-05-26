from random import sample
x = list(range(1,101))
sample_of_x = sample(x,20)
print(sorted(sample_of_x))

# numbers = []

# print("Random numbers:")
# for i in range(20):
#     n = sample(1, 101)
#     print(n, end =' ')
#     numbers.append(n)

# sorted_list = sorted(numbers)
# print(sorted_list)