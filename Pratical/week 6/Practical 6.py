#
  # File:      welcome.py
  # Author:    Lua Jin Yuan Alvis 
  # Email Id:  Luajy004@mymail.unisa.edu.au
  # Version:   1.0  5 August 2014
# # # #
#Description: Practical 1 - displays a welcome message to the screen. This is my own work as defined by the University's
#Academic Misconduct policy.
print("--- 1a ---\n")
total_Num = 0
index = 0

ask = int(input("Enter a number (Enter negative number to be stop) "))

while ask > 0:
    total_Num += ask
    ask = int(input("Enter a number (Enter negative number to be stop)"))
    
print(f"The total num is {total_Num}")

print("--- 1b ---\n")

count = 0
largest = 0
num = int(input("Enter a num (Enter 0 or negative number to be stop) "))

while num > 0:
    count += 1 
    if num > largest:
        largest = num
    num = int(input("Enter a num (Enter 0 or negative number to be stop) "))
print(f"The total num is {count}")
print(f"The total num is {largest}")

print("--- 1c ---")
smallest = ()
largest = ()
num = int(input("Enter a positive number (zero or negative to stop): "))

while num > 0:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
    num = int(input("Enter a positive number (zero or negative to stop): "))

diff = largest - smallest
print("Largest difference between values entered:", diff)

print("--- Question 2 ---")

index = 0 
maxNum = 15
count = 0

ask = ("Enter a num (input a num < 0 or > 15 will be stop)")
while ask > index or ask < maxNum:
    index += ask
    print(f"total ---> {index}")
    
    if index < maxNum:
        print("stop looping value bigger than 15")
        ask = int(input("Enter a number (negative number to stop or total > 15 to stop): "))
    
    if index < 0:
        print("Negative number entered. Stopping the loop.")
    else:
        print(f"Final total ---> {count}")
    

print("--- Quesion 3 ---")

def display_details():
    print("""
     Author: your name
     Email Id: your email id
     This is my own work as defined by the
     University's Academic Misconduct Policy.
     """)
display_details()

print("--- Question 4 ---")
def calculate_sum(numbersStr):
    total_sum = 0
    for digit in numbersStr:
        total_sum += int(digit)
    return total_sum

# Example usage:
numbersStr = '2514'
result = calculate_sum(numbersStr)
print("The sum of all single-digit numbers in the string is:", result)

print("--- Question 5 ---")

def determine_grade():
    index = float(input())
    if index > 0 and index <= 39:
        print("F2")
    elif index > 40 and index <= 49:
        print("F1")
    elif index > 50 and index <= 54:
        print("P2")
    elif index > 55 and index <= 64:
        print("P1")
    elif index > 65 and index <= 74:
        print("C")
    elif index > 75 and index <= 84:
        print("D")
    elif index > 85 and index <100:
        print("HD")
    else:
        ("invaild index")
determine_grade()

print("--- Question 6 ---")

def read_colour():
    index = ['red','blue','yellow']
    
    color = input("please choose a color {red, blue, yellow}")
    
    while color not in index:
        print("error index")
        color = input("please choose a color {red, blue, yellow}")
        
    return color

print(f"you choose {read_colour()}")

print("--- Question 7 ---")

def main():
    sales_list = []

    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        sales = float(input(f"Enter sales for {day}: "))
        sales_list.append(sales)
        
        total_sales = 0
    for sales in sales_list:
        total_sales += sales
        
        print(f"Total sales for the week: {total_sales}")
        
main()

print("--- Question 8 ---")

def main2():
    numbers_list = []

    # enter 20 nums in the list
    for i in range(20):
        num = int(input(f"Enter number {i + 1}: "))
        numbers_list.append(num)

    # Calculate the lowest and highest numbers
    lowest = numbers_list[0]
    highest = numbers_list[0]

    for num in numbers_list:
        if num < lowest:
            lowest = num
        if num > highest:
            highest = num

    total = 0
    for num in numbers_list:
        total += num

    # Calculate the average of the numbers
    average = total / len(numbers_list)

    # Display the results
    print(f"Lowest number: {lowest}")
    print(f"Highest number: {highest}")
    print(f"Total of the numbers: {total}")
    print(f"Average of the numbers: {average}")

print("--- Question 9 ---")


print("--- Question 10 ---")


print("--- Question 11 ---")
import random

def get_choice():
    selection = ['Rock', 'Paper', 'Scissors']
    while True:
        user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").capitalize()
        if user_choice in selection:
            return user_choice
        else:
            print("Invalid choice. Please enter Rock, Paper, or Scissors. ")
            

print("Part II: More Debugging Practise")
print("--- Exercise 1 ---")

numbers = [7, 3, 9, 2, 4]
count = 0
sumNo = 0

for num in numbers:
    sumNo += num
    count += 1

if count > 0:
    average = sumNo / count
    print("Average of numbers is:", average)
else:
    print("The list is empty. Cannot calculate the average.")
    
print("--- Exercise 2 ---")

def sum_numbers(no1, no2, no3):
    return no1 + no2 + no3


number1 = 2
number2 = 3
number3 = 4

result = (number1 + number2 + number3)

print("Sum of numbers is: ", result)

print("--- Exercise 3 ---")

def maximum( no1, no2, no3 ):
    maxValue = no1
    
    if no2 > maxValue:
        maxValue = no2
        
    if no3 > maxValue:
        maxValue = no3
        
    return maxValue

num1 = 4
num2 = 1
num3 = 7

result = maximum(num1, num2, num3)

print('Maximum is:', result)

print("--- Exercise 4 ---")
MAX_VERSES = 100 # maximum number of verses
numberOfVerses = 0 # users choice of number of verses
currentVerseNo = 0 # stores current verse number
answer = 0 # user's response

# Prompt and read whether the user wishes to sing a song. 
answer = input("Would you like to sing a song? ")

# While user continues to enter yes.
while answer == 'Y' or answer == 'y':
    # Prompt and read how many verses the user wishes to sing.
    numberOfVerses = int(input("\nHow many verses of the song do you wish to sing? "))
    
    # Validate input. Can't be less than or equal to zero or grater than 100. 
    while numberOfVerses <= 0 or numberOfVerses > MAX_VERSES:
        print("Not possible my friend ... \n")
        numberOfVerses = int(input("\nHow many verses of the song do you wish to sing? "))
        
        
    # Always start at 100 bottles of beer on the wall.
    currentVerseNo = MAX_VERSES
    
    # Loop number of verses times.
    for k in range(numberOfVerses):
        
         # Display verse.
       if currentVerseNo == 1:
            print(currentVerseNo, "bottle of beer on the wall") 
            print(currentVerseNo, "bottle of beer")
            print("If one of those bottles should happen to fall") 
            print("No bottles of beer on the wall!!\n")
       else:
            print(currentVerseNo, "bottles of beer on the wall") 
            print(numberOfVerses, "bottles of beer")
            print("If one of those bottles should happen to fall")
            
            currentVerseNo = currentVerseNo - 1
            if currentVerseNo == 1:
                print(currentVerseNo, "bottle of beer on the wall\n\n")
            else:
                print(currentVerseNo, "bottles of beer on the wall\n\n")


    # Prompt again.
    answer = input("\nThat was fun! Would you like to sing again? ")
