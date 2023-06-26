
#
# File: practical2ex4.py
# Author: Lua Jin Yuan Alvis
# SAIBT ID: 43018
# Description: Practical 2, exercise 4.
# This is my own work as defined by SAIBT's
# Academic Misconduct policy.
#
import random
print("a)")
# number1 = 2
# number2 = 20
print(f"2")
print(f"20")
print(f"9\n")

print("-"*50,"\n")

print("b)")
# result = 14
print(f"14")
# result = 21
print(f"21\n")

print("-"*50,"\n")

print("c)")
# number1 = 3
# number1 = 5
# number1 = 8
print(f"8\n")

print("-"*50,"\n")

print("d)")
# number3 = 2
# number2 = 30 
# number1 = 7
print(f"7 30 2\n")

print("-"*50,"\n")

print("2)")
print("Please enter your favourite colour!!")

colour = input("")

print(f"{colour} is a lovely colour!")

print("\n\nPlease enter your favourite football team!!")
team = input("")
print(f"{team}! That's my favourite team too!\n")

print("-"*50,"\n")

print("3)")

width = 10
height = 5
area = width * height

print(f"The area is: {area}\n")

print("Please Enter a Height and Width")

finalHeight = input()
finalWidth = input()

finalArea = int(finalHeight) * int(finalWidth)

print(f"The area is: {finalArea}")
 
 
 
print("-"*50, "\n")

print("4)")

number1 = input("please enter number 1 \n")
number2 = input("please enter number 2 \n")
number3 = input("please enter number 3 \n")

math = int(number1) + int(number2) + int(number3)

print(math)


print("-"*50, "\n")

print("5)")

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

def Dice():
    print(f"Dice 1 is {dice1}")
    print(f"DIce 2 is {dice2}")
    
Dice()
    

print("-"*50, "\n")

print("6)")

square = input("Please enter the square of the height or width")

print(int(square)*2)

print("-"*50, "\n")

pi = 3.14

radius = input("Please enter a radius!")

area = int(pi) * int(radius)**2

print(f"the area of the circle is {area}")

print("-"*50, "\n")

print("8)")

male = input("number of male")
female = input("number of female")

maxSum = int(male) + int(female)

precentMale = male / maxSum
precentFemale = female / maxSum

print(f"The precentage of male in clss is {precentMale}")
print(f"The precentage of female in calss is {precentFemale}")

print("-"*50, "\n")

print("9)")


    