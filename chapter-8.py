# Exercise 8.1
s = "  Hello, World!  "

print(s.strip())  # Output: "Hello, World!"

print(s.replace("Hello", "Hi"))  # Output: "  Hi, World!  "

print(s.find("World"))  # Output: 9

print(s.upper())  # Output: "  HELLO, WORLD!  "
print(s.lower())  # Output: "  hello, world!  "
print(s.title())  # Output: "  Hello, World!  "

# Exercise 8.2
word = "banana"
print(word.count("a"))  # Output: 3

# Exercise 8.3
s = "abcdefghijklmnopqrstuvwxyz"

print(s[::2])  # Output: "acegikmoqsuwy"

print(s[::3])  # Output: "adgjmpsvy"

print(s[::-1])  # Output: "zyxwvutsrqponmlkjihgfedcba"

# Exercise 8.4
s = "Hello, World!"
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
# Output: False
print(any_lowercase1(s))
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
# Output: True
print(any_lowercase2(s))
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
# Output: False
print(any_lowercase3(s))
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
# Output: True
print(any_lowercase4(s))
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
# Output: False
print(any_lowercase5(s))

# Exercise 8.5
def rotate_word(word, shift):
    result = ""
    for char in word:
        if char.isalpha(): 
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr(base + (ord(char) - base + shift) % 26)
            result += new_char
        else:
            result += char 
    return result
