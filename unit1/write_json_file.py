# Write JSON file
import json

data = {
    "name": "ravi",
    "age": 25,
    "skills": ["Python", "Data Science"],
    "isEmployed": True
}
with open('ram.json', 'w') as file:
    json.dump(data, file, indent=4)  
