import pandas as pd

data = pd.read_csv('life_quality.csv')

df = pd.DataFrame(data)

print(df.groupby('City')['Quality Index'].mean())

print(df.groupby('City')['Crime Rate'].max())
print(df.groupby('City')['Crime Rate'].min())

print(df.loc[df['Population'].idxmax()]['City'])

print(df[df['Quality Index'] > 80])