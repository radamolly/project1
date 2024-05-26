import csv

# with open('employees_dict.csv', 'w', newline='') as csvfile:
#     fieldnames = ['ID', 'Name', 'Department', 'Salary']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'ID': '1', 'Name': 'John Doe', 'Department': 'Sales', 'Salary': 12000})
#     writer.writerow({'ID': '2', 'Name': 'Jane Smith', 'Department': 'Marketing', 'Salary': 20000})
#     writer.writerow({'ID': '3', 'Name': 'Bob Johnson', 'Department': 'Engineering', 'Salary': 25000})
#     writer.writerow({'ID': '4', 'Name': 'Rada', 'Department': 'CEO', 'Salary': 30000})

with open('employees_dict.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(dict(row))