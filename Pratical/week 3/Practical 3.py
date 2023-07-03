#
  # File:      Practical 3.py
  # Author:    Lua Jin Yuan Alvis 
  # Email Id:  Luajy004@mymail.unisa.edu.au
  # Version:   1.0  5 August 2014
# # # #
#Description: Practical 1 - displays a welcome message to the screen. This is my own work as defined by the University's
#Academic Misconduct policy.
import random

# This is a layout format
print("1)")

number = int(input("Please enter your speed "))

if number >= 65:
    print("Too fast - Fine!")
    
else: print("No fine\n")

# This is a layout format
print("-"*50,"\n")
print("2)")

n = int(input("please enter a number between 1 - 100 "))

math_number = n % 2

if math_number == 0:
    print(f"{n} is an even number")
    
else: print(f"{n} is an odd number")

# This is a layout format
print("-"*50,"\n")
print("3)")

speed = int(input("Please enter your rocket speed to check the racket seprate stage "))

if speed >= 0 and speed < 100:
     print('you are in stage 1')
     
elif speed >= 100 and speed < 170:
     print('you are in stage 2')
     
elif speed >= 170 and speed <= 260:
     print('you are in stage 3')
     
else: print("ERROR")
# This is a layout format
print("-"*50,"\n")
print("4)")

temperature = float(input("Enter the temperature: "))

if temperature >= 40:
    print("Way too hot - stay inside!")
elif temperature >= 30:
    print("Hot - beach time!")
elif temperature >= 20:
    print("Lovely day - how about a picnic!?!")
elif temperature >= 10:
    print("On the cold side - better take a jacket!")
else:
    print("Way too cold - stoke up the fire!")
# This is a layout format
print("-"*50,"\n")
print("5)")


#import random
num = random.randint(1,10)

ans = 4

if ans != 4:
    print("Too bad - better luck next time!")
    
else: print("Well done - you guessed it!")

# This is a layout format
print("-"*50,"\n")
print("6)")


#import random
die1  = random.randint(1,6)
die2 = random.randint(1,6)

    
if die1 == die2:
    print(f"You rolled a pair of {die2}s!")
    
else: print(f"you rolled a {die1} and a {die2}")

# This is a layout format
print("-"*50,"\n")
print("7)")


index = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

num = int(input("please enter an integer between 1-10: "))

if num > 0 and num < 11:
     ramon = index [num - 1]
     print(ramon)
     
else: ("what is it")
# This is a layout format
print("-"*50,"\n")
print("8)")

day = input(f"Enter the day of month: ")
month = input(f"Enter the month in numeric form: ")
year = input(f"Enter the year in two digit format:")

print(f"The date {day}/{month}/{year} is a magic date")

# This is a layout format
print("-"*50,"\n")
print("9. Properly indent the following statements)\n")

# This is a layout format
print("b.")

a=1 
b=1 
c=1
if a == b:
    print('In if statement.') 
    print('Equal.') 
    
else: print('In else statement.')
 
print('Not equal.')

# This is a layout format
print("c.")

max = 5
count=0 
k=0
while k < max:
    count = count + 1 
    print('In while loop.') 
    k=k+1
    print('Count is: ', count)

# This is a layout format
print("-"*50,"\n")
print("10. What is the output produced by the following code?")
print("output answer in the code libary ( Line 152 )")


print("a.")

## Stuck in a loop!
# Stuck in a loop!
# Stuck in a loop!
# Stuck in a loop!
# Stuck in a loop!
## okay then...

print("b.")

## Still looping.
# Still looping.
## Still looping.

print("c.")

# Yes.

print("d.")

# Not equal.

print("e.")

# D

# This is a layout format
print("-"*50,"\n")
print("11)")


#import random


#generate a random num between 1 - 1000
#import random
randomNum = random.randint(1,1000)
even = 0
odd = 0
n = 0 # to get a num between 1 - 100

while n < 100:
    if randomNum % 2 == 0:
        even += 1
        
    else: odd += 1
    
    n += 1
    
print(f"Out of 100 random numbers, {odd} were odd, and {even} were even.")