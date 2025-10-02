# Variables to keep track of the score:
import dice
import copy
from dice import rollD6

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

    player["name"] = input(f"What is the name of Player {i+1}?")
    player["email"] = input(f"What is the e-mail of Player {i+1}?")
    player["country"] = input(f"What is the country of Player {i+1}?")

    players.append(player)

# Repeats until the gam is over. As many rounds as necesary:
while gameover is False:
    print(f"Round {rounds+1}:")
    # input("\nPress ENTER to continue..."):

    # Dice roll for each player in the current round:
    current_rolls = []

    # We need to roll the dice for each player:
    for each_player in players:
        roll = dice.rollD6()

        #player_rolls_history.append(roll)
        each_player["rolls"].append(roll)

        current_rolls.append(roll)

        print(f"Player {each_player['name']} rolled: {roll }")

    # Obtain the highest roll this round:
    max_roll = max(current_rolls)

    # Find winners of the round:
    winners = []

    # Search for all players who got the highest roll:
    for each_player in players:
        if (each_player["rolls"][-1] == max_roll):
            each_player["wins"] += 1
            # Use rounds + 1 so the displayed round number starts at 1, matching earlier 'Round {rounds+1}' print.
            print(f"Player {each_player['name']} won in round {rounds + 1}")

            winners.append(each_player["name"])
    print(f"Winners of this round: {winners}")

    for each_player in players:
        if (each_player["wins"] >= winning_score):
            print(f"\n {each_player['name']} is the newest Battle of Dices champion!")
            gameover = True

    # Print continuation message only once per round (not per player)
    if not gameover:
        print("This heated Battle of Dices is still going on! Who will win in the end?")
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
    for r in range(rounds):
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

    print("\nGame over! Results saves successfully.")