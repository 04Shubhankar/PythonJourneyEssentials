
from PIL import Image

image_path = (r'mountain.jpg')  # Replace with your actual image path
img = Image.open(image_path)

mode = img.mode
print("Image mode:", mode)

