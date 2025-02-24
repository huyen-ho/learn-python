# Exercise 5.1
import time

def convert_time():
    current_time = time.time()  
    days_since_epoch = int(current_time // (24 * 3600)) 
    seconds_in_day = int(current_time % (24 * 3600))  

    hours = seconds_in_day // 3600
    minutes = (seconds_in_day % 3600) // 60
    seconds = (seconds_in_day % 3600) % 60

    print(f"Days since epoch: {days_since_epoch}")
    print(f"Current time: {hours:02}:{minutes:02}:{seconds:02}")

convert_time()

# Exercise 5.2
def check_fermat(a, b, c, n):
    if n > 2 and a ** n + b ** n == c ** n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")
        
def get_user_input():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    n = int(input("Enter n: "))
    
    check_fermat(a, b, c, n)

get_user_input()

# Exercise 5.3
def is_triangle(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        print("No")
    else:
        print("Yes")

def get_user_input():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    
    is_triangle(a, b, c)

get_user_input()