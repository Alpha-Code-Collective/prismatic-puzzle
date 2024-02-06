import pygame
import pygame.freetype
import pygame.mixer
from sys import exit
import random


# from static import COLORS, CLUES, rounds_correct_positions, default_positions
# The .static is for Windows users
from static import COLORS, CLUES, rounds_correct_positions, default_positions

pygame.init()
screen_width, screen_height = 1200, 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Chroma Cube')
clock = pygame.time.Clock()

# GUI settings
title_font = pygame.freetype.SysFont("Arial", 36)
button_font = pygame.freetype.SysFont("Arial", 24)
clue_font = pygame.freetype.SysFont("Arial", 20)
button_color = (0, 150, 0)


button_width = 150
button_x = (screen_width - button_width) // 2
start_button_y = 50  # Y position for the "Start" button
check_button_y = 125  # Updated for clarity, providing more space between buttons
next_round_button_y = 200  # Updated for clarity
rules_button_y = 25

start_button_rect = pygame.Rect(button_x, start_button_y, button_width, 50)  # "Start" button
check_button_rect = pygame.Rect(button_x, check_button_y, button_width, 50)  # "Submit" button
next_round_button_rect = pygame.Rect(button_x, next_round_button_y, button_width, 50)  # "Next Round" button
rules_button_rect = pygame.Rect(button_x, rules_button_y, button_width, 50)  # Define the "Rules" button rectangle

# Grid settings
cell_size = 100
grid_cols, grid_rows = 4, 3

total_grid_width = grid_cols * cell_size
total_grid_height = grid_rows * cell_size

grid_origin_x = (screen_width - total_grid_width) // 2
grid_origin_y = 250
grid_origin = (grid_origin_x, grid_origin_y)

grid_positions = [(x, y) for x in range(grid_cols) for y in range(grid_rows)]

# Overlay menus
menu_visible = True  # Make the menu visible initially or upon certain conditions
show_rules = False
cubes = []
selected_cube = None
start_game = False
positions_correct = False  # Flag to indicate if the cube positions are correct
current_round = 0
message = ""
start_game_button_rect = pygame.Rect(500, 500, 200, 50)  # Adjust position and size as needed


def play_music(music_file, volume=0.2, loops=-1):
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.set_volume(volume)

    pygame.mixer.music.play(loops=loops)

# Call the function with the music file path and loop indefinitely
play_music("prismatic_puzzle/Restless_Bones.mp3", volume=0.2, loops=-1)

# Add this line to keep the program running and music playing
# pygame.event.wait()

def draw_menu(surface, mouse_pos):
    if not menu_visible:
        return  # Skip drawing the menu if it's not supposed to be visible
    
    # Dim background
    overlay = pygame.Surface((1200, 1000), pygame.SRCALPHA)  # Adjust to your screen size
    overlay.fill((0, 0, 0, 180))  # Semi-transparent black overlay
    surface.blit(overlay, (0, 0))
    
    # Draw the menu box
    menu_rect = pygame.Rect(400, 300, 400, 400)  # Adjust as needed
    pygame.draw.rect(surface, (200, 200, 200), menu_rect)  # Light grey menu background

    # Game title
    title_surf, title_rect = title_font.render("Prismatic Puzzle", (0, 0, 0))
    title_rect.center = (600, 350)  # Adjust as needed
    surface.blit(title_surf, title_rect)
    
    # The rest of your menu drawing code...    # Determine button color based on mouse hover
    button_color = (255, 0, 0) if start_game_button_rect.collidepoint(mouse_pos) else (0, 255, 0)    # Draw the "Start Game" button with dynamic color
    pygame.draw.rect(surface, button_color, start_game_button_rect)
    start_surf, start_rect =button_font.render("Start Game", (0, 0, 0))
    start_rect.center = start_game_button_rect.center
    surface.blit(start_surf, start_rect)

def draw_rules_overlay(surface):
    if show_rules:
        # Draw a semi-transparent background
        overlay = pygame.Surface((1200, 1000), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        surface.blit(overlay, (0, 0))

        # Draw the rules box
        rules_rect = pygame.Rect(400, 300, 400, 400)
        pygame.draw.rect(surface, (200, 200, 200), rules_rect)

        # Add your rules content and formatting here
        rules_text = [
            "Rules:",
            "- Arrange cubes on the grid to match the correct positions.",
            "- Click 'Submit' to check your solution.",
            "- Click 'Next Round' to proceed to the next challenge.",
            "- Complete all rounds to win the game.",
            # Add more rules or instructions here
        ]

        y_offset = 350
        for line in rules_text:
            clue_font.render_to(surface, (420, y_offset), line, (0, 0, 0))
            y_offset += 30

# Container settings
container_height = 100  # Adjust height as needed
container_y = screen.get_height() - container_height  # Position it at the bottom
container_color = (100, 100, 100)  # A grey color, adjust as needed

def draw_container(surface):
    container_rect = pygame.Rect(0, container_y, screen.get_width(), container_height)
    pygame.draw.rect(surface, container_color, container_rect)


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
    def draw_button(rect, text, is_active):
        # Draw the button rectangle
        pygame.draw.rect(surface, button_color, rect, 0, 5)
        
        # Render the text to a new Surface
        text_surf = button_font.render(text, fgcolor=(255, 255, 255), size=24)[0]

        # Calculate text position for centering
        text_rect = text_surf.get_rect(center=rect.center)

        # If the button is active and mouse is hovered, simulate hover effect
        if is_active and rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(surface, (0, 180, 0), rect, 0, 5) 
        
        surface.blit(text_surf, text_rect)

    if start_game and not positions_correct:
        draw_button(check_button_rect, "Submit", True)
    # Draw "Next Round" button
    if positions_correct:
        global cubes
        cubes = []
        draw_button(next_round_button_rect, "Next Round", True)

    pygame.draw.rect(surface, button_color, rules_button_rect)
    rules_surf, rules_rect = button_font.render("Rules", (0, 0, 0))
    rules_rect.center = rules_button_rect.center
    surface.blit(rules_surf, rules_rect)


def draw_clues(surface, clues):
    screen_width = 1200  # Assuming this is your screen width
    y_offset = 600  # Starting Y position for clues
    
    for clue in clues[current_round]:
        # Render the clue to an off-screen surface to get its size without displaying it
        clue_surface, clue_rect = clue_font.render(clue, (255, 255, 255))
        clue_width = clue_rect.width
        
        # Calculate the x position to center the clue
        x_position = (screen_width - clue_width) // 2
        
        # Now render the clue to the actual surface at the calculated position
        clue_font.render_to(surface, (x_position, y_offset), clue, (255, 255, 255))
        y_offset += 30  # Increment y_offset for the next clue


def place_initial_cubes():
    global cubes
    if current_round >= len(default_positions):
        print(f"Configuration for round {current_round} is missing.")
        return
    # Starting positions for cubes on the grid for the current round
    starting_positions = default_positions[current_round]

    # Place the specified cubes on their starting positions on the grid
    for color_name, grid_pos in starting_positions.items():
        color_rgb = COLORS[color_name]
        cube_rect = pygame.Rect(grid_origin[0] + grid_pos[0] * cell_size, grid_origin[1] + grid_pos[1] * cell_size, cell_size, cell_size)
        cubes.append({
        'color': color_rgb,
        'rect': cube_rect,
        'grid_pos': grid_pos,
        'color_name': color_name,
        'movable': False,  # Add this line to indicate the cube should not be moved
        'correct_pos': rounds_correct_positions[current_round][color_name]
    })

    # Adjust starting Y position for the cubes placed off the grid to ensure visibility
    off_grid_start_y = container_y + (container_height - cell_size) // 2

    # Place remaining cubes off the grid, excluding those already placed
    placed_colors = starting_positions.keys()
    x_offset = 50
    for color_name, correct_pos in rounds_correct_positions[current_round].items():
        if color_name not in placed_colors:
            color_rgb = COLORS[color_name]
            cube_rect = pygame.Rect(x_offset, off_grid_start_y, cell_size, cell_size)
            cubes.append({
                'color': color_rgb,
                'rect': cube_rect,
                'grid_pos': None,  # Indicates the cube is not on the grid
                'color_name': color_name,
                'movable': True,
                'correct_pos': correct_pos
            })
            x_offset += cell_size + 10  # Adjust spacing to ensure cubes don't overlap

    # Note: Adjust x_offset increment and off_grid_start_y as needed based on your UI layout and total number of cubes
def calculate_grid_position(center_pos):
    # Calculate grid position from pixel coordinates
    # center_pos is a tuple containing the x and y pixel coordinates of the cube's center
    x, y = center_pos

    # Calculate how many pixels the center is from the grid's origin
    delta_x, delta_y = x - grid_origin[0], y - grid_origin[1]

    # Check if the cube's center is within the bounds of the grid
    if 0 <= delta_x <= grid_cols * cell_size and 0 <= delta_y <= grid_rows * cell_size:
        # Calculate the cube's column and row on the grid
        grid_x = delta_x // cell_size
        grid_y = delta_y // cell_size
        return int(grid_x), int(grid_y)
    else:
        # Return None if the cube is not within the grid's bounds
        return None, None


def check_cubes_position():
    global positions_correct, message
    positions_correct = all(cube['grid_pos'] == cube['correct_pos'] for cube in cubes)
    message = "Correct! Click 'Next Round' to continue." if positions_correct else "Not quite right, try again."

def draw_message(surface, message):
    if message:
        clue_font.render_to(surface, (400, 600), message, (0, 255, 0))

def get_clicked_cube(pos):
    for cube in cubes:
        if cube['rect'].collidepoint(pos) and 'movable' in cube and cube['movable']:
            return cube
    return None

def snap_cube_to_grid(cube):
    grid_x, grid_y = calculate_grid_position(cube['rect'].center)

    if grid_x is not None and grid_y is not None:
        # Check if the grid position is already occupied
        for existing_cube in cubes:
            if existing_cube['grid_pos'] == (grid_x, grid_y) and existing_cube is not cube:
                # The position is occupied, snap the cube back to the tray
                snap_cube_to_tray(cube)
                return
        # The position is not occupied, update the cube's grid position and rect position
        cube['rect'].topleft = (grid_origin[0] + grid_x * cell_size, grid_origin[1] + grid_y * cell_size)
        cube['grid_pos'] = (grid_x, grid_y)
    else:
        # The cube is outside the grid boundaries, snap it back to the tray
        snap_cube_to_tray(cube)


def snap_cube_to_tray(cube):
    tray_start_x = 50  # Starting x-coordinate for cubes in the tray
    tray_y = container_y + (container_height - cell_size) // 2  # Center cubes vertically in the tray
    cube_spacing = 10  # Spacing between cubes

    # Filter the list of cubes to only those not on the grid (i.e., in the tray)
    tray_cubes = [c for c in cubes if c['grid_pos'] is None and 'movable' in c and c['movable']]

    # Find the index of this cube within the tray_cubes list
    try:
        index = tray_cubes.index(cube)
    except ValueError:
        # In case the cube is not yet in the tray_cubes list, append it
        tray_cubes.append(cube)
        index = len(tray_cubes) - 1

    # Calculate the x-coordinate based on the index and spacing
    # This ensures that each cube in the tray is placed next to the previous one without overlapping
    cube_x = tray_start_x + index * (cell_size + cube_spacing)

    # Update the cube's position to the calculated tray position
    cube['rect'].topleft = (cube_x, tray_y)


def handle_game_logic(event):
    global start_game, current_round, positions_correct
    if check_button_rect.collidepoint(event.pos) and start_game and not positions_correct:
        check_cubes_position()
    elif next_round_button_rect.collidepoint(event.pos) and positions_correct:
        if current_round < len(rounds_correct_positions) - 1:
            current_round += 1

            start_game = True
            positions_correct = False
            place_initial_cubes()
        else:
            message = "Game Over! You've completed all rounds!"

place_initial_cubes()

while True:
    mouse_pos = pygame.mouse.get_pos()  # Get current mouse position

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_game_button_rect.collidepoint(event.pos):
                menu_visible = False  # Hide the menu only if "Start Game" is clicked
                start_game = True

                # No need for 'continue' as we want to process other events if needed

            handle_game_logic(event)

            if not selected_cube:  # Only select a new cube if we aren't already dragging one
                selected_cube = get_clicked_cube(event.pos)
                if selected_cube:  # If a cube is selected, remove it from its grid position for free dragging
                    selected_cube['grid_pos'] = None

            # Handle button clicks separately from cube selection
            handle_game_logic(event)

            # Check if the "Rules" button is clicked
            if rules_button_rect.collidepoint(event.pos):
                show_rules = not show_rules  # Toggle rules visibility

            elif show_rules and not rules_button_rect.collidepoint(event.pos):
                # If the rules are shown and the click is outside the rules overlay, hide the rules
                show_rules = False         

        elif event.type == pygame.MOUSEBUTTONUP:
            if selected_cube:
                snap_cube_to_grid(selected_cube)  # Snap cube to grid or leave it off-grid as per logic in this function
                selected_cube = None  # Deselect cube after dropping it

        elif event.type == pygame.MOUSEMOTION:
            if selected_cube:  # Move the selected cube with mouse
                selected_cube['rect'].center = event.pos

  
    screen.fill((0, 0, 0))
    draw_grid(screen)
    draw_container(screen)
    draw_buttons(screen)
    draw_clues(screen, CLUES)
    
    if start_game:

        draw_cubes(screen)
    if show_rules:
        draw_rules_overlay(screen)
    draw_message(screen, message)
    draw_menu(screen, mouse_pos)

    pygame.display.update()
    clock.tick(60)
