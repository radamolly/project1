import pandas as pd

data = pd.read_csv('week6/sunday/student.csv')
df = pd.DataFrame(data)

# df[['first_name', 'last_name']] = df['name'].str.split(' ', expand=True)
# print(df)

df.apply()
def changing_prefix(x):
    for i in df['prefix']:
        if i == 'เด็กชาย':
            return 'ด.ช.'(x)
    print(x)
df['full_name'] = df['prefix'].str.cat(df['first_name'].str.cat(df['last_name'], sep=' '))
print(df)
