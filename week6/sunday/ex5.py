import pandas as pd

data = {'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'sales': [100, 120, 150, 200, 180]}
df = pd.DataFrame(data)
print(df)

df.plot(x='month', y='sales', kind='line')