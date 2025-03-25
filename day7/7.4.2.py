import json

def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


data = {
    "name": "yash",
    "age": 22,
    "city": "rajkot"
}
file_path = 'new.json'  
write_json_file(file_path, data)
