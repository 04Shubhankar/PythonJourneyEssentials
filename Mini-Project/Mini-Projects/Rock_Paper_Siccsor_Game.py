import random

# This line imports the random module, which is used to generate random choices.

player1 = input("Select Rock, Paper, or Scissor: ").lower()

# This line prompts the user to enter their choice (Rock, Paper, or Scissor) and converts it to lowercase for case-insensitive comparison.

player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()

# This line randomly selects one of the three choices (Rock, Paper, or Scissor) for Player 2 and also converts it to lowercase.

print("Player 2 selected:", player2)

# This line prints the choice made by Player 2.

if player1 == "rock" and player2 == "paper":
    print("Player 2 Won")

# This block checks if Player 1 chose Rock and Player 2 chose Paper. If this condition is true, it means Player 2 wins.

elif player1 == "paper" and player2 == "scissor":
    print("Player 2 Won")

# This block checks if Player 1 chose Paper and Player 2 chose Scissor. If this condition is true, it means Player 2 wins.

elif player1 == "scissor" and player2 == "rock":
    print("Player 2 Won")

# This block checks if Player 1 chose Scissor and Player 2 chose Rock. If this condition is true, it means Player 2 wins.

elif player1 == player2:
    print("Tie")

# This block checks if both players chose the same option. If this condition is true, it means it's a tie.

else:
    print("Player 1 Won")

# This block is the default case, which means none of the previous conditions were met. Therefore, Player 1 wins.
