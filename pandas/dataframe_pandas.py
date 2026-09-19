import pandas as pd

data = {
    "Test Case": ["Login", "Search", "Checkout", "Logout", "Profile"],
    "Status": ["Passed", "Failed", "Passed", "Failed", "Passed"],
    "Browser": ["Chrome", "Firefox", "Chrome", "Edge", "Chrome"],
    "Duration": [10, 15, 20, 8, 12],
}

print("Data- \n", data)

df = pd.DataFrame(data)
print("\nDataFrame- \n ", df)

print("Pandas Series-\n", df["Test Case"])

print("Pandas Series Test Case and Status-\n", df[["Test Case", "Status"]])

print("-----------")
print(df.iloc[0])  # First row
