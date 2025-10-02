# Import the dice rolling functions from the dice module.
from dice import rollD4, rollD6, rollD8, rollD12, rollD20, rollD100

print("🎲 Welcome to Battle of Dices! 🎲")
  
# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
rounds_played = 0 # Variable to count how many rounds have been played.

print("Choose your dice:")
print("1. d4")
print("2. d6")
print("3. d8")
print("4. d12")
print("5. d20")
print("6. d100")
choice = input("Enter the number of your choice: ")

if choice == "1":
    dice = rollD4
elif choice == "2":
    dice = rollD6
elif choice == "3":
    dice = rollD8
elif choice == "4":
    dice = rollD12
elif choice == "5":
    dice = rollD20
elif choice == "6":
    dice = rollD100
else:
    print("Invalid choice, BYE!!!") # If the choice is invalid, we exit the game.
    exit()

gameover = False # Variable to control when the game is over.

while not gameover: # We will keep playing until one of the players wins 3 times.
    input(f"\nPress ENTER to start round {rounds_played + 1}...")
    player1_roll = dice()
    player2_roll = dice()

    print("Round", rounds_played + 1) # Print the round number and add one to the variable.

    # Print the chosen die.
    print("Player 1 rolled: ", player1_roll)
    print("Player 2 rolled: ", player2_roll)
    # So far so good right? But how to check who got the highest roll?
   
    input("\nPress ENTER to continue...")
    if player1_roll > player2_roll: # Control if the player 1 roll is greater than player 2 roll.
        player1_wins += 1 # If so, we add one win to player 1.
        print("Player 1 wins this round!")
        print("Because ", player1_roll," is greater than ", player2_roll)
    elif player2_roll > player1_roll: # Control if the player 2 roll is greater than player 1 roll.
        player2_wins += 1 # If so, we add one win to player 2.  
        print("Player 2 wins this round!")
        print("Because ", player2_roll," is greater than ", player1_roll)
    else: # Control if both rolls are equal.
        print("Amaaazzinng! This round has a tie!")
    

    # We can print the game score:
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
    rounds_played += 1

    print(" ")
    
    # Now we need to check if either player won.
    if player1_wins == 3:
        print("Player 1 beat Player 2. Player 2 is a LOOSER! ")
        gameover = True # The game is over.
        print("The game was won in", rounds_played, "rounds.")
    elif player2_wins == 3:
        print("Player 2 beat Player 1. Player 1 is a LOOSER! ")
        gameover = True # The game is over.
        print("The game was won in", rounds_played, "rounds.")
    else:
        print("This heated Battle of Dices is still going on! Who will win in the end? ") # The game continues.
    print(" ") 
    # Since none of them would have won after 1 round, we could copy this code several times
    # until we have enough times to make sure someone wins.