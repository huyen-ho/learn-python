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

# Exercise 7.2
def eval_loop():
    last_result = None
    while True:
        expr = input("Enter an expression (or 'done' to exit): ")
        if expr.lower() == 'done':
            return last_result
        try:
            last_result = eval(expr)
            print(last_result)
        except Exception as e:
            print(f"Error: {e}")

eval_loop()

# Exercise 7.3
import math

def estimate_pi():
    total = 0
    k = 0
    factor = (2 * math.sqrt(2)) / 9801
    
    while True:
        num = math.factorial(4 * k) * (1103 + 26390 * k)
        denom = (math.factorial(k) ** 4) * (396 ** (4 * k))
        term = factor * (num / denom)
        
        total += term
        if abs(term) < 1e-15:  
            break
        
        k += 1
    
    return 1 / total  

print(f"Estimate of pi: {estimate_pi()}")
print(f"math.pi: {math.pi}")

