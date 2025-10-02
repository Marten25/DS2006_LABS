# Import the dice rolling functions from the dice module.
from dice import rollD4, rollD6, rollD8, rollD12, rollD20, rollD100
import copy

# Welcome message
print("🎲 Welcome to Battle of Dices! 🎲\n")

# Initialize game variables
rounds = 0
gameover = False

# number of wins needed to win the game:
winning_score = 3

# Dictionary Template for storing player information:
player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": [],
}

# List to store the dicts for each player:
players = []

# Obtain the number of players:
number_of_players = int(input("How many players?"))

# For loop to obtain the player names:
for i in range(number_of_players):

    # Make a deep copy of the template for this player:
    player = copy.deepcopy(player_info)

    # Obtain player information
    player["name"] = input(f"What is the name of Player {i+1}?")
    player["email"] = input(f"What is the e-mail of Player {i+1}?")
    player["country"] = input(f"What is the country of Player {i+1}?")

    players.append(player) # Add the player to the list.

# Dice selection using a dictionary mapping instead of many if/elif blocks.
dice_map = {
    "1": (rollD4, "d4"),
    "2": (rollD6, "d6"),
    "3": (rollD8, "d8"),
    "4": (rollD12, "d12"),
    "5": (rollD20, "d20"),
    "6": (rollD100, "d100"),
}

# Display dice options and prompt for selection
print("Choose your dice:\n")
for key, (_, name) in dice_map.items():
    print(f"{key}. {name}")
print("\nChoose your two dice:")

# Function to choose a dice based on user input
def choose_dice(prompt: str):
    choice = input(prompt).strip()
    if choice in dice_map:
        return dice_map[choice]
    print("Invalid choice, BYE!!!")
    exit()

# Choose two dice for the game
dice1, dicename1 = choose_dice("Choose the first dice: ")
dice2, dicename2 = choose_dice("Choose the second dice: ")
print()

# Start the game loop.
while not gameover:  # the game will go on until one of the players wins 3 times.
    
    # Prompt to start the round
    input(f"Press ENTER to start round {rounds+1}...\n")

    # Round announcement
    print("Round", rounds+1)

    current_rolls = []  # Store the rolls for this round

    for each_player in players:
        roll1 = dice1()
        roll2 = dice2()
        total_roll = roll1 + roll2
        #player_rolls_history.append(roll)
        each_player["rolls"].append(total_roll)

        current_rolls.append(total_roll) # Store the total roll for this round

        # Print the individual roll results
        print(f"Player {each_player['name']} rolled: {roll1} + {roll2} = {roll1 + roll2}")

    input("Press ENTER to continue...\n")

    # Find the highest total roll for this round
    max_roll = max(current_rolls)
    winners = []

    # Loop to find all players who rolled the highest total
    # Search for all players who got the highest roll:
    for each_player in players:
        if (each_player["rolls"][-1] == max_roll):
            each_player["wins"] += 1
            print(f"Player {each_player['name']} won in round {rounds+1}")

            winners.append(each_player["name"])
    print(f"Winners of this round: {winners}")

    # Check after the round (only once per round, not per player)
    for each_player in players:
        if each_player["wins"] >= winning_score:
            print(f"\n {each_player['name']} is the newest Battle of Dices champion!")
            gameover = True
    # Print continuation message only once per round (not per player)
    if not gameover:
        print("This heated Battle of Dices is still going on! Who will win in the end?")

    # Increment rounds ONCE per completed round
    rounds += 1

# Save results to a file
filename = input("Enter the filename and save the results: ")
with open(filename, "w") as file: # "w" = write mode
    # Player information:
    file.write("Player Information:\n")

    # Saves each player information using the python automatically concatenation
    # of adjent strings:
    for each_player in players:
        file.write(
            f"Name: {each_player['name']}\n"
            f"* E-mail: {each_player['email']}\n"
            f"* Country: {each_player['country']}\n"
            f"* Wins: {each_player['wins']}\n"
        )
    file.write("\nGame rounds:\n")

    # Round history
    total_rounds = len(players[0]["rolls"]) if players else 0
    for r in range(total_rounds):
        # Start with empty text for this round
        rolls_str = ""

        # Go through each player and buils the string step by step
        for i, each_player in enumerate(players):
            rolls_str += f"{each_player['name']} rolled {each_player['rolls'][r]}"

            # Add a comma and space unless it's the last player
            if i < len(players) - 1:
                rolls_str += ", "

            # Now write the full round info in the file
        file.write(f"Round {r+1}:\n {rolls_str}\n")

    print("\nGame over! Results saved successfully.")