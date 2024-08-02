# Python - Input/Output

## Overview

This project explores file manipulation in Python, specifically focusing on reading from and writing to files using the JSON format. JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate.

## Acknowledgements

I extend my gratitude to the ALX community for their support and guidance throughout this project.

## Author

**Name**: Ginika Elizabeth, Nna  
**Email**: elizabethginika9@gmail.com

## Table of Contents

1. [Introduction](#introduction)
2. [Reading JSON Files](#reading-json-files)
3. [Writing JSON Files](#writing-json-files)
4. [Use Cases](#use-cases)
5. [Conclusion](#conclusion)
6. [References](#references)

## Introduction

File input and output (I/O) is a fundamental aspect of programming that allows for the persistence of data. In Python, JSON is commonly used to store and exchange data due to its simplicity and compatibility with many programming languages.

## Reading JSON Files

To read a JSON file in Python, we use the `json` module, which provides functionalities to parse JSON data and convert it into Python data structures like dictionaries and lists.

```python
import json

# Reading a JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

print(data)
```

## Writing JSON Files

Writing to a JSON file involves serializing Python objects into JSON strings and saving them to a file. This is also achieved using the `json` module.

```python
import json

# Writing to a JSON file
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
```

## Use Cases

1. **Data Persistence**: Store application settings, user preferences, or any data that needs to persist between program executions.
   
2. **Data Exchange**: JSON is often used in web services and APIs to exchange data between clients and servers.

3. **Configuration Files**: JSON files are used to store configuration data, allowing applications to read settings at runtime.

## Conclusion

Understanding how to read and write JSON files in Python is crucial for data handling and exchange in modern applications. JSON's simplicity and wide adoption make it a valuable tool in a programmer's toolkit.

## References

- Python Documentation: [JSON Module](https://docs.python.org/3/library/json.html)
- W3Schools: [JSON Tutorial](https://www.w3schools.com/js/js_json_intro.asp)
- Real Python: [Working with JSON Data in Python](https://realpython.com/python-json/)
