import pygame
import pygame.freetype
from sys import exit
import random
# Assuming the static.py file is correctly placed relative to this script.
from .static import COLORS, CLUES, rounds_correct_positions

pygame.init()
screen = pygame.display.set_mode((1200, 1000))
pygame.display.set_caption('Chroma Cube')
clock = pygame.time.Clock()

# GUI settings
button_font = pygame.freetype.SysFont("Arial", 24)
clue_font = pygame.freetype.SysFont("Arial", 20)
button_color = (0, 150, 0)
start_button_rect = pygame.Rect(425, 50, 150, 50)  # "Start" button
check_button_rect = pygame.Rect(425, 150, 150, 50)  # "Submit" button
next_round_button_rect = pygame.Rect(425, 250, 150, 50)  # "Next Round" button, shown after correct submission

# Grid settings
grid_origin = (450, 250)
cell_size = 100
grid_cols, grid_rows = 3, 4
grid_positions = [(x, y) for x in range(grid_cols) for y in range(grid_rows)]

cubes = []
selected_cube = None
start_game = False
positions_correct = False  # Flag to indicate if the cube positions are correct
current_round = 0
message = ""

def draw_cubes(surface):
    for cube in cubes:
        pygame.draw.rect(surface, cube['color'], cube['rect'])
        # Render the color name text within the cube
        text_surf, text_rect = clue_font.render(cube['color_name'], (0, 0, 0))
        text_rect.center = cube['rect'].center
        surface.blit(text_surf, text_rect)

def draw_grid(surface):
    for row in range(grid_rows):
        for col in range(grid_cols):
            rect = pygame.Rect(grid_origin[0] + col * cell_size, grid_origin[1] + row * cell_size, cell_size, cell_size)
            pygame.draw.rect(surface, (255, 255, 255), rect, 3)

def draw_buttons(surface):
    # Draw "Start" button only if the game hasn't started
    if not start_game:
        button_font.render_to(surface, (start_button_rect.x + 20, start_button_rect.y + 15), "Start", (255, 255, 255))
        pygame.draw.rect(surface, button_color, start_button_rect, 0, 5)
    # Draw "Submit" button if the game has started
    if start_game and not positions_correct:
        button_font.render_to(surface, (check_button_rect.x + 20, check_button_rect.y + 15), "Submit", (255, 255, 255))
        pygame.draw.rect(surface, button_color, check_button_rect, 0, 5)
    # Draw "Next Round" button if positions are correct
    if positions_correct:
        button_font.render_to(surface, (next_round_button_rect.x + 20, next_round_button_rect.y + 15), "Next Round", (255, 255, 255))
        pygame.draw.rect(surface, button_color, next_round_button_rect, 0, 5)

def draw_clues(surface, clues):
    y_offset = 600
    for clue in clues[current_round]:
        clue_font.render_to(surface, (50, y_offset), clue, (255, 255, 255))
        y_offset += 30

def place_initial_cubes():
    global cubes
    cubes = []

    # Adjust starting Y position for the cubes placed off the grid to ensure visibility
    off_grid_start_y = screen.get_height() - cell_size - 10  # Place cubes at the bottom, with some padding

    # Adjust spacing between cubes to fit them all within the screen width
    total_cubes = len(COLORS)
    available_space = screen.get_width() - 100  # Assuming 50px padding on each side
    cube_spacing = available_space // total_cubes  # Divide available space by the number of cubes

    x_offset = 50  # Start 50px from the left edge of the screen

    for color_name, correct_pos in rounds_correct_positions[current_round].items():
        color_rgb = COLORS[color_name]
        cube_rect = pygame.Rect(x_offset, off_grid_start_y, cell_size, cell_size)
        cubes.append({
            'color': color_rgb, 
            'rect': cube_rect, 
            'grid_pos': None,  # Indicates the cube is not on the grid
            'color_name': color_name, 
            'correct_pos': correct_pos  # Keep the correct position for later checking
        })
        x_offset += cube_spacing  # Increment x_offset for the next cube placement

    # Adjust cube spacing if too narrow
    if cube_spacing < cell_size:
        print("Warning: Cube spacing too narrow, consider reducing number of cubes or screen layout adjustments.")



def check_cubes_position():
    global positions_correct, message
    if all(cube['grid_pos'] == cube['correct_pos'] for cube in cubes):
        message = "Correct! Click 'Next Round' to continue."
        positions_correct = True
    else:
        message = "Not quite right, try again."
        positions_correct = False

def draw_message(surface, message):
    if message:
        clue_font.render_to(surface, (300, 900), message, (0, 255, 0))

def get_clicked_cube(pos):
    for cube in cubes:
        if cube['rect'].collidepoint(pos):
            return cube
    return None

def snap_cube_to_grid(cube):
    # Snap to grid if dropped within grid area, else snap back to original off-grid position
    if grid_origin[0] <= cube['rect'].centerx <= grid_origin[0] + cell_size * grid_cols and \
       grid_origin[1] <= cube['rect'].centery <= grid_origin[1] + cell_size * grid_rows:
        grid_x = (cube['rect'].centerx - grid_origin[0]) // cell_size
        grid_y = (cube['rect'].centery - grid_origin[1]) // cell_size
        snapped_x = grid_origin[0] + grid_x * cell_size
        snapped_y = grid_origin[1] + grid_y * cell_size
        cube['rect'].topleft = (snapped_x, snapped_y)
        cube['grid_pos'] = (grid_x, grid_y)
    else:
        pass
        # Logic to snap back to original off-grid position could be added here

def handle_game_logic(event):
    global start_game, current_round, positions_correct
    if start_button_rect.collidepoint(event.pos) and not start_game:
        start_game = True
        positions_correct = False
        place_initial_cubes()
    elif check_button_rect.collidepoint(event.pos) and start_game and not positions_correct:
        check_cubes_position()
    elif next_round_button_rect.collidepoint(event.pos) and positions_correct:
        if current_round < len(rounds_correct_positions) - 1:
            current_round += 1
            start_game = True
            positions_correct = False
            place_initial_cubes()
        else:
            message = "Game Over! You've completed all rounds!"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not selected_cube:  # Only select a new cube if we aren't already dragging one
                selected_cube = get_clicked_cube(event.pos)
                if selected_cube:  # If a cube is selected, remove it from its grid position for free dragging
                    selected_cube['grid_pos'] = None

            # Handle button clicks separately from cube selection
            handle_game_logic(event)

        elif event.type == pygame.MOUSEBUTTONUP:
            if selected_cube:
                snap_cube_to_grid(selected_cube)  # Snap cube to grid or leave it off-grid as per logic in this function
                selected_cube = None  # Deselect cube after dropping it

        elif event.type == pygame.MOUSEMOTION:
            if selected_cube:  # Move the selected cube with mouse
                selected_cube['rect'].center = event.pos

    screen.fill((0, 0, 0))
    draw_grid(screen)
    draw_buttons(screen)
    draw_clues(screen, CLUES)
    if start_game:
        draw_cubes(screen)
    draw_message(screen, message)

    pygame.display.update()
    clock.tick(60)
