import json

data = {"name": "Ali", "age": 22}

with open("data.json", "w") as f:
    json.dump(data, f)
