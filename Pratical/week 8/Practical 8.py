print("----- Question 1 ----")

def multiply_numbers(num1,num2,num3):
    adds = num1*num2*num3
    return adds

a = 2
b = 3
c = 4

result = multiply_numbers(a,b,c)

print(f"the product of {a},{b},{c} are {result}")

print("\n----- Question 2 -----")

def maximum(a,b):
    if a > b:
        return a
    else:return b
    
num1 = 10
num2 = 5

number = maximum(num1,num2)

print(f"THe maxiume number of {num1} and {num2} is {number}")

print("\n----- Question 3 -----")

import random
def get_random(a):
    integer = random.randint(1,a)
    
    return integer
num = 10

for _ in range(10):
    guess = get_random(num)

    print(guess)

print("\n----- Question 4 -----")

def capitalize_words(cap):
    words = cap.split()
    cap_words = [word.capitalize() for word in words]
    return ' '.join(cap_words)
user_input = input("Whats your name")

fix = capitalize_words(user_input)
print(f"you name is {fix}")

print("\n----- Question 5 -----")

def sum_list(numbers_list):
    total = 0
    for num in numbers_list:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
result = sum_list(numbers)

print(f"The sum of the numbers in the list is: {result}")

print("\n----- Question 6 -----")


def generate_lotto_number():
    num = []
    for _ in range(7):
        random_digit = random.randint(0, 9)
        num.append(random_digit)
    return num

print(f"generated lotto number: {generate_lotto_number()}")

# b)
def display_lotto_number(numList):
    numbers = ', '.join(str(num) for num in numList)
    print(numbers)

display_lotto_number(num)

# c) 
for i in range(20):
    num = generate_lotto_number()
    display_lotto_number(num)

print("\n----- Question 7 -----")

def display_with_dash(word):
    formatWord = '-'.join(word)
    return print(formatWord)

words = ['Elvis', 'has', 'left', 'the', 'building!']

for i in words:
    display_with_dash(i)

print("\n----- Question 8 -----")

def calculate_sum(string):
    total = 0
    for n in string:
        digit = int(n)
        total += digit
    return total

math = input("put some number here ")

print(f"the num are {calculate_sum(math)}")





        