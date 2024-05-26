import pandas as pd

data = {'year': [2021, 2021, 2021, 2021, 2022, 2022, 2022, 2022],
        'quarter': ['Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4'],
        'sales': [100, 120, 130, 150, 110, 130, 140, 160]}
df = pd.DataFrame(data)
print(df)