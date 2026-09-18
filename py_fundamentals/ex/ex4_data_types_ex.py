# Excercise about List
tools = ["Python", "Cypress", "Playwright"]
print("Initial List - ", tools)
tools.append("Postman")
print("List after append() - ", tools)
tools.remove("Cypress")
print("List after remove() - ", tools)

# Excercise about Tuple
browsers = ("Chrome", "Firefox", "Edge")
print("Tuple - ", browsers)
print("2nd browser", browsers[1])

# This line will raise an error because tuples are immutable. So used try except
try:
    browsers[1] = "Safari"
except TypeError as error:
    print("Cannot modify a tuple -", error)

# Excercise about Set
languages = ["Python", "Python", "JavaScript", "Java", "TypeScript", "Java"]
print("Set - ", set(languages))

# Excercise about Dictionary
test_case = {"name": "Login Test", "status": "Passed", "priority": "High"}

print("Dictionary - ", test_case)
print(test_case["name"])
test_case["status"] = "Failed"
print("Updated Dictionary - ", test_case)
test_case["browser"] = "Chrome"
print("Dictionary after adding new key-value pair - ", test_case)
test_case["test"] = "test"
print("Dictionary after adding new key-value pair - ", test_case)
del test_case["test"]
print("Dictionary after deleting key-value pair - ", test_case)
