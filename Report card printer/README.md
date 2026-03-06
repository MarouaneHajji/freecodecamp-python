Report Card Data Types Example

This is a small Python project from the freeCodeCamp curriculum that demonstrates how to use different Python data types when working with student information.

Project Description

The program shows how to:

Store and display string, boolean, integer, and float values.

Check data types using type() and isinstance().

Understand how different data types are used in a student report card scenario.

Example Code
name = 'Alice'
print(name, type(name))

is_student = True
print(is_student, type(is_student))

age = 20
print(age, type(age))

score = 80.5
print(isinstance(score, float))
print(score, type(score))
Example Output
Alice <class 'str'>
True <class 'bool'>
20 <class 'int'>
True
80.5 <class 'float'>
Purpose

Learn how to define and check different data types in Python.

Prepare for building more complex projects like a report card printer.