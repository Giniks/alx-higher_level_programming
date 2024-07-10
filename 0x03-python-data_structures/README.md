# Python - Data Structures: Lists and Tuples

## Overview

This project centers on the manipulation of lists and tuples in Python. It demonstrates various operations such as printing, retrieving, replacing, reversing, removing, inserting, and deleting elements within these data structures. The project provides clear examples and explanations to help users understand and utilize lists and tuples effectively in their Python programming endeavors.

## Table of Contents

- [Introduction](#introduction)
- [Lists](#lists)
  - [Creating a List](#creating-a-list)
  - [Accessing Elements](#accessing-elements)
  - [Modifying Elements](#modifying-elements)
  - [Adding Elements](#adding-elements)
  - [Removing Elements](#removing-elements)
  - [Reversing a List](#reversing-a-list)
  - [Sorting a List](#sorting-a-list)
- [Tuples](#tuples)
  - [Creating a Tuple](#creating-a-tuple)
  - [Accessing Elements](#accessing-elements-1)
  - [Modifying a Tuple](#modifying-a-tuple)
  - [Unpacking a Tuple](#unpacking-a-tuple)
- [Examples](#examples)
- [Acknowledgment](#acknowledgment)
- [Contact](#contact)

## Introduction

Lists and tuples are fundamental data structures in Python that allow for the storage and manipulation of ordered collections of items. While lists are mutable and can be changed after their creation, tuples are immutable and cannot be modified once established. This project covers various methods and techniques to work with both lists and tuples efficiently.

## Lists

### Creating a List

```python
# Creating an empty list
my_list = []

# Creating a list with elements
my_list = [1, 2, 3, 4, 5]
```

### Accessing Elements

```python
# Accessing elements by index
first_element = my_list[0]
last_element = my_list[-1]
```

### Modifying Elements

```python
# Changing an element at a specific index
my_list[1] = 10
```

### Adding Elements

```python
# Appending an element to the end of the list
my_list.append(6)

# Inserting an element at a specific position
my_list.insert(2, 15)
```

### Removing Elements

```python
# Removing an element by value
my_list.remove(10)

# Removing an element by index
del my_list[0]

# Popping the last element
last_element = my_list.pop()
```

### Reversing a List

```python
# Reversing the order of elements in the list
my_list.reverse()
```

### Sorting a List

```python
# Sorting the list in ascending order
my_list.sort()

# Sorting the list in descending order
my_list.sort(reverse=True)
```

## Tuples

### Creating a Tuple

```python
# Creating an empty tuple
my_tuple = ()

# Creating a tuple with elements
my_tuple = (1, 2, 3, 4, 5)
```

### Accessing Elements

```python
# Accessing elements by index
first_element = my_tuple[0]
last_element = my_tuple[-1]
```

### Modifying a Tuple

Tuples are immutable and cannot be modified after creation. However, you can concatenate tuples to create a new one.

```python
# Concatenating tuples
new_tuple = my_tuple + (6, 7)
```

### Unpacking a Tuple

```python
# Unpacking elements of a tuple into variables
a, b, c, d, e = my_tuple
```

## Examples

This section will provide various examples to illustrate how to perform the operations mentioned above on lists and tuples.

## Acknowledgment

Special thanks ALX community for her contributions to this project.

## Author 

Name: Ginika Elizabeth 
Email: elizabethginika9@gmail.com
