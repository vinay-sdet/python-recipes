# Python Recipes

A practical Python learning repository covering the essentials of Python programming, data handling, NumPy, and pandas-based analysis.

## Overview

This repository is a collection of small, focused exercises and scripts designed to help build confidence in Python from the basics through simple data-processing workflows. The examples are intentionally compact and easy to run, making them useful for learning by repetition and gradual progression.

The learning flow in this project follows a practical path:

- Python fundamentals: variables, operators, conditions, loops, strings, and functions
- Data structures: lists, dictionaries, tuples, sets, and nested objects
- Exception handling and input-driven scripts
- JSON handling and file processing
- NumPy arrays and broadcasting
- pandas DataFrames, CSV/JSON work, filtering, and cleanup

## Repository structure

```text
python-recipes/
├── README.md
├── python_learning_progress.pptx
├── .venv/
├── json_/
│   ├── emp.json
│   ├── json_ex.py
│   └── josn_reader.py
├── numpy/
│   ├── array_operations.py
│   ├── broadcasting_2d_array.py
│   ├── ex1_ex2_numpy.py
│   └── numpy_basics.py
├── pandas/
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
│   └── test_results.csv
├── py_fundamentals/
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
│   │   ├── ex1.py
│   │   ├── ex2.py
│   │   ├── ex3.py
│   │   ├── ex4_data_types_ex.py
│   │   ├── ex5_list_loop.py
│   │   ├── ex6_dict_loop_condition.py
│   │   ├── ex7_fn_list.py
│   │   ├── ex8_stats.py
│   │   ├── ex9.py
│   │   ├── ex10_nested_data.py
│   │   ├── ex11_nested_data.py
│   │   ├── ex12_nested_data.py
│   │   └── nested-data.py
│   └── temp/
│       └── create_learning_progress_slide.py
└── python_learning_progress.pptx
```

## Suggested learning path

1. Start with the basics in `py_fundamentals/`
2. Practice the numbered exercises in `py_fundamentals/ex/`
3. Work with JSON files in `json_/`
4. Explore NumPy in `numpy/`
5. Move into pandas for data analysis in `pandas/`

Run scripts from the repository root so relative paths resolve correctly.

## Prerequisites

- Python 3.x
- A virtual environment (recommended: `.venv`)
- `numpy` and `pandas` for data-focused scripts
- `python-pptx` only if you want to regenerate the slide deck

## Quick start

From the project root, you can run the scripts directly:

```bash
python py_fundamentals/first.py
python py_fundamentals/conditional.py
python py_fundamentals/loops.py
python py_fundamentals/ex/ex6_dict_loop_condition.py
python json_/json_ex.py
python json_/josn_reader.py
python numpy/numpy_basics.py
python pandas/dataframe_pandas.py
python pandas/boolean_filtering.py
```

Some scripts, such as `operators.py`, `conditional.py`, `py_fundamentals/ex/ex2.py`, and `math_example.py`, wait for keyboard input.

## Virtual environment setup

### Windows PowerShell

```powershell
cd D:\neova-ai-lab\python-recipes
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install pandas numpy
```

Then run scripts with the virtual environment interpreter:

```powershell
.\.venv\Scripts\python.exe pandas\dataframe_pandas.py
.\.venv\Scripts\python.exe pandas\boolean_filtering.py
.\.venv\Scripts\python.exe json_\josn_reader.py
```

## Fundamentals exercises

| Script | Learning focus |
| --- | --- |
| `py_fundamentals/ex/ex1.py` | Basic variable types with `type()` |
| `py_fundamentals/ex/ex2.py` | `input()` and comparison logic |
| `py_fundamentals/ex/ex3.py` | `for` and `while` loop patterns |
| `py_fundamentals/ex/ex4_data_types_ex.py` | Lists, tuples, sets, and dictionaries |
| `py_fundamentals/ex/ex5_list_loop.py` | Looping items by value and index |
| `py_fundamentals/ex/ex6_dict_loop_condition.py` | Filtering dictionary-based results |
| `py_fundamentals/ex/ex7_fn_list.py` | Functions returning selected values |
| `py_fundamentals/ex/ex8_stats.py` | Pass/fail counts and percentages |
| `py_fundamentals/ex/ex9.py` | Finding maximum values in a list |
| `py_fundamentals/ex/nested-data.py` | Nested structures and lists of dictionaries |
| `py_fundamentals/ex/ex10_nested_data.py` | Reading fields from nested JSON-like structures |
| `py_fundamentals/ex/ex11_nested_data.py` | Printing failed cases from structured data |
| `py_fundamentals/ex/ex12_nested_data.py` | `json.dumps()` and `json.loads()` |

## Example: pandas data exploration

`pandas/test_execution.py` loads `pandas/test_execution_results.csv` and prints the shape, column names, missing values, dtypes, summary statistics, and a sorted view by browser.

```python
import pandas as pd

df = pd.read_csv("pandas/test_execution_results.csv")

print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
df.info()

print(df.isnull().sum())
print(df.describe())
print(df.sort_values("Browser", ascending=True))
```

Related scripts:

- `pandas/boolean_filtering.py` keeps failed rows, Chrome rows, and rows that passed on Chrome, then sorts by duration
- `pandas/ex1&4_pandas.py` writes `ex1_test_results.csv` and `ex4_test_results.json`
- `pandas/ex2&3_pandas.py` reads the CSV and keeps failures with a duration of 10 or more
- `pandas/ex5_pandas.py` fills missing status values with `"Unknown"` and missing durations with the column mean

## Notes

The exercises are intentionally short and focused so each file stays easy to understand, rerun, and extend. They are designed to support learning by repetition and by gradually increasing complexity.

## Next ideas

After completing the current exercises, useful next steps include:

- writing reusable functions and helper modules
- more file handling and CSV/JSON processing
- data cleaning and transformation workflows
- API-based data retrieval
- more advanced pandas analysis
- data science and machine learning projects
