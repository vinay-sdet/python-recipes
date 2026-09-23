# Python Recipes

This repository is a hands-on Python practice workspace covering the fundamentals needed for data work, analysis, and AI-related automation.

## Purpose

The goal is to build confidence with:

- Python syntax and basic scripting
- variables, operators, and data types
- loops, conditionals, and functions
- lists, dictionaries, and strings
- exception handling and debugging
- JSON data handling
- NumPy array operations
- pandas DataFrame analysis and filtering

## Project structure

### py_fundamentals/
Core Python learning exercises.

Examples include:
- first.py
- data_types_guide.py
- conditional.py
- loops.py
- lists_ex.py
- operators.py
- strings_ex.py
- math_example.py
- exception_handling.py
- fun-sum.py
- ex/ — additional beginner exercises and experiments

### json_/
JSON examples and sample data.

Examples include:
- json_ex.py
- josn_reader.py
- emp.json

### numpy/
NumPy practice for arrays and numeric operations.

Examples include:
- numpy_basics.py
- array_operations.py
- broadcasting_2d_array.py
- ex1_ex2_numpy.py

### pandas/
Pandas practice for working with tabular data.

Examples include:
- dataframe_pandas.py
- boolean_filtering.py
- csv_&_json.py
- ex1_test_results.csv
- ex5_pandas.py
- ex1&4_pandas.py
- ex2&3_pandas.py
- test_execution.py
- test_execution_results.csv
- test_results.csv

## Suggested learning order

1. Start with the scripts in py_fundamentals/
2. Practice conditionals, loops, and data types
3. Learn JSON for structured data
4. Move into NumPy for array operations
5. Use pandas for DataFrames, filtering, and CSV/JSON work

## Running scripts

From the project root, run scripts with Python:

```bash
python py_fundamentals/first.py
python py_fundamentals/conditional.py
python py_fundamentals/loops.py
python json_/json_ex.py
python numpy/numpy_basics.py
python pandas/dataframe_pandas.py
python pandas/boolean_filtering.py
```

## Using the virtual environment

This project includes a local virtual environment in `.venv`.

On Windows PowerShell:

```powershell
cd D:\neova-ai-lab\python-recipes
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install pandas numpy
```

Then run a script like this:

```powershell
.\.venv\Scripts\python.exe pandas\dataframe_pandas.py
.\.venv\Scripts\python.exe pandas\boolean_filtering.py
```

## Example: first five rows in pandas

```python
import pandas as pd

df = pd.read_csv("pandas/test_execution_results.csv")
print(df.head(5))
```

This prints the first five rows of the DataFrame.

## Notes

This repository is designed for learning by doing. Many scripts are intentionally small and focused so that the core Python concepts stay easy to understand.

## Future learning ideas

After the basics, the next natural steps are:

- functions and reusable code
- file handling and CSV processing
- data cleaning and transformation
- API requests
- more advanced pandas analysis
- machine learning and data-preprocessing workflows
