import numpy as np
import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, np.nan, 35, np.nan, 45],
    'city': ['New York', 'London', None, 'Tokyo', 'Sydney']
}
df = pd.DataFrame(data)
# print(df.fillna(0))
print(df.fillna(df['age'].min()))


# print(df.dropna(axis=1))
# print(df)

# print(df.isnull().sum())
# print(df[df.isnull().any(axis=1)])
# print(df.dropna())