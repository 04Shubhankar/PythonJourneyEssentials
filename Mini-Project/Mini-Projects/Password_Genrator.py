import random

# Function to generate a password of length n
def generatePassword(n):
    # Defining the list of characters to choose from
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@#$%^&*()"

    # Initialize an empty password string
    password = ""

    # Generate random characters and append them to the password
    for i in range(n):
        password += random.choice(characters)

    # Return the generated password
    return password

# Driver code
if __name__ == "__main__":
    n = 12
    password = generatePassword(n)
    print("Generated password:", password)
