'''
Exercise 2.1. Repeating my advice from the previous chapter, whenever you learn a new feature,
you should try it out in interactive mode and make errors on purpose to see what goes wrong. 
• We’ve seen that n = 42 is legal. What about 42 = n?
'''
# 42 = n 
# print(n) #SyntaxError: expression cannot contain assignment, perhaps you meant "=="?

# • How about x = y = 1?
x = y = 1
print(x, y) #1 1

# • In some languages every statement ends with a semi-colon, ;. What happens if you put a semi-colon at the end of a Python statement?
a = 10;
b = 20;
print(a + b);  #30

# • What if you put a period at the end of a statement?
x = 5.
print(x)  #5.0

# • In math notation you can multiply x and y like this: xy. What happens if you try that in Python?
x = 2
y = 3
# print(xy)  # NameError: name 'xy' is not defined
xy = x * y  # Correct way
print(xy)  #6

# Exercise 2.2. Practice using the Python interpreter as a calculator:
# 1. The volume of a sphere with radius r is 4/3 πr3. What is the volume of a sphere with radius 5?
import math
r = 5
volume = (4/3) * math.pi * r**3
print(volume)  # 523.5987755982989

# 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
book_price = 24.95
discount = 0.40
shipping_first = 3
shipping_additional = 0.75
num_books = 60

total_cost = (book_price * (1 - discount) * num_books) + shipping_first + (shipping_additional * (num_books - 1))
print(total_cost)  # 945.45

# 3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
start_hour = 6
start_minute = 52

easy_pace_per_mile = (8 * 60) + 15  # 8 minutes 15 seconds in seconds
tempo_pace_per_mile = (7 * 60) + 12  # 7 minutes 12 seconds in seconds

total_time_seconds = (2 * easy_pace_per_mile) + (3 * tempo_pace_per_mile)

end_time_minutes = start_minute + (total_time_seconds // 60)
end_time_hours = start_hour + (end_time_minutes // 60)
end_time_minutes = end_time_minutes % 60

print(f"{end_time_hours}:{end_time_minutes:02d}")  # 7:30
