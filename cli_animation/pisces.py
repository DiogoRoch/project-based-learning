import time
from scripts import move_shape, clear_screen, get_screen, draw_square, display_pixels, update_location


# Initialize the parameters
height, width = 40, 90
location_coord = [6, 3]
direction_vector = [1, 1]
size = 2

# Start the animation loop
while True:
    clear_screen()
    screen = get_screen(height, width)
    move_shape(draw_square, screen, location_coord, direction_vector, size, height, width)
    location_coord, direction_vector = update_location(location_coord, direction_vector, size, height, width)
    display_pixels(screen)
    time.sleep(0.3)