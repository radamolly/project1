import pandas as pd

mydict = {"name":["Somchai", "Somying", "Manop", "Piti"], 
          "score":[10, 20, 30, 40]}
x = pd.DataFrame(mydict)
print(x)