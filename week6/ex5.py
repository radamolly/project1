import pandas as pd

data1 = {'A': ['A0', 'A1', 'A2'],
         'B': ['B0', 'B1', 'B2']}
df1 = pd.DataFrame(data1)

data2 = {'A': ['A3', 'A4', 'A5'],
         'B': ['B3', 'B4', 'B5']}
df2 = pd.DataFrame(data2)
concat_df = pd.concat([df1, df2])
print(concat_df)