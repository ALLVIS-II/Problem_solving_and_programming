import random

#title
print("--- Rock-paper-scissors ---")

#empty input for the game start or not
startGame = ""

#play game or not

while startGame not in ['y', 'n']:
    startGame = input("Do you want to play Rock-paper-scissors? (y/n): ")
    
    if startGame == 'y':
        print("Let's have a match with the computer here!")
    elif startGame == 'n':
        quit(0)
    else:
        print("Invalid input. Please enter 'y' or 'n'")
        
    
    playStyle = ["rock", "paper", "scissors"]

    player = int(input("Please choose your choice rock(1), paper(2), scissors(3): ")) - 1
    


    computer = random.randint(0,2)

    print(f"you chose {playStyle[player]}")

    print(f"computer chose {playStyle[computer]}")
    
        
    #math here

     # 0 is rock / 1 is paper / 2 is scissors
    if player == computer:
        print('Draw')
    
    elif player == 0 and computer != player: # if player is rock and computer is not rock 
        if computer == 1: # computer is paper 
            print('you lose') # paper can defeat rock so I'm lose
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
            

            
 
