import json

# สร้างออบเจ็กต์ Python
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "music"],
    "married": False
}

# แปลงออบเจ็กต์ Python เป็นสตริง JSON
json_string = json.dumps(data)
print("JSON string:", json_string)

# แปลงสตริง JSON เป็นออบเจ็กต์ Python
parsed_data = json.loads(json_string)
print("Parsed data:", parsed_data)

# เขียนออบเจ็กต์ Python เป็น JSON ลงในไฟล์
with open("data.json", "w") as file:
    json.dump(data, file)

# อ่านไฟล์ JSON และแปลงเป็นออบเจ็กต์ Python
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print("Loaded data:", loaded_data)