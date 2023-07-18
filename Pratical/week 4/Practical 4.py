
     # File:      filename.py
     # Author:    your name
     # Email Id:  your email id
     # Description:  Practical 4.
     #   This is my own work as defined by the University's
     #   Academic Misconduct policy.
     #
print("--- Question 1 ---")
print("What is the output produced by the following code? (Please look at the coding libary)")

# Homer Simpson
# Homer's Donuts
# mmmmmm Donuts
# m
# nuts
# Home
# o
# 7
# Doh!
print("\n---Question 2 ---\n")

str1 = "These pretzels are making me thirsty!"

# 1. Count how many times the letter 'e' appears in the string.
count_e = str1.count('e')
print(f"Occurrences of 'e': {count_e}")

# 2. Determine whether every character in the string is a digit.
digit = str1.isdigit()
print(f"Is all characters digits?{digit}")

# 3. Convert the string to lowercase.
lowercase = str1.lower()
print(f"Lowercase string: {lowercase}")

# 4. Convert the string to uppercase.
uppercase = str1.upper()
print(f"Uppercase string: {uppercase}")

# 5. Replace all whitespace characters with character '-'
replaced = str1.replace(' ', '-')
print(f"String with replaced whitespace: {replaced}")

print("\n--- Question 3 ---\n")

print("What is the output produced by the following programs (a-f)? (Please look at the coding libary")

# a. WTF!?!
# b. FTW!?!
# c. 38271
# d. 21
# e. Result is: 1045
# f. Result is:  100123456789

print("\n--- Question 4---\n")
# a. -->
import random
# b. -->
random_number = random.randint(1, 100)
user_guess = int(input("Guess the random number between 1 and 100: "))

while user_guess != random_number:
    user_guess = int(input("Guess the random number between 1 and 100: "))

    if user_guess == random_number:
        print("Well done - you guessed it!")
    else:
        print("Too bad - please try again!")
        
# c. -->

# import random

random_number = random.randint(1, 100)
user_guess = int(input("Guess the random number between 1 and 100: "))

while user_guess != random_number:
     if user_guess < random_number:
         print("Too low - please try again!")
     else:
         print("Too high - please try again!")
         
     user_guess = int(input("Guess the random number between 1 and 100: "))
     
print("Well done - you guessed it!")

# d. -->

play = 'y'
while play == 'y':
     random_number = random.randint(1, 100)
     
     user_guess = int(input("Guess the random number between 1 and 100: "))
     
     while user_guess != random_number:
          if user_guess < random_number:
               print("Too low - please try again!")
          else:
               print("Too high - please try again!")
               
          user_guess = int(input("Guess the random number between 1 and 100: "))
          
          
     print(input("want to play again(y/n)"))
     

print("\n --- Question 5 ---\n")

# no idea


print("\n--- Question 6 ---\n")
# a. -->
# import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

if die1 == die2:
     print(f"You rolled a pair of{die1}!")
else:
     print(f"You rolled a {die1} and a {die2}")
     
# b. -->

import random

pair_count = 0
rolls = 10

while rolls >= 0:
     die1 = random.randint(1, 6)
     die2 = random.randint(1, 6)

     if die1 == die2:
          pair_count += 1
          print(f"You rolled a pair of{die1}!")
     else:
          print(f"You rolled a {die1} and a {die2}")

     rolls -= 1
     

print("\n--- Question 7 ---\n")

num_bottles = 100

sing = input("would you like to sing a song(y/n)?")

valid_choices = ['y','n']

while sing not in valid_choices:
     sing = input("would you like tosing a song [y/n]?")
     
while sing == 'y':
     num_verses = int(input("how many verses of the song do you wish to sing?"))
     
     while num_verses < 1 or num_verses > 100:
          print(" Not possible my friend...")
          num_verses = int(input("how many verses of the song do you wish to sing?"))
          
     while num_verses > 0:
          print(f"{num_bottles} bottleof beer on the wall")
          print(f"{num_bottles} bottles of beer")
          print("if one of those bottles should happen to fail ")
          print(f"{num_bottles-1} bottle of beeron the wall\n\n")
          
          num_bottles -= 1
          num_verses -= 1
          sing = input("\n\nThat was fun! would you like to sing again [y/n]?")
          while sing not in valid_choices:
               sing = input("would you like to sing a song [y/n]?")
               
print("\n\nThank for singing along")