# Exercise 7.1
import math

def mysqrt(a):
    x = a / 2 
    epsilon = 1e-10 
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            return y
        x = y

def test_square_root():
    print(f"{'a':<10}{'mysqrt(a)':<20}{'math.sqrt(a)':<20}{'diff':<20}")
    print("-" * 70)
    
    for a in range(1, 10):
        my_sqrt = mysqrt(a)
        math_sqrt = math.sqrt(a)
        diff = abs(my_sqrt - math_sqrt)
        print(f"{a:<10}{my_sqrt:<20}{math_sqrt:<20}{diff:<20}")

test_square_root()
