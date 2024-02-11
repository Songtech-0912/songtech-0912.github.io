+++
title = "Introduction to Python programming"
date = 2024-02-11
+++

There are notes taken in CS1100 at RPI, and cover introductory programming using the Python language.

<!-- more -->

## What is Python?

- Programming is breaking down a big problem into smaller parts
- It is typically done with a programming language
- Python is an interpreted language - it uses a program to execute commands 
- Compiled languages by contrast translate programming code to binary code that is executed by a computer

## First steps with Python

```python
# this is a comment, it is not run
print("Hello World!") # this prints "Hello World!" to console
```

## Python as a calculator

Python supports all the standard operations of a calculator:

```python
5 + 7
12 - 5
2 * 6
25 / 5
# for exponentiation
6 ** 2
```

Usually it's a good idea to use brackets to prevent ambiguities in the order of operations - for instance, does `3 / 5 * 2` mean `(3/5) * 2` or `3 / (5 * 2`? However, if brackets are not used, Python follows the BEDMAS order of operations as in math - that is, first brackets, then exponentiation, then multiplication/division, then addition/subtraction. The one special note is that exponentiation occurs right-to-left: that is `5 ** 2 ** 2` actually means `5 ** (2 ** 2)`.
## Variables

Variables are declared with a name on the left-hand side of the equal sign and a value on the right hand side. For instance:

```python
a = 5
b = 9
pi = 3.14159
```

Variables can only be used after they are declared. If you try to use a variable that doesn't exist and wasn't assigned a value, then Python will give an error.

Python has certain requirements for what it allows as legal variable names. Generally speaking, if a variable name has unusual characters or numbers, or might be confused for a Python keyword, it is most likely invalid.

## Errors

There are 2 types of errors possible in programming (generally):

- Syntactical error: code that isn't valid Python syntax and cannot be run
- Semantic error: code that can be run and is syntactically correct, but doesn't perform as expected

## Numerical types

Python has 2 numeric types:

- Floats, which represent decimal numbers like 2.35 or 5.0
- Ints, which are whole numbers

Division always returns a float, and any float in a calculation returns a float.

## Strings

Strings are Python's type for representing text. Python strings can use single or double quotes. Anything between the quotes is part of the string. For example, this is valid:

```python
msg = "Hi!"
```

And this too is valid:

```python
msg = 'Hi!'
```

In addition, you can include single quotes in double quotes, or double quotes in single quotes, as long as you don't mix them. For instance, this is valid:

```python
# valid
greeting = "Hi there! I'm saying hello!"
# also valid
response = 'Have you read the book "The Great Gatsby" yet?'
```

But if you mix them it wouldn't work:

```python
# invalid
msg = "Hi'
```

Multi-line strings use three quotes; they can contain single or double quote characters within them, anything between the three starting quotes and three ending quotes is valid:

```python
sonnet = """
"Love alters not with his brief hours and weeks,"
'But bears it out even to the edge of doom.'
"If this be error and upon me prov'd,"
I never writ, nor no man ever lov'd.
"""
```

Python also has some special characters to control the print output of a string (what is displayed when you call `print()` on the string):

| Character | Output |
| ---- | ---- |
| `\n` | Creates a new line |
| `\t` | Creates a tab |
| `\\` | Creates a literal `\` character |
| `\"` | Creates a literal `"` character |
| `\'` | Creates a literal `'` character |

### String gotchas

Python does automatic string concatenation on adjacent strings, so the following code would be valid but is not recommended:

```python
msg = "Hi!"'my name is Jack'
```

Whichever type of quote you use - single or double - can appear only once at the beginning of the string and once at the end. For instance, this would not be valid:

```python
msg = "Hi""
```

You can also repeat a string multiple times using `*` or concatenate strings with `+`, like so:

```python
"Hi" * 3 # "HiHiHi"
"Hi" + " Jack!" # "Hi Jack!"
```

However, this isn't recommended either, because if done improperly it can cause a multitude of errors - **string formatting** (discussed later) is the preferable way to create new strings out of existing strings.

## Functions

Functions in Python perform a certain operation. `print()`, `len()`, `max()` are all functions built-in to Python. `int()`, `float()`, and `str()` are built-in functions that convert between types. Functions contain blocks of code that implement functionalities - this could be performing a calculation, opening a window, or creating an image.

Every function takes in *arguments* as input and returns a *value*. When a function is run, we say it is _called_. For instance, `len()` has a single argument, and returns a single value. A function to calculate the area of a circle in Python might look like this:

```python
def area(r):
	pi = 3.14159
	return pi * r ** 2
```

## Boolean logic

There are two types to represent logical truths and falsehoods in Python - `True` and `False`. There are called booleans. Python uses the `>`, `<`, `>=`, `<=` and `!=` (not equal) operators to compare between different things. For instance, `3 < 5` would be equal to `True`. We can also use the `==` operator to check that two things are equal. For instance, `9 == 9` would return `True`, and `5 == 6` would return `False`. Python supports three-way comparisons, like `1 < 2 < 3`.

On strings, Python boolean operators compare based on alphabetical order. For example `"zen" > "apple"` is true, because the first letter of zen (z) is after the first letter of apple (a) in the alphabet, and letters later in the alphabet are greater (in terms of booleans). From the same logic, `"david" < "flamingo"` would also evaluate to true, because d comes before f in the alphabet. In addition, uppercase comes before lowercase, so `"Good" < "good"` would also be true.
