import pandas as pd

data = {'year': [2021, 2021, 2021, 2021, 2022, 2022, 2022, 2022],
        'quarter': ['Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4'],
        'sales': [100, 120, 130, 150, 110, 130, 140, 160]}
df = pd.DataFrame(data)
print(df)

pivot_df = df.pivot(index='year', columns='quarter', values='sales')
# print(pivot_df)

melted_df = pivot_df.reset_index().melt(id_vars='year', var_name='quarter', value_name='sales')
print(melted_df)