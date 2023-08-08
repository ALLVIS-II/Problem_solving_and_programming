import random

print("--- Question 1 ---\n")

ask = input("Would you like to play rock-paper-scissors? (y/n) ---> ")

while ask not in ['y', 'n']:
    ask = input("Invalid input. Please enter 'y' or 'n'. Would you like to play rock-paper-scissors? (y/n) ---> ")

if ask == 'y':
    user_choice = int(input("Enter your choice (1 for rock, 2 for paper, 3 for scissors): "))
    while user_choice not in ['1', '2', '3']:
        user_choice = input("Invalid input. Please enter 1, 2, or 3: ")
        
    user_choice = int(user_choice)
    computer_choice = random.randint(1, 3)

    choices = ['rock', 'paper', 'scissors']

    print(f"Your choice: {choices[user_choice - 1]}")
    print(f"Computer's choice: {choices[computer_choice - 1]}")

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == 1 and computer_choice == 3:
    print("You win - rock broke scissors!")
elif user_choice == 2 and computer_choice == 1:
    print("You win - paper defeat rock")
elif user_choice == 3 and computer_choice == 2:
    print("You win - scissors cut paper!")
else:
    print("Computer wins!")

print("\n--- Question 3 ---\n")
full_name = input("Enter your full name: ")

name= full_name[0].upper()

for i in range(1, len(full_name)):
    if full_name[i - 1].isspace():
        name.append(full_name[i].upper())

print(f"Initials: {'.'.join(name)}.")

print("\n--- Question 4 ---\n")

inputstr = input("Enter a series of single-digit numbers with nothing separating them")

totalsum = 0

for i in inputstr:
    index = int(inputstr)
    totalsum +=inputstr
    
print(f"The sum are {totalsum}")

print("\n--- Question 5 ---\n")
#import random

total_turn = 0

while total_turn < 2:
    turn = random.choice(['H', 'T'])
    
    if turn == 'H':
        total_turn += 1
        print("you a flip a head")
    else:
        print("you flip a tail")

print(f"Turn total: {total_turn}")