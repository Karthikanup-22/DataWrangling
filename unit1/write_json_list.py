
import json

data = [
    {"name": "raju", "age": 25},
    {"name": "ramana", "age": 30}
]

with open('data222.json', 'w') as file:
    
    json.dump(data, file, indent=2)






