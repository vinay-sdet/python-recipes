# Ex5 Do the following:

# Find the missing values.
# Replace missing Status with "Unknown".
# Replace missing Duration with the average duration.
# Print the cleaned DataFrame.

import pandas as pd

data = {
    "Test Case": ["Login", "Search", "Checkout", "Logout"],
    "Status": ["Passed", "Failed", None, "Passed"],
    "Duration": [10, 15, None, 8],
}

df = pd.DataFrame(data)
print("Missing values\n", df.isnull())
print("Missing values per column\n", df.isnull().sum())
df["Status"] = df["Status"].fillna("Unknown")
df["Duration"] = df["Duration"].fillna(df["Duration"].mean())

print("\nCleared Dataframe:")
print(df)
