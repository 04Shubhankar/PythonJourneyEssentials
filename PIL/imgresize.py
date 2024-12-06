
from PIL import Image

image_path = (r'mountain.jpg')  # Replace with your actual image path
img = Image.open(image_path)


resized_img = img.resize((200, 200))  # Resize to 200x200 pixels
resized_img.save(r'C:\Users\Admin\Desktop\S Python\PIL\resized_image.jpg')

