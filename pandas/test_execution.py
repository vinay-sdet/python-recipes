import pandas as pd

df = pd.read_csv("pandas/test_execution_results.csv")

print("First 5 rows\n", df.head(5))
print("Shape - ", df.shape)
print("Column Names\n", df.columns.tolist())
print("Dataframe information\n", df.info())
