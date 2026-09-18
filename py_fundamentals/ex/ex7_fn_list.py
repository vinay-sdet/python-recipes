test_results = {
    "Login": "Passed",
    "Search": "Failed",
    "Checkout": "Passed",
    "Logout": "Failed",
}


def verify_passed_tests(test_results) -> list:
    passed_tests = []
    for test_case, results in test_results.items():
        if results == "Passed":
            passed_tests.append(test_case)
    return passed_tests


print("Passed test cases are ", verify_passed_tests(test_results))
