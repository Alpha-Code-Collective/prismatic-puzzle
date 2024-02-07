import pygame
import pygame.freetype
import pygame.mixer
from sys import exit
import random
import os

# The .static is for Windows users
from static import COLORS, CLUES, rounds_correct_positions, default_positions
from solution_logic import check_cubes_position


pygame.init()
screen_width, screen_height = 1200, 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Chroma Cube')
clock = pygame.time.Clock()

player_start_time = 0
elapsed_time = 0

# GUI settings
title_font = pygame.freetype.SysFont("Arial", 36)
button_font = pygame.freetype.SysFont("Arial", 24)
clue_font = pygame.freetype.SysFont("Arial", 20)
button_color = (0, 150, 0)
#Background Image
background_images = [
    pygame.image.load('prismatic_puzzle/assets/background1.jpg').convert_alpha(),
    pygame.image.load('prismatic_puzzle/assets/background2.jpg').convert_alpha(),
    pygame.image.load('prismatic_puzzle/assets/background3.jpg').convert_alpha(),
    pygame.image.load('prismatic_puzzle/assets/background4.jpg').convert_alpha(),
    pygame.image.load('prismatic_puzzle/assets/background5.jpg').convert_alpha(),
    pygame.image.load('prismatic_puzzle/assets/background6.jpg').convert_alpha(),
    pygame.image.load('prismatic_puzzle/assets/background7.jpg').convert_alpha(),
    pygame.image.load('prismatic_puzzle/assets/background8.jpg').convert_alpha(),
    pygame.image.load('prismatic_puzzle/assets/background9.jpg').convert_alpha(),
    pygame.image.load('prismatic_puzzle/assets/background10.jpg').convert_alpha(),

]

# Button Settings

button_width = 150
button_x = (screen_width - button_width) // 2
start_button_y = 50  # Y position for the "Start" button
check_button_y = 125  # Updated for clarity, providing more space between buttons
next_round_button_y = 185  # Updated for clarity
rules_button_y = 25
# Buttons
start_button_rect = pygame.Rect(
    button_x, start_button_y, button_width, 50)  # "Start" button
check_button_rect = pygame.Rect(
    button_x, check_button_y, button_width, 50)  # "Submit" button
next_round_button_rect = pygame.Rect(
    button_x, next_round_button_y, button_width, 50)  # "Next Round" button
rules_button_rect = pygame.Rect(button_x, rules_button_y, button_width, 50)
undo_button_rect = pygame.Rect(button_x + 300, 250, 100, 50)
reset_button_rect = pygame.Rect(button_x + 300, 350, 100, 50)
quit_button_rect = pygame.Rect(500, 600, 200, 50)
buttons = [start_button_rect, quit_button_rect]  
# Grid settings
cell_size = 100
grid_cols, grid_rows = 4, 3
total_grid_width = grid_cols * cell_size
total_grid_height = grid_rows * cell_size
grid_origin_x = (screen_width - total_grid_width) // 2
grid_origin_y = 250
grid_origin = (grid_origin_x, grid_origin_y)
grid_positions = [(x, y) for x in range(grid_cols) for y in range(grid_rows)]

# Container settings
container_height = 100  # Adjust height as needed
container_y = screen.get_height() - container_height  # Position it at the bottom
container_color = (172, 176, 174)  # A grey color, adjust as needed

# Overlay menus
menu_visible = True  # Make the menu visible initially or upon certain conditions
show_rules = False
show_validate = False
cubes = []
selected_cube = None
start_game = False
positions_correct = False  # Flag to indicate if the cube positions are correct
current_round = 0
message = ""

# Adjust position and size as needed
start_game_button_rect = pygame.Rect(500, 500, 200, 50)

move_history = []
# ----------------------------Undo functions--------------------

def record_move(cube, old_rect, old_grid_pos):
    move = {
        'cube': cube,
        'old_rect': pygame.Rect(old_rect),  # Deep copy of the rect
        # Assuming this is a simple value or tuple, not a mutable object
        'old_grid_pos': old_grid_pos
    }
    move_history.append(move)


def undo_last_move():
    if move_history:
        last_move = move_history.pop()
        cube = last_move['cube']
        cube['rect'] = pygame.Rect(
            last_move['old_rect'])  # Re-apply the old rect
        # Re-apply the old grid position
        cube['grid_pos'] = last_move['old_grid_pos']
        cube['rect'] = pygame.Rect(last_move['old_rect'])  # Re-apply the old rect
        cube['grid_pos'] = last_move['old_grid_pos']  # Re-apply the old grid position
#-----------------------------Undo functions END------------------------

#-------------------------------Draw functions-------------------------------------

def play_music(music_file, volume=0.2, loops=-1):
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.set_volume(volume)

    pygame.mixer.music.play(loops=loops)

# Call the function with the music file path and loop indefinitely
play_music("prismatic_puzzle/assets/Restless_Bones.mp3", volume=0.2, loops=-1)

# Add this line to keep the program running and music playing
# pygame.event.wait()

def draw_menu(surface, mouse_pos):
    if not menu_visible:
        return
    
    overlay = pygame.Surface((1200, 1000), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    surface.blit(overlay, (0, 0))
    
    # Load and draw the logo
    logo_path = os.path.join('prismatic_puzzle/assets', 'logo.png')  # Adjust the path as necessary
    logo_image = pygame.image.load(logo_path)
    new_width = 500
    new_height = 500
    logo_image = pygame.transform.scale(logo_image, (new_width, new_height))
    logo_rect = logo_image.get_rect()
    logo_rect.center = (600, 400)  # Adjust the position as necessary
    
    # Assuming you have your buttons defined somewhere above this function
    buttons = [start_game_button_rect, quit_button_rect]

    # Calculate the boundary of the logo and buttons
    min_x = min(logo_rect.left, min(button.left for button in buttons))
    max_x = max(logo_rect.right, max(button.right for button in buttons))
    min_y = min(logo_rect.top, min(button.top for button in buttons))
    max_y = max(logo_rect.bottom, max(button.bottom for button in buttons))


    # Add some padding around the elements
    padding = 20
    menu_rect = pygame.Rect(min_x - padding, min_y - padding, max_x - min_x + 2*padding, max_y - min_y + 2*padding)
    
    # Draw the menu rectangle outline
    pygame.draw.rect(surface, (200, 200, 200), menu_rect, 3)
    
    # Draw the logo
    surface.blit(logo_image, logo_rect)
  
    # Draw buttons with dynamic background based on mouse hover
    for button_rect, text in [(start_game_button_rect, "Start Game"), (quit_button_rect, "Quit")]:
        color = (0, 255, 0) if button_rect.collidepoint(mouse_pos) else (255, 255, 255)
        pygame.draw.rect(surface, color, button_rect)  # Fill background on hover
        text_surf, text_rect = button_font.render(text, (0, 0, 0))
        text_rect.center = button_rect.center
        surface.blit(text_surf, text_rect)


def draw_rules_overlay(surface):
    if show_rules:
        # Draw a semi-transparent background
        overlay = pygame.Surface((1200, 1000), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        surface.blit(overlay, (0, 0))

        # Draw the rules box
        rules_rect = pygame.Rect(300, 200, 600, 600)
        pygame.draw.rect(surface, (200, 200, 200), rules_rect)

        # Add your rules content and formatting here
        rules_text = [
            "Rules:",
            "- Arrange cubes on the grid to match the correct positions.",
            "- Clues are provided below the grid. Use logic to find",
            "  the correct position for each piece.",
            "- Click 'Submit' to check your solution.",
            "- Click 'Next Round' to proceed to the next challenge.",
            "- Complete all rounds to win the game.",
            # Add more rules or instructions here
        ]

        y_offset = 350
        for line in rules_text:
            clue_font.render_to(surface, (350, y_offset), line, (0, 0, 0))
            y_offset += 30

def draw_validation_overlay(surface, message):
    if show_validate:
        # Draw a semi-transparent background
        overlay = pygame.Surface((1200, 1000), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        surface.blit(overlay, (0, 0))

        # Draw the validation message box
        message_rect = pygame.Rect(250, 400, 700, 200)
        pygame.draw.rect(surface, (200, 200, 200), message_rect)

        if current_round == 10 and message == "Correct! Click 'Next Round' to continue.":
            title_font.render_to(surface, (280, 540), f"Congratulations. You beat the game!", (117, 165, 35))
            title_font.render_to(surface, (280, 540), f"You solved the round in {str(elapsed_time)} seconds", (117, 165, 35))
        elif message == "Correct! Click 'Next Round' to continue.":
            title_font.render_to(surface, (300, 490), message, (0, 0, 0))
            title_font.render_to(surface, (280, 540), f"You solved the round in {str(elapsed_time)} seconds", (117, 165, 35))
        else:
            title_font.render_to(surface, (300, 490), message, (0, 0, 0))

def draw_title(screen):
    # Round title
    title_surf, title_rect = title_font.render(
        f"Round {current_round + 1}", (0, 255, 0))
    title_rect.center = (600, 210)  # Adjust as needed
    screen.blit(title_surf, title_rect)

def draw_container(surface):
    container_rect = pygame.Rect(
        0, container_y, screen.get_width(), container_height)
    pygame.draw.rect(surface, container_color, container_rect)

def draw_cubes(surface):
    cubes_to_draw = []

    for cube in cubes:
        if cube is not selected_cube:
            cubes_to_draw.append(cube)

    for cube in cubes_to_draw:
        pygame.draw.rect(surface, cube['color'], cube['rect'])
        text_surf, text_rect = clue_font.render(cube['color_name'], (0, 0, 0))
        text_rect.center = cube['rect'].center
        surface.blit(text_surf, text_rect)

    if selected_cube:
        pygame.draw.rect(
            surface, selected_cube['color'], selected_cube['rect'])
        text_surf, text_rect = clue_font.render(
            selected_cube['color_name'], (0, 0, 0))
        text_rect.center = selected_cube['rect'].center
        surface.blit(text_surf, text_rect)

def draw_grid(surface):
    for row in range(grid_rows):
        for col in range(grid_cols):
            rect = pygame.Rect(
                grid_origin[0] + col * cell_size, grid_origin[1] + row * cell_size, cell_size, cell_size)
            pygame.draw.rect(surface, (255, 255, 255), rect, 3)

def draw_buttons(surface):
    def draw_button(rect, text, is_active):
        # Draw the button rectangle
        pygame.draw.rect(surface, button_color, rect, 0, 5)

        # Render the text to a new Surface
        text_surf = button_font.render(
            text, fgcolor=(255, 255, 255), size=24)[0]

        # Calculate text position for centering
        text_rect = text_surf.get_rect(center=rect.center)

        # If the button is active and mouse is hovered, simulate hover effect
        if is_active and rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(surface, (0, 180, 0), rect, 0, 5)

        surface.blit(text_surf, text_rect)

    if start_game and not positions_correct:
        draw_button(reset_button_rect, "Reset", True)
        draw_button(undo_button_rect, "Undo", True)
        draw_button(check_button_rect, "Submit", True)
    # Draw "Next Round" button
    if positions_correct:
        global cubes
        cubes = []
        draw_button(next_round_button_rect, "Next Round", True)

    pygame.draw.rect(surface, button_color, rules_button_rect, 0, 5)
    rules_surf, rules_rect = button_font.render("Rules", (255, 255, 255))
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
        clue_font.render_to(surface, (x_position, y_offset),
                            clue, (255, 255, 255))
        y_offset += 30  # Increment y_offset for the next clue

def draw_message(surface, message):
    if message:
        clue_font.render_to(surface, (400, 600), message, (0, 255, 0))
# -------------------------------Draw functions END-------------------------------------
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
        cube_rect = pygame.Rect(grid_origin[0] + grid_pos[0] * cell_size,
                                grid_origin[1] + grid_pos[1] * cell_size, cell_size, cell_size)
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
            cube_rect = pygame.Rect(
                x_offset, off_grid_start_y, cell_size, cell_size)
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
        cube['rect'].topleft = (
            grid_origin[0] + grid_x * cell_size, grid_origin[1] + grid_y * cell_size)
        cube['grid_pos'] = (grid_x, grid_y)
    else:
        # The cube is outside the grid boundaries, snap it back to the tray
        snap_cube_to_tray(cube)

def snap_cube_to_tray(cube):
    tray_start_x = 50  # Starting x-coordinate for cubes in the tray
    # Center cubes vertically in the tray
    tray_y = container_y + (container_height - cell_size) // 2
    cube_spacing = 10  # Spacing between cubes

    # Filter the list of cubes to only those not on the grid (i.e., in the tray)
    tray_cubes = [c for c in cubes if c['grid_pos']
                  is None and 'movable' in c and c['movable']]

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

# --------------------------Testing functions ---------------------------------------

def skip_to_next_level():
    global current_round, start_game, positions_correct, cubes, message
    if current_round < len(rounds_correct_positions) - 1:
        current_round += 1  # Move to the next round
    else:
        # Notify the player if they're already at the last level
        message = "You've reached the final level!"
        return  # Exit the function to avoid resetting the game state

    # Reset game state for the new level
    start_game = True
    positions_correct = False
    cubes = []  # Clear the cubes list to start fresh for the new level
    place_initial_cubes()  # Place initial cubes for the new level
    message = ""  # Clear any previous messages


def go_to_previous_level():
    global current_round, start_game, positions_correct, cubes, message
    if current_round > 0:
        current_round -= 1  # Move to the previous round
    else:
        # Notify the player if they're already at the first level
        message = "This is the first level!"
        return  # Exit the function to avoid any further actions

    # Reset game state for the previous level
    start_game = True
    positions_correct = False
    cubes = []  # Clear the cubes list to start fresh for the previous level
    place_initial_cubes()  # Place initial cubes for the previous level
    message = ""  # Clear any previous messages

    # Optionally, if you want to hide the menu when going back to the previous level
    # menu_visible = False
# --------------------------Testing functions END-------------------------------
def check_time():
    global positions_correct, message, elapsed_time, player_start_time
    correct_count = sum(cube['grid_pos'] == cube['correct_pos'] for cube in cubes)
    total_cubes = len(cubes)
    if message == f"Correct! Click 'Next Round' to continue.":
        elapsed_time = (pygame.time.get_ticks() - player_start_time) / 1000  # Convert to seconds
    else:
        positions_correct = False
        message = f"You got {correct_count} out of {total_cubes} correct. Try again."  

def handle_game_logic(event):
    global start_game, current_round, positions_correct, player_start_time, cubes, move_history, message, elapsed_time
    if check_button_rect.collidepoint(event.pos) and start_game and not positions_correct:
        positions_correct, message = check_cubes_position(cubes)
        check_cubes_position(cubes)
        check_time()
    
    elif reset_button_rect.collidepoint(event.pos):
        cubes = []
        move_history = []
        place_initial_cubes()
    elif next_round_button_rect.collidepoint(event.pos) and positions_correct:
        if current_round < len(rounds_correct_positions) - 1:
            current_round += 1
            player_start_time = None
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
            if undo_button_rect.collidepoint(event.pos):
                undo_last_move()
                continue
            if start_game_button_rect.collidepoint(event.pos):
                menu_visible = False  # Hide the menu only if "Start Game" is clicked
                start_game = True
                # No need for 'continue' as we want to process other events if needed
            handle_game_logic(event)

            if not selected_cube:  # Only select a new cube if we aren't already dragging one
                selected_cube = get_clicked_cube(event.pos)
                if selected_cube:  # If a cube is selected, remove it from its grid position for free dragging
                    record_move(
                        selected_cube, selected_cube['rect'].copy(), selected_cube['grid_pos'])
                    selected_cube['grid_pos'] = None

            # Handle button clicks separately from cube selection
            handle_game_logic(event)

            # Check if the "Rules" button is clicked
            if rules_button_rect.collidepoint(event.pos):
                show_rules = not show_rules  # Toggle rules visibility

            elif show_rules and not rules_button_rect.collidepoint(event.pos):
                # If the rules are shown and the click is outside the rules overlay, hide the rules
                show_rules = False

            # Check if the "Submit" button is clicked
            if check_button_rect.collidepoint(event.pos):
                show_validate = not show_validate  # Toggle rules visibility

            elif show_validate and not check_button_rect.collidepoint(event.pos):
                show_validate = False

        elif event.type == pygame.MOUSEBUTTONUP:
            if selected_cube:
                snap_cube_to_grid(selected_cube)
                selected_cube = None  # Deselect cube after dropping it

        elif event.type == pygame.MOUSEMOTION:
            if selected_cube:  # Move the selected cube with mouse
                selected_cube['rect'].center = event.pos

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:  # 'N' key for 'Next Level'
                skip_to_next_level()
            elif event.key == pygame.K_b:  # 'B' key for 'Previous Level'
                go_to_previous_level()

    screen.fill((0, 0, 0))
    if 0 <= current_round < len(background_images):
        current_background = background_images[current_round - 1]
        image_width, image_height = current_background.get_size()
        x_position = (screen_width - image_width) // 2
        y_position = (screen_height - image_height) // 2
        current_background.set_alpha(100)
        screen.blit(current_background, (x_position, y_position))
   
    draw_grid(screen)
    draw_title(screen)
    draw_container(screen)
    draw_buttons(screen)
    draw_clues(screen, CLUES)
    
    if start_game:
        draw_cubes(screen)
    if show_rules:
        draw_rules_overlay(screen)
    if show_validate:
        draw_validation_overlay(screen, message)
    draw_menu(screen, mouse_pos)
    pygame.display.update()
    clock.tick(60)
