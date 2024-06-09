import pandas as pd

data = pd.read_csv('emojis.csv')

df = pd.DataFrame(data)

print(df.groupby('Emoji')['Usage Count'].mean())

print(df.loc[df.groupby('Emoji')['Usage Count'].idxmax()])

print(df.groupby('User')['Usage Count'].agg(['max','min']))

print(df[df['Usage Count'] > 70])