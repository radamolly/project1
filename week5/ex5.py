import csv
import random

def random_salary():
    return random.randrange(8900, 25000)

with open('employees.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'Name', 'Department', 'Salary'])
    writer.writerow(['1', 'John Doe', 'Sales', random_salary()])
    writer.writerow(['2', 'Jane Smith', 'Marketing', random_salary()])
    writer.writerow(['3', 'Bob Johnson', 'Engineering', random_salary()])
