# Exercise 3 — JSON
# Create Python dictionary Then
# Convert it to a JSON string using json.dumps().
# Print the JSON string.
# Convert the JSON string back into a Python object using json.loads().
# Print the status.

import json

test_result = {"name": "Login", "status": "Passed", "duration": 10}
test_result_json = json.dumps(test_result)
print(test_result_json)

test_result_py_obj = json.loads(test_result_json)
print(test_result_py_obj)
print(test_result_py_obj["status"])
