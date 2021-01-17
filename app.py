import json

x = {
    "name": "Cedd",
    "age": 24,
    "city": "Manila"
}

y = json.dumps(x)

print(y)