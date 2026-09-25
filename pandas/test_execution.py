import pandas as pd

df = pd.read_csv("pandas/test_execution_results.csv")

print("First 5 rows\n", df.head(5))
print("Shape - ", df.shape)
print("Column Names\n", df.columns.tolist())
print("Dataframe information\n", df.info())

print("\nMissing values\n", df.isnull().sum())
print("\nData types\n", df.dtypes)
print("\nSummary statistics\n", df.describe())
print("\nLast 5 rows\n", df.tail(5))
