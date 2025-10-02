# Battle of Dices is going to be an amazing 2 player game, 
# where two players face each other using only their sheer luck! 
# 
# The rules are:
# 
# Each player throws one D6.
# The player with the highest roll wins the round.  
# The first player to win 3 times is the winner.
#
# Our main task today is to implement the code necessary to bring this
# amazing game alive!

import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
player1_roll = random.randint(1, 6)
player2_roll = random.randint(1, 6)
# Round 1
input("\nPress ENTER to roll the dice...")

print("Player 1 rolled: ", player1_roll)
print("Player 2 rolled: ", player2_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

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

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 beat Player 2. Player 2 is a LOOSER! ")
elif player2_wins == 3:
    print("Player 2 beat Player 1. Player 1 is a LOOSER! ")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")

# Since none of them would have won after 1 round, we could copy this code several times
# until we have enough times to make sure someone wins.


