import random

#title
print("--- Rock-paper-scissors ---")

#empty input for the game start or not
game = ""


#play game or not

while game not in ['y', 'n']:
    game = input("Do you want to play Rock-paper-scissors? (y/n): ")
    
    if game == 'y':
        print("Let's have a match with the computer here!")
    elif game == 'n':
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'")
        
    
    playStyle = ["rock", "paper", "scissors"]

    player = int(input("Please choose your choice rock(1), paper(2), scissors(3): ")) - 1
    


    pc = random.randint(0,2)

    print(f"you chose {playStyle[player]}")

    print(f"computer chose {playStyle[pc]}")
    
        
    #math here

     # 0 is rock / 1 is paper / 2 is scissors
    if player == pc:
        print('Draw')
    
    elif player == 0 and pc != player: # if player is rock and pc is not rock 
        if pc == 1: # pc is paper 
            print('you lose') # paper can defeat rock so I'm lose
        else: 
            print('you win') # if opposite then I will win
    
    elif player == 1 and pc != player: 
        if pc == 2: 
            print('you lose')
        else: 
            print('you win')
        
    elif player == 2 and pc != player:
        if pc == 0: 
            print('you lost')
        else: 
            print('you win')
            

            
    playagain = input("Want to play again (y/n)>>>")
    if playagain != 'y':
        break
