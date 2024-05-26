import pandas as pd

data = pd.read_csv('life_quality.csv')

df = pd.DataFrame(data)

print(df.loc[(df['Crime Rate'] > 2.5) & (df['City'] == 'Sydney'), 'City'])