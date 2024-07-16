# Python Exceptions

## Overview

In this project, I will demonstrate the use of exceptions in Python using built-in functions. This project aims to provide a clear understanding of how exceptions work in Python and how they can be effectively managed to write robust and error-free code.

## Acknowledgement

I am filled with gratitude for the community's support in sharing vital resources that have been instrumental in completing this project. Thank you to the ALX community for all the technical and theoretical assistance provided throughout this course.

## Author

**Name:** Ginika Elizabeth Nna  
**Email:** elizabethginika9@gmail.com  

## Table of Contents

- [Introduction](#introduction)
- [What are Exceptions?](#what-are-exceptions)
- [Common Built-in Exceptions](#common-built-in-exceptions)
- [Handling Exceptions](#handling-exceptions)
- [Creating Custom Exceptions](#creating-custom-exceptions)
- [Best Practices](#best-practices)
- [Conclusion](#conclusion)

## Introduction

Python exceptions are events that can modify the normal flow of a program's execution. In this project, we'll explore various built-in exceptions and how to handle them gracefully to ensure our programs run smoothly even in the face of unexpected issues.

## What are Exceptions?

Exceptions are errors detected during execution that are not unconditionally fatal. They can be handled using try-except blocks, allowing the program to continue running or to fail gracefully.

## Common Built-in Exceptions

Here are some common built-in exceptions in Python:

- `ZeroDivisionError`: Raised when division or modulo by zero takes place.
- `IndexError`: Raised when an index is not found in a sequence.
- `KeyError`: Raised when a key is not found in a dictionary.
- `ValueError`: Raised when a function receives an argument of the right type but an inappropriate value.

## Handling Exceptions

Exceptions in Python can be handled using the `try`, `except`, `else`, and `finally` blocks. Here's an example:

```python
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful!")
finally:
    print("This block always executes.")
```

## Creating Custom Exceptions

In addition to built-in exceptions, Python allows you to define your own exceptions by creating a new class that derives from the base `Exception` class. Here's an example:

```python
class CustomError(Exception):
    """Base class for other exceptions"""
    pass

class ValueTooSmallError(CustomError):
    """Raised when the input value is too small"""
    pass

class ValueTooLargeError(CustomError):
    """Raised when the input value is too large"""
    pass

# Example usage
try:
    number = 10
    if number < 5:
        raise ValueTooSmallError
    elif number > 20:
        raise ValueTooLargeError
except ValueTooSmallError:
    print("Value is too small!")
except ValueTooLargeError:
    print("Value is too large!")
```

## Best Practices

- Use specific exceptions rather than a generic `Exception` to improve code clarity.
- Keep try blocks short and focused on the specific operation that may fail.
- Clean up resources in the `finally` block or use context managers.
- Document the exceptions your functions may raise.

## Conclusion

Understanding and handling exceptions is crucial for building reliable and maintainable Python applications. This project has covered the basics of exceptions, how to handle them, and best practices to follow.
