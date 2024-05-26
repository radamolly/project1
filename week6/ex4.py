import pandas as pd
data = {'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'value': [100, 200, 300]}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
print(df[(df['date'] >= '2023-01-01') & (df['date'] <= '2023-01-02')])

delta = df['date'].max() - df['date'].min()
print(delta)