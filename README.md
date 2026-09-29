# Python Recipes

A hands-on Python learning repository focused on fundamentals, data structures, JSON handling, NumPy, and pandas.

## Overview

This project is a collection of small scripts and exercises designed to build practical Python skills step by step. It covers:

- Python basics: variables, operators, loops, conditionals, functions, and strings
- data structures: lists, dictionaries, and nested data
- exception handling and debugging
- reading and processing JSON data
- NumPy arrays, broadcasting, and basic numeric operations
- pandas DataFrames, filtering, CSV/JSON examples, and data exploration

## Project structure

```text
python-recipes/
├── README.md
├── .venv/                               # local virtual environment
├── json_/                               # JSON examples and sample datasets
│   ├── emp.json
│   ├── json_ex.py
│   └── josn_reader.py
├── numpy/                               # NumPy exercises
│   ├── array_operations.py
│   ├── broadcasting_2d_array.py
│   ├── ex1_ex2_numpy.py
│   └── numpy_basics.py
├── pandas/                              # pandas exercises and CSV/JSON files
│   ├── boolean_filtering.py
│   ├── csv_&_json.py
│   ├── dataframe_pandas.py
│   ├── ex1&4_pandas.py
│   ├── ex2&3_pandas.py
│   ├── ex5_pandas.py
│   ├── ex1_test_results.csv
│   ├── ex4_test_results.json
│   ├── test_execution.py
│   ├── test_execution_results.csv
│   ├── test_results.csv
│   └── ...
├── py_fundamentals/                      # beginner Python practice
│   ├── conditional.py
│   ├── data_types_guide.py
│   ├── exception_handling.py
│   ├── first.py
│   ├── fun-sum.py
│   ├── lists_ex.py
│   ├── loops.py
│   ├── math_example.py
│   ├── number_2_exploration.ipynb
│   ├── operators.py
│   ├── strings_ex.py
│   ├── ex/
│   └── temp/
└── ...
```

## Suggested learning order

1. Start with the fundamentals in `py_fundamentals/`
2. Practice conditionals, loops, and basic data types
3. Explore JSON and nested data handling
4. Move into NumPy for numeric and array operations
5. Use pandas for DataFrames, filtering, and tabular data analysis

## Quick start

From the project root, run a script with Python:

```bash
python py_fundamentals/first.py
python py_fundamentals/conditional.py
python py_fundamentals/loops.py
python json_/json_ex.py
python numpy/numpy_basics.py
python pandas/dataframe_pandas.py
python pandas/boolean_filtering.py
```

## Virtual environment setup

This project includes a local virtual environment in `.venv`.

### Windows PowerShell

```powershell
cd D:\neova-ai-lab\python-recipes
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install pandas numpy
```

Then run scripts using the project environment:

```powershell
.\.venv\Scripts\python.exe pandas\dataframe_pandas.py
.\.venv\Scripts\python.exe pandas\boolean_filtering.py
```

## Pandas data exploration

```python
import pandas as pd

df = pd.read_csv("pandas/test_execution_results.csv")

# Preview and inspect the dataset
print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
df.info()  # info() prints its report and returns None

# Summarize values and numeric data
print(df["Status"].value_counts())
print(df["Priority"].value_counts())
print(df["Duration"].describe())

# Filter, sort, and group rows
failed_tests = df[df["Status"] == "Failed"]
print(failed_tests)
print(df.sort_values("Duration", ascending=False))
print(df.groupby("Status")["Duration"].mean())

# Check data quality
print("Missing values:\n", df.isna().sum())
print("Duplicate rows:", df.duplicated().sum())
```

Run `python pandas/test_execution.py` from the project root to try these operations on the sample test-execution data. Use `df.loc[...]` to select by labels and `df.iloc[...]` to select by row or column position. After cleaning or transforming data, save it with `df.to_csv("pandas/cleaned_results.csv", index=False)`.

## Notes

This repository is intended for learning by doing. The exercises are compact and focused so each concept stays easy to understand and easy to test.

## Next ideas

After covering the basics, useful next steps include:

- reusable functions and modular scripts
- file handling and CSV processing
- data cleaning and transformation
- API-based data retrieval
- more advanced pandas workflows
- data science and machine learning projects
