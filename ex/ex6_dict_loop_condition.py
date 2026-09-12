test_results = {
    "Login": "Passed",
    "Search": "Failed",
    "Checkout": "Passed",
    "Logout": "Failed",
}

for test_case, result in test_results.items():
    print(f"Test Case: {test_case}, Result: {result}")

print("Failed Test Cases------------")
for test_case, result in test_results.items():
    if result == "Failed":
        print(test_case)
