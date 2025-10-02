# Import the dice rolling functions from the dice module.
from dice import rollD4, rollD6, rollD8, rollD12, rollD20, rollD100


print("🎲 Welcome to Battle of Dices! 🎲\n")


# Variables to keep track of the score:
player1_wins = 0 # Player 1 win counter.
player2_wins = 0 # Player 2 win counter.
gameover = False # Variable to control when the game is over.
rounds_played = 0 # Variable to count how many rounds have been played.


# Print out the dice options.
print("Choose your dice:\n")
print("1. d4")
print("2. d6")
print("3. d8")
print("4. d12")
print("5. d20")
print("6. d100\n")
print("Pick two different dices by entering the corresponing number")
   

choice1 = input("Choose the first dice: ") # Get the first dice choice from the player.

# Assign the first dice functions based on player choices.
if choice1 == "1":
    dice1 = rollD4
    dicename1 = "d4"
elif choice1 == "2":
    dice1 = rollD6
    dicename1 = "d6"
elif choice1 == "3":
    dice1 = rollD8 
    dicename1 = "d8"
elif choice1 == "4":
    dice1 = rollD12 
    dicename1 = "d12"
elif choice1 == "5":
    dice1 = rollD20 
    dicename1 = "d20"
elif choice1 == "6":
    dice1 = rollD100
    dicename1 = "d100"
else:
    print("Invalid choice, BYE!!!") # If the choice is invalid, the game ends.
    exit()

choice2 = input("Choose the second dice: ") # Get the second dice choice from the player.
print(" ")

# Assign the second dice functions based on player choices.
if choice2 == "1":
    dice2 = rollD4
    dicename2 = "d4"
elif choice2 == "2":
    dice2 = rollD6
    dicename2 = "d6"
elif choice2 == "3":
    dice2 = rollD8
    dicename2 = "d8"    
elif choice2 == "4":
    dice2 = rollD12
    dicename2 = "d12"
elif choice2 == "5":
    dice2 = rollD20
    dicename2 = "d20"
elif choice2 == "6":
    dice2 = rollD100
    dicename2 = "d100"
else:
    print("Invalid choice, BYE!!!") # If the choice is invalid, the game ends.
    exit()    

# Prevent picking the same dice twice.
if choice1 == choice2:
    print("You cannot pick the same dice twice. BYE!!!")
    exit()


# Start the game loop.
while not gameover: # the game will go on until one of the players wins 3 times.

    input(f"Press ENTER to start round {rounds_played + 1}...\n")
    

    # Each player rolls both dices.
    player1_roll1 = dice1()
    player1_roll2 = dice2()
    player2_roll1 = dice1()
    player2_roll2 = dice2()

    # Print out the results of the rolls.
    print("Round", rounds_played + 1)
    print(f"Player 1 rolled {dicename1} and got a {player1_roll1}")
    print(f"Player 1 rolled {dicename2} and got a {player1_roll2}")
    print(f"Player 2 rolled {dicename1} and got a {player2_roll1}")
    print(f"Player 2 rolled {dicename2} and got a {player2_roll2}\n")
    
   # Calculate the total of both rolls for each player.
    total_player1 = player1_roll1 + player1_roll2
    total_player2 = player2_roll1 + player2_roll2

    input("Press ENTER to continue...\n")


    # Compare the total rolls to determine if there is a round winner.
    if total_player1 > total_player2: 
        player1_wins += 1 
        print("Player 1 wins this round!")
        print(f"Because {total_player1} is greater than {total_player2}")
    elif total_player2 > total_player1: 
        player2_wins += 1   
        print("Player 2 wins this round!")
        print(f"Because {total_player2} is greater than {total_player1}")
    else: 
        print("Amaaazzinng! This round has a tie!")
    

    # Show the current score.
    print(f"The game score is Player1 [{player1_wins} vs. {player2_wins}] Player 2.\n")
    

    rounds_played += 1 # Increase the round counter.
    

    # Checking if there is a winner.
    if player1_wins == 3:
        print("Player 1 beat Player 2. Player 2 is a LOOSER! ")
        gameover = True # The game is over.
        print(f"Player 1 won in {rounds_played} rounds.")
    elif player2_wins == 3:
        print("Player 2 beat Player 1. Player 1 is a LOOSER! ")
        gameover = True # The game is over.
        print(f"Player 2 won in {rounds_played} rounds.")
    else:
        print("This heated Battle of Dices is still going on! Who will win in the end?\n\n") # The game continues.
    