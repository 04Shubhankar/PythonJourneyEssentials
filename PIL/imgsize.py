
from PIL import Image

image_path = (r'mountain.jpg')  # Replace with your actual image path
img = Image.open(image_path)


width, height = img.size
print("Image size:", width, height)
