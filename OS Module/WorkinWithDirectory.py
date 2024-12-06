import os

# Get the current working directory
current_dir = os.getcwd()
print("Current working directory:", current_dir)

# Create a new directory
new_dir = "new_folder"
os.mkdir(new_dir)
print("Created new directory:", new_dir)

# List contents of the new directory
contents = os.listdir(new_dir)
print("Contents of new directory:", contents)

# Rename the new directory
new_name = "renamed_folder"
os.rename(new_dir, new_name)
print("Renamed directory to:", new_name)

# Remove the renamed directory (assuming it's empty)
os.rmdir(new_name)
print("Removed directory:", new_name)
