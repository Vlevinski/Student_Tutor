import json

dj = {
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

print(json.dumps(dj, indent=4))
with open("jsonme.json","w") as f:
    json.dump(dj,f)
print("Done")

with open("jsonme.json","r") as f:
    data = json.load(f)

print(data)
