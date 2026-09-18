employee = {
    "name": "Vinay",
    "role": "SDET",
    "skills": ["Python", "JavaScript", "Cypress"],
}

print("Employee Dictionary - ", employee)
print("Employee Name - ", employee["name"])
print("Employee Role - ", employee["role"])
print("Employee Skills - ", employee["skills"])

for skill in employee["skills"]:
    print(skill)

print("---- Employee Skill - ", employee["skills"][0])

# Nested Dictionary
employee = {
    "name": "Vinay",
    "contact": {"email": "vinay@example.com", "phone": "1234567890"},
}

print("Employee Contact-email - ", employee["contact"]["email"])

# Real world example

test_case = {
    "name": "Login Test",
    "status": "Failed",
    "browser": {"name": "Chrome", "version": "140"},
    "tags": ["login", "smoke", "regression"],
}

print("Test Case Tags - ", test_case["tags"][1])
