import pyscreenshot as ImageGrab

# Capture a specific region (top-left corner, width, height)
image = ImageGrab.grab(bbox=(100, 100, 500, 500))

# Display the screenshot (optional)
image.show()

# Save the screenshot
image.save("partial_screen.png")
