def program5():
    """
    Finds the total occurrences of a specific word in a text file.
    """

    cnt = 0  # Initialize a counter to keep track of word occurrences
    word_search = input("Enter word to search: ")  # Prompt the user to enter the word to search for

    with open("myfile.txt", "r") as f1:  # Open the file "merge.txt" in read mode ('r')
        for data in f1:  # Iterate through each line in the file
            words = data.split()  # Split the line into a list of words
            for word in words:  # Iterate through each word in the list
                if word == word_search:  # Check if the current word matches the search word
                    cnt += 1  # Increment the counter if a match is found

    print(word_search, "found", cnt, "times from the file")  # Print the number of occurrences

program5()  # Call the function to execute the code
