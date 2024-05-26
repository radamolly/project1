def h(x):
    y = [i for i in x if i % 2 == 0]
    return y
print(h([5, 1, 3, 7, 8]))