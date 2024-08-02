# Python Inheritance

## Overview

This project explores the concept of inheritance in Python, focusing on the following key topics:

- **Base (Parent) Class**: Understanding the role and structure of a base or super class in Python.
- **Subclassing**: Creating subclasses that inherit from base classes and extend or modify their functionality.
- **Multiple Inheritance**: Utilizing multiple base classes to design more complex class hierarchies.
- **Method and Attribute Override**: Overriding methods and attributes in subclasses to customize behavior.
- **Default Class Behavior**: Implementing default behavior in base classes to streamline subclass creation.

## Acknowledgements

I extend my gratitude to the ALX community for their support and guidance throughout this project.

## Author

**Name**: Ginika Elizabeth, Nna  
**Email**: elizabethginika9@gmail.com

## Table of Contents

1. [Introduction](#introduction)
2. [Base and Subclasses](#base-and-subclasses)
3. [Multiple Inheritance](#multiple-inheritance)
4. [Method and Attribute Override](#method-and-attribute-override)
5. [Default Class Behavior](#default-class-behavior)
6. [Conclusion](#conclusion)
7. [References](#references)

## Introduction

Inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from another class. This promotes code reuse and can lead to more efficient and organized code.

## Base and Subclasses

In this section, we demonstrate how to create a base class and extend it through subclasses. We explore how subclasses can inherit and override methods and attributes to provide specialized functionality.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")
```

## Multiple Inheritance

Multiple inheritance allows a class to inherit from more than one base class. This section provides examples of how to implement and use multiple inheritance in Python.

```python
class Flyer:
    def fly(self):
        print("Can fly")

class Swimmer:
    def swim(self):
        print("Can swim")

class Duck(Flyer, Swimmer):
    pass
```

## Method and Attribute Override

Here, we explore how subclasses can override methods and attributes of their base classes to alter or extend their behavior.

```python
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def start(self):
        print("Car starts with a key")
```

## Default Class Behavior

Base classes can provide default behavior, making it easier to create subclasses with consistent functionality. This section illustrates how to set default behaviors in base classes.

```python
class DefaultShape:
    color = "red"

    def draw(self):
        print("Drawing shape")

class Circle(DefaultShape):
    pass
```

## Conclusion

This project demonstrates the versatility and power of inheritance in Python, showcasing how it can be used to create organized and maintainable code structures.

## References

- Python Documentation: [Classes and Inheritance](https://docs.python.org/3/tutorial/classes.html)
- ALX Community Resources
