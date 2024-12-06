
from PIL import Image

image_path = (r'mountain.jpg')  # Replace with your actual image path
img = Image.open(image_path)



rotated_img = img.rotate(45)  # Rotate by 45 degrees
rotated_img.save(r'C:\Users\Admin\Desktop\S Python\PIL\rotated_image.jpg')
