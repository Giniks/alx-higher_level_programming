# Project Title: Python - if/else, loops, functions

## Introduction

This project aims to explore Python's conditional statements, loops, functions, and other fundamental concepts. We will dive into the usage of `if`, `else`, `break`, `continue`, `pass`, and `range` statements. Additionally, we'll implement loop functions using `while` and `for` loops. The project will also cover tracebacks, scope of variables, and arithmetic operations.

## Table of Contents

1. [Overview](#overview)
2. [Getting Started](#getting-started)
3. [Concepts Covered](#concepts-covered)
   - [Conditionals](#conditionals)
   - [Loops](#loops)
   - [Functions](#functions)
   - [Traceback](#traceback)
   - [Scope](#scope)
   - [Arithmetic Operations](#arithmetic-operations)
4. [Examples](#examples)
5. [Author](#author)
6. [Acknowledgements](#acknowledgements)

## Overview

This project is designed to provide a comprehensive understanding of how conditionals, loops, and functions work in Python. By the end of this project, you should be able to implement and utilize these concepts effectively in your own programs.

## Getting Started

1. **Prerequisites**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. **Clone the Repository**: Clone this repository to your local machine using the command:
   ```bash
   git clone https://
   ```
3. **Navigate to the Project Directory**:
   ```bash
   cd 0x01-python-if-else-loops-functions
   ```

## Concepts Covered

### Conditionals

- **if Statement**: Executes a block of code if the condition is true.
- **else Statement**: Executes a block of code if the condition in the if statement is false.
- **elif Statement**: Checks multiple expressions for TRUE and executes a block of code as soon as one of the conditions evaluates to TRUE.
- **break Statement**: Exits the loop prematurely when a condition is met.
- **continue Statement**: Skips the rest of the code inside a loop for the current iteration only.
- **pass Statement**: Acts as a placeholder and does nothing when executed.
- **range() Function**: Generates a sequence of numbers.

### Loops

- **for Loop**: Iterates over a sequence (like a list, tuple, dictionary, set, or string).
- **while Loop**: Repeats a block of code as long as a condition is true.

### Functions

- **Defining Functions**: Creating reusable blocks of code using the `def` keyword.
- **Calling Functions**: Executing a function by using its name followed by parentheses.
- **Parameters and Arguments**: Passing values to functions for more dynamic code.

### Traceback

Understanding and debugging error messages in Python.

### Scope

- **Global Scope**: Variables defined outside of any function.
- **Local Scope**: Variables defined within a function.
- **Variable Scope**: The region where a variable is recognized.

### Arithmetic Operations

Performing basic arithmetic operations like addition, subtraction, multiplication, division, modulus, and exponentiation.

## Examples

### Conditionals Example
```python
number = 10
if number > 0:
    print("Positive number")
else:
    print("Negative number or zero")
```

### Loops Example
```python
for i in range(5):
    print(i)

i = 0
while i < 5:
    print(i)
    i += 1
```

### Functions Example
```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)
```

### Traceback Example
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
```

### Scope Example
```python
global_var = "I am global"

def my_function():
    local_var = "I am local"
    print(global_var)
    print(local_var)

my_function()
print(global_var)
# The next line will raise an error because local_var is not accessible outside the function
# print(local_var)
```

### Arithmetic Operations Example
```python
a = 10
b = 5
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b) # Exponentiation
```

## Author

- **Your Name** - Ginika Elizabeth (https://github.com/Giniks)

## Acknowledgements

- **ALX Community**: For their support and resources.
- **Python Documentation**: For providing detailed explanations and examples.
