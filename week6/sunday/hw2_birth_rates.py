import pandas as pd

data = pd.read_csv('birth_rates.csv')

df = pd.DataFrame(data)

print(df.groupby('Country')['Birth Rate'].mean())

print(df.groupby('Country')['Birth Rate'].max())
print(df.groupby('Country')['Birth Rate'].min())

print(df.loc[(df['Year'] == 2023), 'Country'])

print(df[df['Year'] >= 2015])