import pandas as pd

data = {'product': ['A', 'B', 'C', 'A', 'B', 'C'],
        'store': ['X', 'X', 'X', 'Y', 'Y', 'Y'],
        'sales': [100, 200, 150, 120, 180, 200]}
df = pd.DataFrame(data)
print(df)

# store_group = df.groupby('store')
# print(store_group)

# store_product_group = df.groupby(['store', 'product'])
# print(store_product_group)

# sales_sum = df.groupby('store')['sales'].sum()
# print(sales_sum)

sales_stats = df.groupby('product')['sales'].agg(['sum', 'mean', 'min', 'max'])
print(sales_stats)
print("hello")