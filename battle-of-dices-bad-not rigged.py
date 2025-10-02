# We will use the random module to simulate dice rolls.
import random

# Welcome message
print("🎲 Welcome to Battle of Dices! 🎲")
  
# Variables to keep track of the score and results:
player1_wins = 0
player2_wins = 0
round_counter = 1

# To keep track of the rounds, dice used, and rolls for summary
rounds = []
dice = []
player1_rolls = []
player2_rolls = []

# Function to print the summary table at the end
def print_summary():
    def lines(): print("\n" + "-" * (12 + len(rounds) * 10)) 

    lines()
    print(" ")
    print("Round:     ", end="")
    for i in range(len(rounds)):
        print(f"| {str(i+1):^7}", end=" ")
    print("|")
    lines()
    print("Dice:      ", end="")
    for i in range(len(rounds)):
        print(f"| {dice[i]:^7}", end=" ")
    print("|")
    lines()
    print("\nPlayer 1:  ", end="")
    for roll in player1_rolls:
        print(f"| {str(roll):^7}", end=" ")
    print("|")
    lines()
    print("\nPlayer 2:  ", end="")
    for roll in player2_rolls:
        print(f"| {str(roll):^7}", end=" ")
    print("|")
    lines()

# Round 1
# Simulate rolling a D12 for both players
player1_round_1 = random.randint(1, 12)
player2_round_1 = random.randint(1, 12)

# Update the rounds, dice, and rolls lists
rounds.append(round_counter)
dice.append('d12')
player1_rolls.append(player1_round_1)
player2_rolls.append(player2_round_1)
round_counter += 1

# Display the rolls
print("Player 1 rolled: ", player1_round_1)
print("Player 2 rolled: ", player2_round_1)

# Determine the winner of the round
if player1_round_1 > player2_round_1:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round_1, " is greater than ", player2_round_1)
elif player2_round_1 > player1_round_1:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_round_1, " is greater than ", player1_round_1)
else:
    print("Amaaazzinng! This round has a tie!")

# Update the game score
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Check if there's a winner
if player1_wins == 3 or player2_wins == 3:
    print_summary() # Print the summary if there's a winner
    if player1_wins == 3:
        print("Player 1 beat Player 2. Player 2 is a LOOSER! ")
    else:
        print("Player 2 beat Player 1. Player 1 is a LOOSER! ")
    exit()

# Since none of them would have won after 1 round, we could copy this code several times
# until we have enough times to make sure someone wins.



# Round 2
player1_round_2 = random.randint(1, 12)
player2_round_2 = random.randint(1, 12)
rounds.append(round_counter)
dice.append('d12')
player1_rolls.append(player1_round_2)
player2_rolls.append(player2_round_2)
round_counter += 1

print("Player 1 rolled: ", player1_round_2)
print("Player 2 rolled: ", player2_round_2)

if player1_round_2 > player2_round_2:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round_2, " is greater than ", player2_round_2)
elif player2_round_2 > player1_round_2:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_round_2, " is greater than ", player1_round_2)
else:
    print("Amaaazzinng! This round has a tie!")

print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

if player1_wins == 3 or player2_wins == 3:
    print_summary()
    if player1_wins == 3:
        print("Player 1 beat Player 2. Player 2 is a LOOSER! ")
    else:
        print("Player 2 beat Player 1. Player 1 is a LOOSER! ")
    exit()

 # Round 3
player1_round_3 = random.randint(1, 12)
player2_round_3 = random.randint(1, 12)
rounds.append(round_counter)
dice.append('d12')
player1_rolls.append(player1_round_3)
player2_rolls.append(player2_round_3)
round_counter += 1

print("Player 1 rolled: ", player1_round_3)
print("Player 2 rolled: ", player2_round_3)

if player1_round_3 > player2_round_3:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round_3, " is greater than ", player2_round_3)
elif player2_round_3 > player1_round_3:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_round_3, " is greater than ", player1_round_3)
else:
    print("Amaaazzinng! This round has a tie!")

print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

if player1_wins == 3 or player2_wins == 3:
    print_summary()
    if player1_wins == 3:
        print("Player 1 beat Player 2. Player 2 is a LOOSER! ")
    else:
        print("Player 2 beat Player 1. Player 1 is a LOOSER! ")
    exit()


 # Round 4
player1_round_4 = random.randint(1, 12)
player2_round_4 = random.randint(1, 12)
rounds.append(round_counter)
dice.append('d12')
player1_rolls.append(player1_round_4)
player2_rolls.append(player2_round_4)
round_counter += 1

print("Player 1 rolled: ", player1_round_4)
print("Player 2 rolled: ", player2_round_4)

if player1_round_4 > player2_round_4:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round_4, " is greater than ", player2_round_4)
elif player2_round_4 > player1_round_4:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_round_4, " is greater than ", player1_round_4)
else:
    print("Amaaazzinng! This round has a tie!")

print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

if player1_wins == 3 or player2_wins == 3:
    print_summary()
    if player1_wins == 3:
        print("Player 1 beat Player 2. Player 2 is a LOOSER! ")
    else:
        print("Player 2 beat Player 1. Player 1 is a LOOSER! ")
    exit()


 # Round 5
player1_round_5 = random.randint(1, 12)
player2_round_5 = random.randint(1, 12)
rounds.append(round_counter)
dice.append('d12')
player1_rolls.append(player1_round_5)
player2_rolls.append(player2_round_5)
round_counter += 1

print("Player 1 rolled: ", player1_round_5)
print("Player 2 rolled: ", player2_round_5)

if player1_round_5 > player2_round_5:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round_5, " is greater than ", player2_round_5)
elif player2_round_5 > player1_round_5:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_round_5, " is greater than ", player1_round_5)
else:
    print("Amaaazzinng! This round has a tie!")

print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

if player1_wins == 3 or player2_wins == 3:
    print_summary()
    if player1_wins == 3:
        print("Player 1 beat Player 2. Player 2 is a LOOSER! ")
    else:
        print("Player 2 beat Player 1. Player 1 is a LOOSER! ")
    exit()

 # Round 6
player1_round_6 = random.randint(1, 12)
player2_round_6 = random.randint(1, 12)
rounds.append(round_counter)
dice.append('d12')
player1_rolls.append(player1_round_6)
player2_rolls.append(player2_round_6)
round_counter += 1

print("Player 1 rolled: ", player1_round_6)
print("Player 2 rolled: ", player2_round_6)

if player1_round_6 > player2_round_6:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round_6, " is greater than ", player2_round_6)
elif player2_round_6 > player1_round_6:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_round_6, " is greater than ", player1_round_6)
else:
    print("Amaaazzinng! This round has a tie!")

print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

if player1_wins == 3 or player2_wins == 3:
    print_summary()
    if player1_wins == 3:
        print("Player 1 beat Player 2. Player 2 is a LOOSER! ")
    else:
        print("Player 2 beat Player 1. Player 1 is a LOOSER! ")
    exit()


 # Round 7
player1_round_7 = random.randint(1, 12)
player2_round_7 = random.randint(1, 12)
rounds.append(round_counter)
dice.append('d12')
player1_rolls.append(player1_round_7)
player2_rolls.append(player2_round_7)
round_counter += 1

print("Player 1 rolled: ", player1_round_7)
print("Player 2 rolled: ", player2_round_7)

if player1_round_7 > player2_round_7:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round_7, " is greater than ", player2_round_7)
elif player2_round_7 > player1_round_7:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_round_7, " is greater than ", player1_round_7)
else:
    print("Amaaazzinng! This round has a tie!")

print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

if player1_wins == 3 or player2_wins == 3:
    print_summary()
    if player1_wins == 3:
        print("Player 1 beat Player 2. Player 2 is a LOOSER! ")
    else:
        print("Player 2 beat Player 1. Player 1 is a LOOSER! ")
    exit()


 # Round 8
player1_round_8 = random.randint(1, 12)
player2_round_8 = random.randint(1, 12)
rounds.append(round_counter)
dice.append('d12')
player1_rolls.append(player1_round_8)
player2_rolls.append(player2_round_8)
round_counter += 1

print("Player 1 rolled: ", player1_round_8)
print("Player 2 rolled: ", player2_round_8)

if player1_round_8 > player2_round_8:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round_8, " is greater than ", player2_round_8)
elif player2_round_8 > player1_round_8:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_round_8, " is greater than ", player1_round_8)
else:
    print("Amaaazzinng! This round has a tie!")

print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

if player1_wins == 3 or player2_wins == 3:
    print_summary()
    if player1_wins == 3:
        print("Player 1 beat Player 2. Player 2 is a LOOSER! ")
    else:
        print("Player 2 beat Player 1. Player 1 is a LOOSER! ")
    exit()


 # Round 9
player1_round_9 = random.randint(1, 12)
player2_round_9 = random.randint(1, 12)
rounds.append(round_counter)
dice.append('d12')
player1_rolls.append(player1_round_9)
player2_rolls.append(player2_round_9)
round_counter += 1

print("Player 1 rolled: ", player1_round_9)
print("Player 2 rolled: ", player2_round_9)

if player1_round_9 > player2_round_9:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round_9, " is greater than ", player2_round_9)
elif player2_round_9 > player1_round_9:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_round_9, " is greater than ", player1_round_9)
else:
    print("Amaaazzinng! This round has a tie!")

print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

if player1_wins == 3 or player2_wins == 3:
    print_summary()
    if player1_wins == 3:
        print("Player 1 beat Player 2. Player 2 is a LOOSER! ")
    else:
        print("Player 2 beat Player 1. Player 1 is a LOOSER! ")
    exit()


 # Round 10
player1_round_10 = random.randint(1, 12)
player2_round_10 = random.randint(1, 12)
rounds.append(round_counter)
dice.append('d12')
player1_rolls.append(player1_round_10)
player2_rolls.append(player2_round_10)
round_counter += 1

print("Player 1 rolled: ", player1_round_10)
print("Player 2 rolled: ", player2_round_10)

if player1_round_10 > player2_round_10:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round_10, " is greater than ", player2_round_10)
elif player2_round_10 > player1_round_10:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_round_10, " is greater than ", player1_round_10)
else:
    print("Amaaazzinng! This round has a tie!")

print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

if player1_wins == 3 or player2_wins == 3:
    print_summary()
    if player1_wins == 3:
        print("Player 1 beat Player 2. Player 2 is a LOOSER! ")
    else:
        print("Player 2 beat Player 1. Player 1 is a LOOSER! ")
    exit()

    