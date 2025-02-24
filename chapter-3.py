"""
Exercise 3.1. Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.
>>>right_justify('monty')
monty
Hint: Use string concatenation and repetition. Also, Python provides a built-in function called len that returns the length of a string, so the value of len('monty') is 5."""
def right_justify(s):
    spaces = ' ' * (70 - len(s)) 
    print(spaces + s)

right_justify('monty')

# Exercise 3.2. A function object is a value you can assign to a variable or pass as an argument. For
# example, do_twice is a function that takes a function object as an argument and calls it twice:
def do_twice(f):
    f()
    f()

# Here’s an example that uses do_twice to call a function named print_spam twice.

def print_spam():
    print('spam')

do_twice(print_spam)
# 1. Type this example into a script and test it.
# spam
# spam

# 2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument.
def do_twice(f, v):
    f(v)
    f(v)

def print_twice(s):
    print(s)

do_twice(print_twice, 'spam')
# 3. Copy the definition of print_twice from earlier in this chapter to your script.


# 4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an
# argument.
def do_twice(f, v):
    f(v)
    f(v)

def print_twice(s):
    print(s)
    print(s)

do_twice(print_twice, 'spam')
# 5. Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as a parameter. There should be only two statements in the body of this function, not four.
def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)

do_four(print_twice, 'spam')

# Exercise 3.3. Note: This exercise should be done using only the statements and other features we have learned so far.
def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_row():
    print('+ - - - -', end=' ')

def print_rows():
    do_twice(print_row)
    print('+')

def print_column():
    print('|        ', end=' ')

def print_columns():
    do_twice(print_column)
    print('|')

def print_frame():
    print_rows()
    do_four(print_columns)

def print_grid():
    do_twice(print_frame)
    print_rows()

print_grid()

# 2. Write a function that draws a similar grid with four rows and four columns.
def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_row():
    print('+ - - - -' * 2 ,end=' ')
    print('+ - - - -' * 2 + '+')

def print_column():
    print('|        ' * 2 , end=' ')
    print('|        ' * 2 + '|')

def print_frame():
    print_row()
    do_four(print_column)

def print_grid():
    do_four(print_frame)
    print_row()

print_grid()