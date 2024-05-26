import pandas as pd

mydict = pd.read_json('profile.json')
df = pd.DataFrame(mydict)
print(df)
df.to_csv("profile2.csv", index=False)