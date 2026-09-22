# Python Recipes for AI Learning

A practical learning repository for building Python fundamentals with examples that connect directly to AI, data analysis, and automation work.

## Goal

This repo helps practice the Python skills that matter most in real workflows: variables, data types, conditionals, loops, collections, JSON, NumPy arrays, and pandas DataFrames.

## Learning checklist

Use this as a progress tracker while going through the exercises:

- [x] Python basics and syntax
- [x] Variables and data types
- [x] Lists, dictionaries, and strings
- [x] Conditionals and input handling
- [x] For and while loops
- [x] Exception handling and debugging
- [x] JSON data structures
- [x] NumPy array basics
- [x] Pandas DataFrames and filtering
- [ ] Connecting Python basics to AI/data tasks

## Core topics covered

- Python syntax and basic scripting
- Data types and mutability
- User input and decision-making
- Iteration with for and while loops
- Lists, dictionaries, and strings
- Error handling and debugging
- JSON serialization and structured data
- NumPy arrays for numeric and ML-adjacent tasks
- Pandas DataFrames for tabular data analysis
- Boolean filtering, sorting, and summary statistics

## Repository layout

### py_fundamentals/
This folder contains the main foundational Python exercises.

Examples include:
- first.py — basic Hello World example
- data_types_guide.py — overview of Python data types and practical usage
- conditional.py — simple branching logic with input
- loops.py — for and while loop examples
- lists_ex.py — list operations and indexing
- exception_handling.py — handling runtime errors with try/except
- strings_ex.py — text manipulation examples
- math_example.py — arithmetic exercises
- operators.py — arithmetic and comparison operators
- ex/ — additional small practice scripts and experiments

### json_/
This folder focuses on structured data, especially JSON.

Included files:
- json_ex.py — basic JSON serialization example
- josn_reader.py — JSON-related reading or processing work
- emp.json — sample employee data in JSON format

### numpy/
This folder introduces array-based data handling, which is key in AI and data science.

Included files:
- numpy_basics.py — simple array creation and arithmetic using NumPy
- array_operations.py — element-wise array operations
- broadcasting_2d_array.py — broadcasting examples with 2D arrays
- ex1_ex2_numpy.py, ex3_numpy.py — practice exercises and examples

### pandas/
This folder introduces tabular data handling with pandas.

Included files:
- dataframe_pandas.py — creating a DataFrame from a dictionary and printing it
- boolean_filtering.py — filtering rows by column values, sorting, and summary statistics
- ex5_pandas.py — identifying missing values, filling missing status values with "Unknown", and replacing missing durations with the mean duration

## Suggested learning path

1. Begin with the Python basics in py_fundamentals/
2. Learn data types and collections before moving to more complex logic
3. Practice conditionals and loops with small real examples
4. Handle errors and unexpected input using try/except
5. Explore JSON to understand structured data
6. Move into NumPy to work with arrays and numeric operations
7. Use pandas to work with tabular data and filtering logic

## Quick start

Run the scripts from the project root:

```bash
python py_fundamentals/first.py
python py_fundamentals/data_types_guide.py
python py_fundamentals/conditional.py
python py_fundamentals/loops.py
python json_/json_ex.py
python numpy/numpy_basics.py
python pandas/dataframe_pandas.py
python pandas/boolean_filtering.py
python pandas/ex5_pandas.py
```

## Running in VS Code

Use the project virtual environment so the same Python packages are used consistently across the repo.

```powershell
cd D:\neova-ai-lab\python-recipes
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install pandas numpy
```

Then either:

1. Open a terminal in VS Code and run a script directly:

```powershell
.\.venv\Scripts\python.exe pandas\dataframe_pandas.py
.\.venv\Scripts\python.exe pandas\boolean_filtering.py
```

2. Or select the interpreter in VS Code: 
   - Open the Command Palette
   - Choose `Python: Select Interpreter`
   - Pick the `.venv` environment in this project
   - Run any script with the built-in Python extension

> If pandas throws a Windows DLL error, reinstall the package in the venv as shown above. This usually fixes the native binary issue.

## Why this matters for AI

These exercises are the building blocks behind many AI-related tasks:

- reading and validating user or prompt input
- working with structured JSON data
- organizing information in lists and dictionaries
- handling missing or malformed values safely
- preparing numeric data for analysis or model workflows
- filtering and summarizing datasets before model training or reporting

This repo is a foundation for later work with APIs, data preprocessing, model inputs, automation, and ML pipelines.

## Next steps

As your Python confidence grows, the natural next topics are:

- functions and reusable code
- file handling and CSV data
- more advanced pandas operations
- data cleaning and transformation
- requests and API integration
- data preprocessing for ML

## Notes

This is intentionally a small, practical repository designed for learning and experimentation.

The focus is on simple examples that build understanding step by step, instead of large or production-style projects.

## Summary

This repo is a compact Python practice space for building the fundamentals that support AI and data work.

It is best viewed as a progression: start with basic syntax, gain comfort with data structures, then move into JSON, numeric arrays, and tabular datasets before taking on larger AI projects.
