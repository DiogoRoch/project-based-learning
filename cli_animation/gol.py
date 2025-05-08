# Conway's Game of Life using my ascii cli animation scripts

import time
from scripts import clear_screen, get_screen, display_pixels, display_pixels_inverted, get_neighbors, draw_square, update_location
import random

def evaluate_conway_one(screen, location_coord):
    """Evaluates the next state of the cell at location_coord based on Conway's rules."""

    x, y = location_coord
    cell_state = screen[y][x]
    neighbors = get_neighbors(screen, location_coord)

    n_neighbors = sum(neighbors)
    # RULE 1: Living cells die if they have fewer than 2 neighbors (underpopulation)
    if cell_state == 1 and n_neighbors < 2:
        return 0
    
    # RULE 2: Living cells die if they have more than 3 neighbors (overpopulation)
    if cell_state == 1 and n_neighbors > 3:
        return 0

    # RULE 3: Dead cells that have 3 neighbors become alive (reproduction)
    if cell_state == 0 and n_neighbors == 3:
        return 1

    # RULE 4: Otherwise, the cell stays in its current state
    return cell_state


def evaluate_conway(screen):
    """
    Evaluates the next state of the entire screen based on Conway's rules.
    """
    rows, cols = len(screen), len(screen[0])
    new_screen = [[0 for _ in range(cols)] for _ in range(rows)]
    for y in range(rows):
        for x in range(cols):
            new_screen[y][x] = evaluate_conway_one(screen, (x, y))
    
    return new_screen


# Initialize the parameters
height, width = 60, 180
location_coord = [6, 3]
direction_vector = [1, 1]
size = 2

# Initialize the screen (randomly 1 or 0)
screen = [[random.randint(0, 1) for _ in range(width)] for _ in range(height)]
while True:
    clear_screen()
    display_pixels_inverted(screen)
    screen = evaluate_conway(screen)
    time.sleep(0.3)