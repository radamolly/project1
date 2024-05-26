from datetime import date, datetime, time, timedelta

# def checkTodayIsMyBirthDay(birthday):
#     if birthday == date.today():
#         return True
#     else:
#         return False
# my_birth_day = date(2024,5,12)
# print(checkTodayIsMyBirthDay(my_birth_day))
thai_month = ['มกราคม', 'กุมพาพันธ์', 'มีนาคม', 'เมษายน', 'พฤษภาคม',
              'มิถุนายน', 'กรกฎาคม', 'สิงหาคม', 'กันยายน', 'ตุลาคม', 'พฤศจิกายน', 'ธันวาคม']
def get_thai_month(month):
    return thai_month[month-1]

my_delta = timedelta(days=2)
the_day_after_tomorrow = date.today() + my_delta

budhist_year = the_day_after_tomorrow.year + 543

print("อีกสองวันเป็นวันที่", the_day_after_tomorrow.strftime('%d'), get_thai_month(the_day_after_tomorrow.month), 'พ.ศ.', budhist_year)




