import json

family = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}

json_file = "file.json"

with open(json_file, 'w') as file_obj:
    json.dump(family, file_obj, indent = 2, sort_keys=True)
