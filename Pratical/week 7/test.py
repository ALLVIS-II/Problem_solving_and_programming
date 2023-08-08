import random

    
user_choice = int(input("Enter your choice (1 for rock, 2 for paper, 3 for scissors): "))
computer_choice = random.randint(1, 3)

choices = ['rock', 'paper', 'scissors']

print(f"Your choice: {choices[user_choice - 1]}")
print(f"Computer's choice: {choices[computer_choice - 1]}")

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == 1 and computer_choice == 3:
    print("You win!")
elif user_choice == 2 and computer_choice == 1:
    print("You win")
elif user_choice == 3 and computer_choice == 2:
    print("You win")
else:
    print("Computer wins!")
