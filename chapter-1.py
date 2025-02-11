'''Exercise 1.1. It is a good idea to read this book in front of a computer so you can try out the
Whenever you are experimenting with a new feature, you should try to make mistakes. For example, in the “Hello, world!” program, what happens if you leave out one of the quotation marks? What if you leave out both? What if you spell print wrong?
This kind of experiment helps you remember what you read; it also helps when you are programming, because you get to know what the error messages mean. It is better to make mistakes now and on purpose than later and accidentally.
'''
# 1. In a print statement, what happens if you leave out one of the parentheses, or both?
print('Hello world!')

# 2. If you are trying to print a string, what happens if you leave out one of the quotation marks, or both?
# print('Hello world!')
# SyntaxError: EOL while scanning string literal

# 3. You can use a minus sign to make a negative number like -2. What happens if you put a plus sign before a number? What about 2++2?
print(-2)   #-2
print(+2)   #2
print(2++2) #4

# 4. In math notation, leading zeros are ok, as in 09. What happens if you try this in Python? What about 011?
#print(09)   #SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
#print(011)  #SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

#5. What happens if you have two values with no operator between them?
print(2, 3) #2 3

# Exercise 1.2. Start the Python interpreter and use it as a calculator.
# 1. How many seconds are there in 42 minutes 42 seconds?
m = s = 42
print(m * 60 + s)

# 2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
k = 10 / 1.61
print(k)

# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?
print((m + s/60)/k)
print(k/((m + s/60)/60))
