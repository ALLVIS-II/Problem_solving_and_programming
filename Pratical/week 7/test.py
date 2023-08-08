import random

index = ['rock', 'paper', 'scissors']
player = int(input("Would you like to play rock-paper-scissor\n Enter\n '1' = rock \n '2' = paper \n '3' = scissors\n\n")) -1

computer = random.randint(0,2)

print(f"player choose {index[player]}")
print(f"computer choose {index[player]}")


if player == computer:
    print('Draw')
    
elif player == 0 and computer != player: # if player is ro
    if computer == 1: # computer is paper 
        print('you lose') # paper can defeat rock so I'm l
    else: 
        print('you win') # if opposite then I will win
    
elif player == 1 and computer != player: 
    if  computer == 2: 
        print('you lose')
    else: 
        print('you win')
    
elif player == 2 and computer != player:
    if computer == 0: 
        print('you lost')
    else: 
        print('you win')
        
