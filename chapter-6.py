# Exercise 6.2
def ackermann(m, n):
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))


print(ackermann(3, 4))

# Exercise 6.3
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


print(is_palindrome('john'))
print(is_palindrome('bob'))
print(is_palindrome('otto'))
print(is_palindrome('redivider'))

# Exercise 6.4
def is_power(a, b):
    if a == 1:
        return True
    if a < b or a % b != 0:
        return False
    return is_power(a // b, b)  

print(is_power(8, 2)) 
print(is_power(27, 3)) 
print(is_power(10, 2)) 
print(is_power(1, 3)) 

# Exercise 6.5
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)  

print(gcd(48, 18))  
print(gcd(101, 103)) 
print(gcd(56, 98))