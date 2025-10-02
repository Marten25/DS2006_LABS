# Import the dice rolling functions from the dice module.
from dice import rollD4, rollD6, rollD8, rollD12, rollD20, rollD100


print("🎲 Welcome to Battle of Dices! 🎲\n")

# Number of wins needed to win the game
winning_score = 3
rounds_played = 0

# Array for storing the names of the players:
player_names = []
player_wins = []
player_rolls_history = []  # New: stores each player's per-round totals

# Initialize game state
gameover = False

# Get number of players
number_of_players = int(input("How many players?: ")) # This game is for two players only.

# Collect names and init wins in one loop
for i in range(number_of_players):
    name = input(f"What is the name of Player {i+1}?: ")
    player_names.append(name) # Store player name
    player_wins.append(0) # init wins to 0
    player_rolls_history.append([])  # init empty history list for this player

# Dice options
print("Choose your dice:\n")
print("1. d4")
print("2. d6")
print("3. d8")
print("4. d12")
print("5. d20")
print("6. d100\n")
print("Choose your two dices: ")

# Get the first dice choice from the player.
choice1 = input("Choose the first dice: ")

# Assign the first dice functions based on player choices.
if choice1 == "1":
    dice1, dicename1 = rollD4, "d4"
elif choice1 == "2":
    dice1, dicename1 = rollD6, "d6"
elif choice1 == "3":
    dice1, dicename1 = rollD8, "d8"
elif choice1 == "4":
    dice1, dicename1 = rollD12, "d12"
elif choice1 == "5":
    dice1, dicename1 = rollD20, "d20"
elif choice1 == "6":
    dice1, dicename1 = rollD100, "d100"
else:
    print("Invalid choice, BYE!!!") # If the choice is invalid, the game ends.
    exit()

choice2 = input("Choose the second dice: ") # Get the second dice choice from the player.
print(" ")

# Assign the second dice functions based on player choices.
if choice2 == "1":
    dice2, dicename2 = rollD4, "d4"
elif choice2 == "2":
    dice2, dicename2 = rollD6, "d6"
elif choice2 == "3":
    dice2, dicename2 = rollD8, "d8"    
elif choice2 == "4":
    dice2, dicename2 = rollD12, "d12"
elif choice2 == "5":
    dice2, dicename2 = rollD20, "d20"
elif choice2 == "6":
    dice2, dicename2 = rollD100, "d100"
else:
    print("Invalid choice, BYE!!!") # If the choice is invalid, the game ends.
    exit()    

# Start the game loop.
while not gameover:  # the game will go on until one of the players wins 3 times.
    
    # Prompt to start the round
    input(f"Press ENTER to start round {rounds_played + 1}...\n")

    # Round announcement
    print("Round", rounds_played + 1)

    # Each player rolls both dice and we store totals for this round
    round_totals = []
    for idx in range(number_of_players):  # idx is the player index
        roll1 = dice1()  # Roll the first dice
        roll2 = dice2()  # Roll the second dice
        total = roll1 + roll2  # Calculate total for players
        round_totals.append(total)  # Store the total for this round
        player_rolls_history[idx].append(total)  # record total for saving later
        # print the result of the rolls for players
        print(f"{player_names[idx]} rolled {dicename1} and got {roll1} and {dicename2} and got {roll2} with a total of {total}")

    input("Press ENTER to continue...\n")
    
    # 
    highest_total = max(round_totals)
    winners = []

    # Loop to find all players who rolled the highest total
    for i in range(len(round_totals)):
        if round_totals[i] == highest_total:
            winners.append(player_names[i])
            player_wins[i] += 1

    if len(winners) == 1:
        print(f"{winners[0]} wins this round with {highest_total}!")
    else:
        print("Tie round! Winners:", ", ".join(winners), f"with {highest_total}")

    # Detailed scoreboard lines
    print("Scoreboard:")
    for i in range(number_of_players):
        print(f"  {player_names[i]} -> {player_wins[i]}")

    # Increment rounds played
    rounds_played += 1

    # Check for any winner
    game_winner = []
    for i in range(len(player_wins)):
        if player_wins[i] >= winning_score:
            game_winner.append(player_names[i])
    if game_winner:
        if len(game_winner) == 1:
            print(f"\n{game_winner[0]} is the Battle of Dices winner in {rounds_played} rounds!")
        else:
            print(f"\nMultiple winners: {', '.join(game_winner)} reached {winning_score} wins!")
        gameover = True
    else:
        print("The battle continues...\n")

filename = input("Enter the filename to save the results: ")
with open(filename, "w") as file:  # "w" = write mode
    for round_number in range(rounds_played):
        file.write(f"Round {round_number + 1}:\n")
        rolls_str = ""
        for i in range(number_of_players):
            rolls_str += f"{player_names[i]} rolled {player_rolls_history[i][round_number]}"
            if i < number_of_players - 1:
                rolls_str += ", "
        print(f"Saving {rolls_str}")
        file.write(rolls_str + "\n")
    
    # Add who won the game as last string
    if len(game_winner) == 1:
        file.write(f"Game winner: {game_winner[0]}")
    else:
        file.write(f"Game winners: {', '.join(game_winner)}")