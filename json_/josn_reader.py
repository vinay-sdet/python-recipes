import json

with open("json_/emp.json", "r") as file:
    emp_data = json.load(file)
print("Employee Data from JSON file - ", emp_data)
print("Employee Name from JSON file - ", emp_data["name"])
print("Employee Role from JSON file - ", emp_data["role"])
print("Employee Skills from JSON file - ", emp_data["skills"])
