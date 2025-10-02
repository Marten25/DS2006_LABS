# Import the dice rolling functions from the dice module.
from dice import rollD4, rollD6, rollD8, rollD12, rollD20, rollD100


# Welcome message
print("🎲 Welcome to Battle of Dices! 🎲")

# Function to print the summary table at the end
def lines(n):
    print("\n" + "-" * (12 + n * 10))

# Function to print the summary table at the end
def print_summary(rounds, dice_type, player1_rolls, player2_rolls, winner=None):
    lines(len(rounds))
    print(" ")
    print("Round:     ", end="")
    for i in range(len(rounds)):
        print(f"| {str(rounds[i]):^7}", end=" ")
    print("|")
    lines(len(rounds))
    print("Dice:      ", end="")
    for i in range(len(dice_type)):
        print(f"| {dice_type[i]:^7}", end=" ")
    print("|")
    lines(len(rounds))
    print("\nPlayer 1:  ", end="")
    for roll in player1_rolls:
        print(f"| {str(roll):^7}", end=" ")
    print("|")
    lines(len(rounds))
    print("\nPlayer 2:  ", end="")
    for roll in player2_rolls:
        print(f"| {str(roll):^7}", end=" ")
    print("|")
    lines(len(rounds))
    if winner:
        print(f"\nWinner: {winner}")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
rounds_played = 0 # Variable to count how many rounds have been played.

# Dictionary to map user choices to dice names
dice_names = {"1": "d4", "2": "d6", 
              "3": "d8", "4": "d12", 
              "5": "d20", "6": "d100"} 

# Ask the user to choose a dice type:
print("Choose your dice:")
print("1. d4")
print("2. d6")
print("3. d8")
print("4. d12")
print("5. d20")
print("6. d100")
choice = input("Enter the number of your choice: ") # We will use this choice to select the dice function.

# Map the user's choice to the corresponding dice function
if choice == "1":
    dice_func = rollD4
elif choice == "2":
    dice_func = rollD6
elif choice == "3":
    dice_func = rollD8
elif choice == "4":
    dice_func = rollD12
elif choice == "5":
    dice_func = rollD20
elif choice == "6":
    dice_func = rollD100
else:
    print("Invalid choice, BYE!!!")
    exit()




gameover = False # Variable to control when the game is over.
winner = None # Variable to store the winner's name.

# Lists to keep track of rolls for summary
player1_rolls = []
player2_rolls = []

# Game loop
while gameover is False: # We will keep playing until one of the players wins 3 times.
    
    # Start a new round
    input(f"\nPress ENTER to start round {rounds_played + 1}...")
    
    # Each player rolls the dice

    player1_roll = dice_func()
    player2_roll = dice_func()

    # Store rolls
    player1_rolls.append(player1_roll)
    player2_rolls.append(player2_roll)

    rounds_played += 1 # Increase the round counter by one.

    # Print round information
    print("Round", rounds_played) # Print the round number.

    # Print what each player rolled:
    print("Player 1 rolled: ", player1_roll)
    print("Player 2 rolled: ", player2_roll)
   
   # Compare the rolls to determine the round winner
    input("\nPress ENTER to continue...")
    if player1_roll > player2_roll: # Control if the player 1 roll is greater than player 2 roll.
        player1_wins += 1 # If so, we add one win to player 1.
        print("Player1 wins this round!")
        print("Because ", player1_roll," is greater than ", player2_roll)
    elif player2_roll > player1_roll: # Control if the player 2 roll is greater than player 1 roll.
        player2_wins += 1 # If so, we add one win to player 2.  
        print("Player2 wins this round!")
        print("Because ", player2_roll," is greater than ", player1_roll)
    else: # Control if both rolls are equal.
        print("Amaaazzinng! This round has a tie!")
    

    # We can print the game score:
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player2.")
    

    print(" ")
    # Now we need to check if either player won.
    if player1_wins == 3:
        print("Player1 beat Player2. Player2 is a LOSER! ")
        winner = "Player1"
        gameover = True
    elif player2_wins == 3:
        print("Player2 beat Player1. Player1 is a LOSER! ")
        winner = "Player2"
        gameover = True
    else:
        print("This heated Battle of Dices is still going on! Who will win in the end?")
    print(" ")
# End of the game loop

# Prepare data for the summary
dice_type = [dice_names[choice]] * rounds_played
count_list = list(range(1, rounds_played+1))

# Print the game summary
print_summary(count_list, dice_type, player1_rolls, player2_rolls, winner)

# Ask the user for a filename to save the results
filename = input("Save the results. Name a file: ")

# Save the summary to a file


def file_lines(n):
    return "\n" + "-" * (12 + n * 10) + "\n"

with open(filename, "w") as file:
    n = len(count_list)
    file.write(file_lines(n))
    file.write(" \n")
    file.write("Round:     ")
    for i in range(n):
        file.write(f"| {str(count_list[i]):^7}")
    file.write(" |\n")
    file.write(file_lines(n))
    file.write("Dice:      ")
    for i in range(n):
        file.write(f"| {dice_type[i]:^7}")
    file.write(" |\n")
    file.write(file_lines(n))
    file.write("\nPlayer 1:  ")
    for roll in player1_rolls:
        file.write(f"| {str(roll):^7}")
    file.write(" |\n")
    file.write(file_lines(n))
    file.write("\nPlayer 2:  ")
    for roll in player2_rolls:
        file.write(f"| {str(roll):^7}")
    file.write(" |\n")
    file.write(file_lines(n))
    if winner:
        file.write(f"\nWinner: {winner}\n")

# Last message before the game ends.
print(f"Results saved to {filename}. Bye!!!")