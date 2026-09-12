test_results = {
    "Login": "Passed",
    "Search": "Failed",
    "Checkout": "Passed",
    "Logout": "Failed",
}


def verify_tests(test_results) -> list:
    passed_tests, failed_tests, total_tests = 0, 0, 0
    pass_percentage = 0.00
    for test_case, results in test_results.items():
        total_tests += 1
        if results == "Passed":
            passed_tests += 1
        else:
            failed_tests += 1
    if total_tests > 0:
        pass_percentage = (passed_tests / total_tests) * 100
    return passed_tests, failed_tests, total_tests, pass_percentage


passed_tests, failed_tests, total_tests, percentage = verify_tests(test_results)
print(
    f"Total Tests: {total_tests}, Passed Tests: {passed_tests}, Failed Tests: {failed_tests}, Pass Percentage: {percentage:.2f}%"
)
