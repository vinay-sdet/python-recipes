import pandas as pd

data = {
    "Test Case": ["Login", "Search", "Checkout"],
    "Status": ["Passed", "Failed", "Passed"],
    "Browser": ["Chrome", "Firefox", "Chrome"],
    "Duration": [10, 15, 20],
}
df = pd.DataFrame(data)
# Failed test cases
failed_testcases = df[df["Status"] == "Failed"]
print("Failed Test Cases:\n", failed_testcases)
# Chrome test cases
chrome_tests = df[df["Browser"] == "Chrome"]
print("Chrome Test Cases:\n", chrome_tests)

# Filtering with multiple conditions
# Passed test cases running on Chrome
result = df[(df["Status"] == "Passed") & (df["Browser"] == "Chrome")]
print("Passed Test Cases on Chrome:\n", result)

sorted_df = df.sort_values("Duration", ascending=False)
print("Sorted DataFrame by Duration (Descending):\n", sorted_df)

print("Mean Duration of Test Cases:", df["Duration"].mean())
print("Max Duration of Test Cases:", df["Duration"].max())
print("Min Duration of Test Cases:", df["Duration"].min())
print("Total Duration of Test Cases:", df["Duration"].sum())


print("----------- ")
print(df.info())
print("----------- ")
print(df.describe())
