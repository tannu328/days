import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        print(json.dumps(data, indent=4))

file_path = 'file.json'
read_json_file(file_path)
