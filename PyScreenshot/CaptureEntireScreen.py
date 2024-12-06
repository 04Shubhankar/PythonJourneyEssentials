import pyscreenshot as ImageGrab

# Capture the entire screen
image = ImageGrab.grab()

# Display the screenshot (optional)
image.show()

# Save the screenshot
image.save("full_screen.png")
# Not providing a entire path results in the image being saved in the working directory

