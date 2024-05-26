import json

# with open("profile.json", "r") as file:
#     loaded_data = json.load(file)
#     print("สวัสดี", loaded_data['name'], "คุณอายุ", loaded_data['age'], "คุณอาศัยอยู่ที่", loaded_data['city'])

profile = {"name" : "Rada", "age" : 15, "city" : "Chiang Mai"}

old_value = []
with open("profile.json", "r") as file:
    old_value = json.load(file)

old_value.append(profile)

with open("profile.json", "w") as file:
    json.dump(old_value,file)
