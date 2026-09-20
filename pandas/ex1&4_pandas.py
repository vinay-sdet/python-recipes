# Ex 1 & 4 Create a DataFrame using:
# Save it as:
# test_results.csv

import pandas as pd

data = {
    "Test Case": ["Login", "Search", "Checkout", "Logout", "Profile"],
    "Status": ["Passed", "Failed", "Passed", "Failed", "Passed"],
    "Browser": ["Chrome", "Firefox", "Chrome", "Edge", "Chrome"],
    "Duration": [10, 15, 20, 8, 12],
}

df = pd.DataFrame(data)

df.to_csv("pandas/ex1_test_results.csv", index=False)

df.to_json("pandas/ex4_test_results.json", orient="records", lines=True)

df = pd.read_json("pandas/ex4_test_results.json", orient="records", lines=True)
print("------------------")
print(df)
