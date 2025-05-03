import os
from PIL import Image

imgs = "./ascii_generator/imgs"
img = "ascii-pineapple.jpg"

try:
    image = Image.open(os.path.join(imgs, img))
    print("Successfully loaded image!")
    height, width = image.size
    print(f"Image size: {height}x{width}")
except FileNotFoundError:
    print(f"Image {img} not found in {imgs}. Please check the path.")
    exit(1)
