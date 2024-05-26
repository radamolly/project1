import pandas as pd

data = pd.read_json("company.json")
# no header
list_employee = data.to_dict(orient='records')

def calculate_salary(row):
    vat = (14 / 100)
    if (row['age'] > 30 and row['age'] < 40):
        vat = vat - (2 / 100)
    elif (row['age'] > 40 and row['age'] < 50):
        vat = vat - (4 / 100)
    elif (row['age'] > 50 and row['age'] < 60):
        vat = vat - (6 / 100)
    else:
        vat = vat - (8 / 100)

    if row['gender'] == 'male':
        vat = vat - (1 / 100)
    else:
        vat = vat - (1.5 / 100)

    salary = row['salary'] - (row['salary'] * vat)
    row['vat'] = vat
    row['net_salary'] = calculate_salary

    return row

z = []
for row in list_employee:
    new_row = calculate_salary(row)
    z.append(new_row)

df = pd.DataFrame(z)
df.to_csv('company.csv', index=False)