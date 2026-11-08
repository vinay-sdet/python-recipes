# Python Recipes

A hands-on Python practice repository for learning the fundamentals of programming, working with JSON data, and exploring data with NumPy and pandas.

## Overview

This repository is a collection of small exercises and scripts used to build practical Python skills step by step. It is designed for beginners who want to move from basic syntax to simple data analysis workflows.

Most examples use test-execution data (test case, status, browser, duration) so the same ideas show up again as the scripts get more capable.

Topics covered include:

- Python basics: variables, operators, loops, conditionals, strings, and functions
- Data structures: lists, dictionaries, tuples, sets, and nested data
- Exception handling
- Reading and writing JSON data
- NumPy arrays, vectorized math, and broadcasting
- pandas DataFrames, CSV/JSON I/O, filtering, sorting, and missing values

## Repository structure

```text
python-recipes/
├── README.md
├── python_learning_progress.pptx          # generated progress slide
├── .venv/                                 # local virtual environment
├── json_/
│   ├── emp.json
│   ├── json_ex.py                         # dict → JSON string
│   └── josn_reader.py                     # load emp.json and print fields
├── numpy/
│   ├── numpy_basics.py                    # element-wise +, -, *, /
│   ├── ex1_ex2_numpy.py                   # create an array and scale it
│   ├── array_operations.py                # add, subtract, and multiply two arrays
│   └── broadcasting_2d_array.py           # scalar and 2D broadcasting
├── pandas/
│   ├── dataframe_pandas.py                # build a DataFrame and select rows
│   ├── boolean_filtering.py               # filter, sort, and select columns
│   ├── csv_&_json.py                      # read test_results.csv
│   ├── ex1&4_pandas.py                    # write CSV and JSON, then read JSON back
│   ├── ex2&3_pandas.py                    # read the CSV and filter slow failures
│   ├── ex5_pandas.py                      # fill missing status and duration
│   ├── test_execution.py                  # explore test_execution_results.csv
│   ├── ex1_test_results.csv
│   ├── ex4_test_results.json
│   ├── test_execution_results.csv
│   └── test_results.csv
└── py_fundamentals/
    ├── first.py                           # hello world
    ├── data_types_guide.py                # str, int, float, bool, list, dict, and more
    ├── operators.py                       # comparison operators from user input
    ├── conditional.py                     # simple text bot
    ├── loops.py                           # for and while over a name list
    ├── lists_ex.py                        # list length and indexing
    ├── strings_ex.py                      # len, isalnum, isalpha
    ├── fun-sum.py                         # a typed add function
    ├── math_example.py                    # square root with the math module
    ├── exception_handling.py              # try/except around a TypeError
    ├── number_2_exploration.ipynb
    ├── ex/                                # numbered practice exercises
    └── temp/
        └── create_learning_progress_slide.py
```

## Suggested learning path

1. Start with the fundamentals in `py_fundamentals/`
2. Work through the numbered exercises in `py_fundamentals/ex/`
3. Practice JSON handling in `json_/` and nested data in `py_fundamentals/ex/`
4. Work through the NumPy scripts in order: basics, then exercises 1–4
5. Use pandas for DataFrames, file I/O, filtering, and cleaning

Run scripts from the project root. Several files open data with paths such as `pandas/test_results.csv` and `json_/emp.json`, which only resolve from that directory.

## Fundamentals exercises

| Script | What it practices |
| --- | --- |
| `ex/ex1.py` | Variable types with `type()` |
| `ex/ex2.py` | `input()` and an age check |
| `ex/ex3.py` | `for` and `while` over a language list |
| `ex/ex4_data_types_ex.py` | List, tuple, set, and dictionary behavior |
| `ex/ex5_list_loop.py` | Loop a test-case list by value and by index |
| `ex/ex6_dict_loop_condition.py` | Loop a results dict and print failures |
| `ex/ex7_fn_list.py` | Return the passed test names from a dict |
| `ex/ex8_stats.py` | Count passed, failed, and pass percentage |
| `ex/ex9.py` | Find the largest number in a list |
| `ex/nested-data.py` | Nested dicts and lists |
| `ex/ex10_nested_data.py` | Read fields from a nested employee dict |
| `ex/ex11_nested_data.py` | Print only the failed test from a list of dicts |
| `ex/ex12_nested_data.py` | `json.dumps()` and `json.loads()` |

## Prerequisites

- Python 3.x
- A virtual environment (this workspace already has `.venv`)
- `numpy` and `pandas` for the data scripts
- `python-pptx` only if you regenerate `python_learning_progress.pptx`

## Quick start

From the project root:

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

`operators.py`, `conditional.py`, `ex/ex2.py`, and `math_example.py` wait for keyboard input.

## Virtual environment setup

### Windows PowerShell

```powershell
cd D:\neova-ai-lab\python-recipes
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install pandas numpy
```

Then run scripts with that interpreter:

```powershell
.\.venv\Scripts\python.exe pandas\dataframe_pandas.py
.\.venv\Scripts\python.exe pandas\boolean_filtering.py
.\.venv\Scripts\python.exe json_\josn_reader.py
```

## Example: pandas data exploration

`pandas/test_execution.py` loads `pandas/test_execution_results.csv` and prints the shape, columns, missing values, dtypes, summary stats, and a sort by browser:

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
- `pandas/ex2&3_pandas.py` reads that CSV and keeps failures with duration of 10 or more
- `pandas/ex5_pandas.py` fills a missing status with `"Unknown"` and a missing duration with the column mean

## Notes

The exercises are intentionally compact. Each file focuses on one idea so it stays easy to read and easy to rerun

## Next ideas

After the current scripts, useful next steps include:

- reusable functions and modular scripts
- more file handling and CSV processing
- data cleaning and transformation
- API-based data retrieval
- more advanced pandas workflows
- data science and machine learning projects
