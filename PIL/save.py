
from PIL import Image

image_path = (r'mountain.jpg')  # Replace with your actual image path
img = Image.open(image_path)



new_image_path = r'C:\Users\Admin\Desktop\S Python\PIL\new_image.jpg'
img.save(new_image_path)
