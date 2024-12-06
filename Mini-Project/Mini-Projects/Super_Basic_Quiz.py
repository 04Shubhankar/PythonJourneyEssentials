# Initialize global variables
global score
still_guessing = True

# Set initial attempt count to 0
attempt = 0

# Begin the guessing loop
while still_guessing and attempt < 3:
    # Get the user's guess and convert it to lowercase for case-insensitive comparison
    guess = input("Guess the animal: ").lower()

    # Check if the guess is correct
    if guess == answer.lower():
        # If correct, print a success message, increment the score, and end the guessing loop
        print("Correct Answer")
        score += 1
        still_guessing = False
    else:
        # If incorrect and there are remaining attempts, prompt the user to try again
        if attempt < 2:
            guess = input("Sorry, Wrong Answer. Try again: ").lower()
        # Increment the attempt count
        attempt += 1

# If the maximum attempts have been reached without a correct guess, reveal the correct answer
if attempt == 3:
    print("The correct answer is:", answer)

# Print the final score
print("Your score is:", score)
