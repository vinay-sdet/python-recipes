# Exercise 2 — Read the CSV
# Read the file you just created using:
# pd.read_csv()
# Print:
# first 3 rows
# shape
# column names

import pandas as pd

df = pd.read_csv("pandas/ex1_test_results.csv")
print("Test Data:")
print(df.head(3))
print("Shape:", df.shape)
print("Column Names:", df.columns.tolist())

# Tests that failed and took more than 10 seconds.
print("\nTests that failed and took more than 10 seconds:")
print(df[(df["Status"] == "Failed") & (df["Duration"] >= 10)])
