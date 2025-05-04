import os
from PIL import Image
import numpy as np

def color_to_brightness(pixel: np.ndarray):

    brightness = np.mean(pixel, dtype=int)
    return brightness

imgs = "./ascii_generator/imgs"
img = "ascii-pineapple.jpg"
ascii_str = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

try:
    image = Image.open(os.path.join(imgs, img))
    #print("Successfully loaded image!")
    width, height = image.size
    image = image.resize((128, 64))
    #print(f"Image size: {width} x {height}")
except FileNotFoundError:
    print(f"Image {img} not found in {imgs}. Please check the path.")
    exit(1)

img_array = np.array(image)
brightness_matrix = np.apply_along_axis(color_to_brightness, axis=2, arr=img_array)
norm_brightness = brightness_matrix / brightness_matrix.max()
indices = (norm_brightness * (len(ascii_str) - 1)).astype(int)
ascii_arr = np.array([[ascii_str[x] for x in row] for row in indices])
ascii_image = "\n".join("".join(row) for row in ascii_arr)

print(ascii_image)