import json

employee = {
    "name": "Vinay",
    "role": "SDET",
}

print("Employee Dictionary - ", employee)
json_data = json.dumps(employee)
print("JSON Data - ", json_data)
