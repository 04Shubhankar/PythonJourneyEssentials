from PIL import Image

def process_image(image_path):
    img = Image.open(image_path)

    print("Image mode:", img.mode)
    print("Image size:", img.size)
    print("Image format:", img.format)

    rotated_img = img.rotate(45)
    rotated_img.save(r'C:\path\to\save\rotated_' + image_path)

    resized_img = img.resize((200, 200))
    resized_img.save(r'C:\path\to\save\resized_' + image_path)

image_paths = [
    r'C:\path\to\image1.jpg',
    r'C:\path\to\image2.png',
    r'C:\path\to\image3.gif'
]

for image_path in image_paths:
    process_image(image_path)
