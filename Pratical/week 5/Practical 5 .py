print("""
--- Question 1--- 
What is the output produced by the following code? Check your answers using Python. 
      \n""")

# a) 3

# b) 8

# c) S
# o
# o
# o
#
# m
# u
# c
# h
#
# f
# u
# n
# !

# d) o
# o
# o
#
# m
# u
# c
# h

# f) Yes it is

# g) WTF!?!


# h) F!?!T!?!W

# i) 3

# j) 21 

# k) 25

# l) 0123456789

# m) ## ## ## !

print("\n--- Question 2 ---\n")
# a)

# 6
# 8
# 4
# 9
# 72
# 9

# b)
# 2
# four
# 10
# eight
# two
# 0
# 2

# c)
# These
# pretzels
# are
# making
# me
# thirsty!

# d)
# Tony Stark
# Lex Luthor
# Selina Kyle 
# Bruce Wayne
# Peter Parker

# e)
# Lex Luthor
# Bruce Wayne

print("\n--- Question 3 ---\n")
# a)
list1 = [7, 21, 1, 2, 5, 1, 15]

# b)
list2 = [0, 0, 0, 0, 0, 0, 0]

# c)
list2 = list1[1] + list2[3]

# d)
print(list2)

print("\n--- Question 4 ---\n")
# a) 
xy = [4, 3, 2, 1, 0, 'new', 'old']

# b)
print(xy)

# c) 
for i in xy:
    print(i)
# d)
st3 = xy[:3]
print("st3")

# e)
st3 = xy[-3:]
print(st3)

# f)
xy[4] = "same"

# g)
print(xy)

# h)
reversed_xy = xy[::-1]
print(reversed_xy)

print("\n--- Question 5 ---\n")
# Use a for loop to sum the elements in the following list:
numbers = [7, 8, 2, 0, 1, 6, 3, 4]

for i in numbers:
    ans = sum(numbers)
    
print(ans)

# Check your answer using the Python built-in sum function.
ans = sum(numbers)
    
print(ans)
    

print("\n--- Question 6 ---\n")

numbers = [7, 8, 2, 0, 1, 6, 3, 4]

sum_use_while = 0
index = 0
while index < len(numbers):
    ans = sum(numbers)
    index += 1

print(f"Sum use while loop: {sum_use_while}")

print("\n--- Question 7 ---\n")
# Use a for loop to count how many times the letter 'a' appears in the string 'fanta'.

str = "fanta"
countStr = 0

for i in len(str):
    if i == 'a':
        countStr += 1

print(f"there have {countStr} letter 'a' in the string")

# Check your answer using Python’s string method called count().

index = str.count("a")
print(f"there have {index} letter 'a' in the str")

print("\n--- Question 8 ---\n")
str = 'fanta'
countStr = 0
index = 0
while index < len(str):
    if str[index] == 'a':
        countStr += 1
    index += 1

print(f"there have {index} letter 'a' in the str")

print("\n--- Question 9---\n")

radii = [5, 2, 4, 3, 1]

for radius in radii:
    area = 3.14159 * radius * radius
    print(f"Radius is: {radius} Area is: {float(area)}")
    
print("\n--- PART 2 ---\n")
# excerise 1
count = 6
while count > 0:
   count = count - 1
print(f"Count is {count}")

# excerise 2

mark = 69
grade = ''
if mark >= 85:
    grade = 'HD'
elif mark >= 75:
    grade = 'D'
elif mark >= 65:
    grade = 'C'
elif mark >= 55:
    grade = 'P1'
elif mark >= 50:
    grade = 'P2'
elif mark >= 40:
    grade = 'F1'
else:
    grade = 'F2'
print('The grade is:', grade)

# excerise 3 

import random
play = 'y'
while play == 'y':
    # generate random number 1 - 100 inclusive
    number = random.randint(1,100)
    # prompt for and read user’s guess
  
    print('')
# determine whether user guessed correct random number while guess == number:
while play =='y':
    guess = int(input('Please enter your guess: '))
    if guess < number:
        print('Too low - please try again!')
    else:
        print('Too high - please try again!')
        # prompt for and read user’s guess
        guess = int(input('Please enter your guess: '))
        print('')
    print('Well done - you guessed it!')
# prompt for and read whether the user would like to play again play = input('Would you like to play again (y/n)? ')
print('')