# Exercise 9.1
def long_words(filename):
    with open(filename, 'r') as file:
        for word in file:
            word = word.strip() 
            if len(word) > 20:
                print(word)

long_words('words.txt')

# Exercise 9.2
def has_no_e(word):
    return 'e' not in word

def words_without_e(filename):
    total_words = 0
    no_e_words = 0

    with open(filename, 'r') as file:
        for word in file:
            word = word.strip()
            total_words += 1
            if has_no_e(word):
                print(word)
                no_e_words += 1

    percentage = (no_e_words / total_words) * 100
    print(f"Percentage of words without 'e': {percentage:.2f}%")

words_without_e('words.txt')

# Exercise 9.3
def avoids(word, forbidden):
    for letter in forbidden:
        if letter in word:
            return False
    return True

def count_words_without_forbidden(filename, forbidden):
    count = 0

    with open(filename, 'r') as file:
        for word in file:
            word = word.strip()
            if avoids(word, forbidden):
                count += 1

    print(f"Number of words that avoid '{forbidden}': {count}")

forbidden_letters = input("Enter forbidden letters: ")
count_words_without_forbidden('words.txt', forbidden_letters)

# Exercise 9.4
def uses_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True

def find_words_with_only(filename, letters):
    with open(filename, 'r') as file:
        for word in file:
            word = word.strip()
            if uses_only(word, letters):
                print(word)

find_words_with_only('words.txt', 'acefhlo')


