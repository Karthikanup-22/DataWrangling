# Reading JSON string
import json

json_string = '{"name": "Jack", "age": 30, "isEmployed": true}'

data = json.loads(json_string)

print(data['name'])  
print(data['isEmployed'])  




