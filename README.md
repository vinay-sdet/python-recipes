# Python Recipes

A hands-on Python practice repository for learning the fundamentals of programming, working with JSON data, and exploring data with NumPy and pandas.

## Overview

This repository is a collection of small exercises and scripts used to build practical Python skills step by step. It is designed for beginners who want to move from basic syntax to simple data analysis workflows.

Topics covered include:

- Python basics: variables, operators, loops, conditionals, strings, and functions
- Data structures: lists, dictionaries, and nested data
- Exception handling and debugging
- Reading and writing JSON data
- NumPy arrays and numeric operations
- pandas DataFrames, filtering, grouping, and CSV/JSON examples

## Repository structure

```text
python-recipes/
├── README.md
├── python_learning_progress.pptx
├── .venv/                              # local virtual environment
├── json_/                              # JSON exercises and sample data
│   ├── emp.json
│   ├── json_ex.py
│   └── josn_reader.py
├── numpy/                              # NumPy practice scripts
│   ├── array_operations.py
│   ├── broadcasting_2d_array.py
│   ├── ex1_ex2_numpy.py
│   └── numpy_basics.py
├── pandas/                             # pandas practice scripts and sample data
│   ├── boolean_filtering.py
│   ├── csv_&_json.py
│   ├── dataframe_pandas.py
│   ├── ex1&4_pandas.py
│   ├── ex1_test_results.csv
│   ├── ex2&3_pandas.py
│   ├── ex4_test_results.json
│   ├── ex5_pandas.py
│   ├── test_execution.py
│   ├── test_execution_results.csv
│   ├── test_results.csv
│   └── ...
├── py_fundamentals/                     # beginner Python practice
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

## Suggested learning path

1. Start with the fundamentals in `py_fundamentals/`
2. Practice conditionals, loops, and core data types
3. Explore JSON handling and nested data
4. Work through NumPy exercises for arrays and numeric operations
5. Use pandas for DataFrames, filtering, and tabular data analysis

## Prerequisites

- Python 3.x installed on your system
- Optional: a virtual environment for isolated package installs
- `numpy` and `pandas` installed for the data-focused scripts

## Quick start

From the project root, run scripts using Python directly:

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

This project includes a local virtual environment in `.venv`, which is already set up in the workspace.

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
.\.venv\Scripts\python.exe json_\json_ex.py
```

## Example: pandas data exploration

```python
import pandas as pd

df = pd.read_csv("pandas/test_execution_results.csv")

print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
df.info()

print(df["Status"].value_counts())
print(df["Duration"].describe())

failed_tests = df[df["Status"] == "Failed"]
print(failed_tests)
print(df.sort_values("Duration", ascending=False))
print(df.groupby("Status")["Duration"].mean())

print("Missing values:\n", df.isna().sum())
print("Duplicate rows:", df.duplicated().sum())
```

Run `python pandas/test_execution.py` from the project root to try these operations on the sample execution dataset. Use `df.loc[...]` and `df.iloc[...]` to select rows and columns by label or position.

## Notes

This repository is intended for learning by doing. The exercises are intentionally compact and focused so that each concept stays easy to understand and easy to test.

## Next ideas

After completing the basics, useful next steps include:

- reusable functions and modular scripts
- file handling and CSV processing
- data cleaning and transformation
- API-based data retrieval
- more advanced pandas workflows
- data science and machine learning projects
