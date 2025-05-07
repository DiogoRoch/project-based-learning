import os


def clear_screen():
    """Clears the console to update the display."""
    os.system("cls" if os.name == "nt" else "clear")


def get_screen(height, width):
    """Creates a screen of the provided height and width."""
    screen = [[0] * width for _ in range(height)]
    return screen


def display_pixels(screen):
    """Updates the display each frame."""
    for row in screen:

        print("".join("#" if not pixel else " " for pixel in row))


def draw_square(screen, location_coord,  size):
    """Draws a square at a specific location vector."""
    x0, y0 = location_coord

    for y in range(y0, y0 + size):

        for x in range(x0, x0 + size):

            screen[y][x] = 1


def update_location(location_coord, direction_vector, size, height, width):
    """
    Updates the location coordinates and direction vector.
    """

    # First update the location coordinates
    #location_coord = [l + d for l, d in zip(location_coord, direction_vector)]

    # Set parameters for readability
    x, y = location_coord
    x_, y_ = direction_vector
    x_new, y_new = x + x_, y + y_

    # Check if the updated coordinates would be outside of the screen
    if (x_new < 0 or x_new > (width)) or ((x_new + size) < 0 or (x_new + size) > (width)):
        x_ *= -1
        x_new = x + x_
    
    if (y_new < 0 or y_new > (height)) or ((y_new + size) < 0 or (y_new + size) > (height)):
        y_ *= -1
        y_new = y + y_

    location_coord = [x_new, y_new]
    direction_vector = [x_, y_]

    return location_coord, direction_vector


def move_shape(draw_fn, screen, location_coord, direction_vector, size, height, width):
    """Draws the shape at the next location depending on the direction vector."""
    # Border logic here...
    # Make the shape bounce around the borders
    
    draw_fn(screen, location_coord, size)