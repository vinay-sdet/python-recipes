# Python Recipes

A hands-on Python learning workspace for fundamentals, data processing, and introductory data analysis.

## Overview

This repository is organized as a collection of small practice scripts and examples covering:

- Python basics: variables, operators, loops, conditionals, functions, and strings
- data structures: lists, dictionaries, and nested data
- exception handling and debugging
- JSON parsing and structured data handling
- NumPy array operations and broadcasting
- pandas DataFrames, filtering, CSV/JSON work, and result analysis

## Project structure

```text
python-recipes/
├── README.md
├── .venv/                     # local virtual environment
├── json_/                    # JSON examples and sample data
│   ├── emp.json
│   ├── json_ex.py
│   └── josn_reader.py
├── numpy/                    # NumPy practice files
│   ├── array_operations.py
│   ├── broadcasting_2d_array.py
│   ├── ex1_ex2_numpy.py
│   └── numpy_basics.py
├── pandas/                   # pandas exercises and datasets
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
├── py_fundamentals/          # beginner-level Python exercises
│   ├── conditional.py
│   ├── data_types_guide.py
│   ├── exception_handling.py
│   ├── first.py
│   ├── fun-sum.py
│   ├── lists_ex.py
│   ├── loops.py
│   ├── math_example.py
│   ├── operators.py
│   ├── strings_ex.py
│   ├── ex/
│   └── temp/
└── ...
```

## Suggested learning order

1. Start with the scripts in `py_fundamentals/`
2. Practice conditionals, loops, and data types
3. Explore JSON and nested data structures
4. Move into NumPy for numeric and array operations
5. Use pandas for DataFrames, filtering, and tabular datasets

## Running scripts

From the project root, use Python to run any script:

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

This repository includes a local environment in `.venv`.

### Windows PowerShell

```powershell
cd D:\neova-ai-lab\python-recipes
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install pandas numpy
```

Then run a script with the project environment:

```powershell
.\.venv\Scripts\python.exe pandas\dataframe_pandas.py
.\.venv\Scripts\python.exe pandas\boolean_filtering.py
```

## Example

```python
import pandas as pd

df = pd.read_csv("pandas/test_execution_results.csv")
print(df.head())
```

This prints the first few rows of the DataFrame for quick inspection.

## Notes

This project is designed for learning by doing. The exercises are intentionally compact so that each concept stays easy to understand and easy to test.

## Next ideas

After the basics, useful next steps include:

- reusable functions and modular scripts
- file handling and CSV processing
- data cleaning and transformation
- APIs and external data sources
- more advanced pandas analysis
- data science and machine learning workflows
