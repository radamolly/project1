import pandas as pd

data = pd.read_csv('activities.csv')

df = pd.DataFrame(data)

print(df.groupby('Activity')['Duration (hrs)'].mean())
print(df.groupby('Activity')['Calories Burned'].max())
print(df.groupby('Activity')['Calories Burned'].min())
print(df.loc[df['Duration (hrs)'].idxmax()]['Activity'])
print(df[df['Calories Burned'] > 400])
