# Exercise 2 — List of dictionaries
# Use a loop to print only the failed test: Search


test_cases = [
    {"name": "Login", "status": "Passed"},
    {"name": "Search", "status": "Failed"},
    {"name": "Checkout", "status": "Passed"},
]

for tc in test_cases:
    if tc["status"] == "Failed":
        print(tc["name"])
