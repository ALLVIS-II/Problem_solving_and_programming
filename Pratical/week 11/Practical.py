# -------------------------------- Question 1 --------------------------------

secretWord = ['p', 'y', 't', 'h', 'o', 'n']
blanks = '_' * len(secretWord)
blankWord = list(blanks)
guess = 't'

for k in range(len(secretWord)):
    if secretWord[k] == guess:
        blankWord(k) == secretWord(k)
        

# -------------------------------- Question 2 --------------------------------

index = 3

for i in range(1,index + 1):
    print('*'*i)
    

# -------------------------------- Question 4 --------------------------------
numbers = []


value = int(input("Enter a positive integer (0 or negative to stop): "))
while value < 0:
    numbers.append(value)
    value = int(input("Enter a positive integer (0 or negative to stop): "))

    # Calculate the largest, smallest, and median values
    largest = numbers[0]
    smallest = numbers[-1]
    
    if len(numbers) % 2 == 1:
        median = numbers[len(numbers) // 2]
    else:
        mid1 = numbers[len(numbers) // 2 - 1]
        mid2 = numbers[len(numbers) // 2]
        median = (mid1 + mid2) / 2

    # Print the sorted list and calculated values
    print("Sorted values in descending order:", numbers)
    print("Largest value:", largest)
    print("Smallest value:", smallest)
    print("Median value:", median)
else:
    print("No positive integers were entered.")

# -------------------------------- Question 5 --------------------------------


strList = ["I've", "made", "a", "huge", "mistake!"]

final = " ".join(strList)

print(final)


# 5a 

scores = [21, 92, 77, 53, 99, 87, 95]

index = 0

for i in scores:
    if scores > 90:
        index += 1

        
# -------------------------------- Question 6 --------------------------------


# 2
# 3
# 4
# 5
# 6
# 7

# 6b. 

# 27 

# -------------------------------- Question 7 --------------------------------
    
def happy():
    print("Happy Birthday to you!")
    

def sing(person):
    happy()
    happy()
    print(f"Happy birthday, dear {person}.")
    happy()
    
sing("Elmer")