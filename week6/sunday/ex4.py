import pandas as pd

data = {'name': ['John Doe', 'Jane Doe', 'John Smith', 'Jane Smith'],
        'email': ['john.doe@example.com', 'jane.doe@gmail.com', 'john.smith@example.com', 'jane.smith@example.com']}
df = pd.DataFrame(data)
print(df)

mask = df['email'].str.contains('@example.com')
print(df[mask])