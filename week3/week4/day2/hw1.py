from datetime import date

user_input = input("Enter date (YYYY-MM-DD): ")

date_input = date.fromisoformat(user_input)

print("วันที่ user input เข้่ามาตรงกับ", date_input.strftime('%A'))

