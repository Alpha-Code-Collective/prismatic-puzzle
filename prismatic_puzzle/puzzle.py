import pygame
import pygame.freetype
import pygame.mixer
from pygame.locals import *
import sys
import os

# The .static is for Windows users
if sys.platform.startswith('win'):
    from .static import COLORS, CLUES, rounds_correct_positions, default_positions
    from .solution_logic import check_cubes_position
else:
    from static import COLORS, CLUES, rounds_correct_positions, default_positions
    from solution_logic import check_cubes_position

pygame.init()
screen_width, screen_height = 1325, 955
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Chroma Cube')
clock = pygame.time.Clock()

player_start_time = pygame.time.get_ticks()
elapsed_time = 0

# Music player
play_button = pygame.Rect(10, 10, 50, 50)  # Adjust position and size as needed
pause_button = pygame.Rect(70, 10, 50, 50)

play_font = pygame.font.Font(None, 30)  # Choose a suitable font
play_text = play_font.render("▶️", True, (255, 255, 255))
pause_text = play_font.render("⏸", True, (255, 255, 255))


# GUI settings
title_font = pygame.freetype.SysFont("Arial", 36)
button_font = pygame.freetype.SysFont("Arial", 24)
clue_font = pygame.freetype.SysFont("Arial", 24, bold= True)
rules_font = pygame.freetype.SysFont("Arial", 20, bold= True)
button_color = (70, 73, 242)

# Background Image
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
    pygame.image.load('prismatic_puzzle/assets/background11.jpg').convert_alpha(),
    pygame.image.load('prismatic_puzzle/assets/background12.jpg').convert_alpha(),
    pygame.image.load('prismatic_puzzle/assets/background13.jpg').convert_alpha(),
    pygame.image.load('prismatic_puzzle/assets/background14.jpg').convert_alpha(),
    pygame.image.load('prismatic_puzzle/assets/background15.jpg').convert_alpha(),

]

# Button Settings
button_width = 150
button_x = (screen_width - button_width) // 2
start_button_y = 50  # Y position for the "Start" button
check_button_y = 125  # Updated for clarity, providing more space between buttons
next_round_button_y = 185  # Updated for clarity
rules_button_y = 25
# Buttons


#---Round Buttons

start_button_rect = pygame.Rect(
    button_x, start_button_y, button_width, 50)  # "Start" button
check_button_rect = pygame.Rect(
    button_x, check_button_y, button_width, 50)  # "Submit" button
next_round_button_rect = pygame.Rect(
    button_x, next_round_button_y, button_width, 50)  # "Next Round" button
rules_button_rect = pygame.Rect(button_x, rules_button_y, button_width, 50)



border_rect = rules_button_rect.inflate(8,8)
#---Undo Buttons

undo_button_rect = pygame.Rect(button_x + 300, 250, 100, 50)
reset_button_rect = pygame.Rect(button_x + 300, 350, 100, 50)
# ---Music Buttons
music_button_rect = pygame.Rect(50, 30, 100, 50)
volume_up_button_rect = pygame.Rect(50, 100, 100, 50)
volume_down_button_rect = pygame.Rect(50, 170, 100, 50)
# ---Beginning Buttons
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
# -----------------------------Undo functions END------------------------


# ----------------------Play Music-----------------------------------------


# Music file path
music_file = "prismatic_puzzle/assets/Restless_Bones.mp3"

def play_music(music_file, volume=0.2, loops=-1):
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loops=loops)

music_playing = True  # Variable to track the music playing state
play_music(music_file)

def toggle_music():
    global music_playing
    if music_playing:
        pygame.mixer.music.pause()
        music_playing = False
    else:
        pygame.mixer.music.unpause()
        music_playing = True

def increase_volume():
    current_volume = pygame.mixer.music.get_volume()
    if current_volume < 1.0:
        new_volume = min(current_volume + 0.1, 1.0)  # Increase volume by 0.1 but limit to 1.0
        pygame.mixer.music.set_volume(new_volume)

def decrease_volume():
    current_volume = pygame.mixer.music.get_volume()
    if current_volume > 0.0:
        new_volume = max(current_volume - 0.1, 0.0)  # Decrease volume by 0.1 but limit to 0.0
        pygame.mixer.music.set_volume(new_volume)


# ----------------------END Play Music-----------------------------------------
# -------------------------------Draw functions-------------------------------------


def draw_menu(surface, mouse_pos):
    global screen_width, screen_height

    if not menu_visible:
        return

    # Load and scale the logo
    logo_path = os.path.join('prismatic_puzzle/assets', 'logo.png')
    logo_image = pygame.image.load(logo_path).convert_alpha()
    new_width, new_height = 600, 600  # Adjust as necessary
    logo_image = pygame.transform.scale(logo_image, (new_width, new_height))
    logo_rect = logo_image.get_rect()

    # Calculate the total height of the menu's content (logo + buttons + spacing)
    button_spacing = 20  # Space between buttons and logo
    total_content_height = new_height + button_spacing + sum(button.height for button in buttons) + (len(buttons) - 1) * button_spacing

    # Determine the starting Y position for the menu content to center it vertically
    content_start_y = (screen_height - total_content_height) // 2

    # Position the logo at the start of the content area
    logo_rect.center = (screen_width // 2, content_start_y + new_height // 2)
    content_start_y += new_height + button_spacing  # Update the starting Y for the buttons

    # Overlay for dimming the background
    overlay = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    surface.blit(overlay, (0, 0))

    # Draw the logo
    surface.blit(logo_image, logo_rect)

    # Draw buttons centered and below the logo
    for button_rect, text in [(start_game_button_rect, "Start Game"), (quit_button_rect, "Quit")]:
        button_rect.centerx = screen_width // 2
        button_rect.y = content_start_y
        color = (0, 255, 0) if button_rect.collidepoint(mouse_pos) else (255, 255, 255)
        pygame.draw.rect(surface, color, button_rect)
        text_surf, text_rect = button_font.render(text, (0, 0, 0))
        text_rect.center = button_rect.center
        surface.blit(text_surf, text_rect)
        content_start_y += button_rect.height + button_spacing



def draw_rules_overlay(surface):
    global screen_width, screen_height  # Use global screen dimensions
    if show_rules:
        # Draw a semi-transparent background
        overlay = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        surface.blit(overlay, (0, 0))

        # Calculate rules box position and size to center it
        rules_box_width = 700
        rules_box_height = 600
        rules_box_x = (screen_width - rules_box_width) // 2
        rules_box_y = (screen_height - rules_box_height) // 2

        rules_rect = pygame.Rect(rules_box_x, rules_box_y, rules_box_width, rules_box_height)
        border_rect = rules_rect.inflate(6, 6)
        pygame.draw.rect(surface, (56, 62, 130), border_rect, 0, 7)
        pygame.draw.rect(surface, (175, 180, 196), rules_rect, 0, 7)

        # Rules content
        rules_text = [
            "Rules:",
            "- Arrange cubes on the grid to match the correct positions.",
            "- Clues are provided below the grid. Use logic to find",
            "  the correct position for each piece.",
            "- Click 'Submit' to check your solution.",
            "- Click 'Next Round' to proceed to the next challenge.",
            "- Complete all rounds to win the game.",
        ]

        # Start rendering rules text a bit below the top of the rules box
        text_start_y = rules_box_y + 150
        for line in rules_text:
            # Render each line of text and center it within the rules box
            text_surface, text_rect = clue_font.render(line, (0, 0, 0))
            text_x = rules_box_x + (rules_box_width - text_rect.width) // 2
            surface.blit(text_surface, (text_x, text_start_y))
            text_start_y += 30  # Increment y position for the next line


def draw_validation_overlay(surface, message):
    global screen_width, screen_height
    if show_validate:
        # Draw a semi-transparent background
        overlay = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        surface.blit(overlay, (0, 0))

        # Dimensions for the validation message box
        message_box_width = 700
        message_box_height = 200

        # Calculate positions to center the message box on the screen
        message_box_x = (screen_width - message_box_width) // 2
        message_box_y = (screen_height - message_box_height) // 2

        message_rect = pygame.Rect(message_box_x, message_box_y, message_box_width, message_box_height)
        border_rect = message_rect.inflate(6, 6)  # Add some padding for the border

        pygame.draw.rect(surface, (56, 62, 130), border_rect, 0, 7)  # Border
        pygame.draw.rect(surface, (175, 180, 196), message_rect, 0, 7)  # Message box

        # Render the message
        congrats_message = "Congratulations. You beat the game!" if current_round == 14 and message == "Correct! Click 'Next Round' to continue." else message
        solved_message = f"You solved the round in {str(elapsed_time)} seconds" if message == "Correct! Click 'Next Round' to continue." else None

        # Calculate the position of the text for centering
        congrats_surf, congrats_rect = title_font.render(congrats_message, (117, 165, 35))
        congrats_rect.midtop = (screen_width // 2, message_box_y + 40)  # Adjust the Y offset as needed
        surface.blit(congrats_surf, congrats_rect.topleft)  # Use topleft of the rect for positioning

        if solved_message:
            solved_surf, solved_rect = title_font.render(solved_message, (117, 165, 35))
            solved_rect.midtop = (screen_width // 2, message_box_y + 90)  # Adjust for spacing
            surface.blit(solved_surf, solved_rect.topleft)  # Use topleft of the rect for positioning


def draw_title(screen):
    global screen_height, screen_width
    # Round title
    title_surf, title_rect = title_font.render(
        f"Round {current_round + 1}", (0, 255, 0))
    title_rect.center = (screen_width // 2, 210)  # Adjust as needed
    screen.blit(title_surf, title_rect)

def draw_container(surface):
    container_rect = pygame.Rect(
        0, container_y, screen.get_width(), container_height)
    pygame.draw.rect(surface, container_color, container_rect, -1)

def draw_cubes(surface):
    cubes_to_draw = []

    for cube in cubes:
        if cube is not selected_cube:
            cubes_to_draw.append(cube)

    for cube in cubes_to_draw:

        if cube['color_name'] == "Black":
            pygame.draw.rect(surface, cube['color'], cube['rect'], 0, 7)
            text_surf, text_rect = clue_font.render(cube['color_name'], (255, 255, 255))
            text_rect.center = cube['rect'].center
            surface.blit(text_surf, text_rect)
        else:
            pygame.draw.rect(surface, cube['color'], cube['rect'], 0, 7)
            text_surf, text_rect = clue_font.render(cube['color_name'], (0, 0, 0))
            text_rect.center = cube['rect'].center
            surface.blit(text_surf, text_rect)

    for cube in cubes:
        if cube is selected_cube:
            if cube['color_name'] == "Black":
                pygame.draw.rect(
                    surface, selected_cube['color'], selected_cube['rect'])
                text_surf, text_rect = clue_font.render(
                    selected_cube['color_name'], (255, 255, 255))
                text_rect.center = selected_cube['rect'].center
                surface.blit(text_surf, text_rect)
            else:
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
            pygame.draw.rect(surface, (255, 255, 255), rect, 3, 2)

def draw_buttons(surface):
    def draw_button(rect, text, is_active, border_thickness=1.5, border_color=(242, 195, 39)):
        # Calculate the border rect by inflating the original rect
        border_rect = rect.inflate(border_thickness * 2, border_thickness * 2)
        button_inner_color = (0, 180, 0) if is_active and rect.collidepoint(pygame.mouse.get_pos()) else button_color
        # Draw the border rect first
        pygame.draw.rect(surface, border_color, border_rect, 0, 7)  # Adjust the corner radius if needed

        # Then draw the button rect over it
        pygame.draw.rect(surface, button_inner_color, rect, 0, 7)

        # Render the button text
        text_surf = button_font.render(text, fgcolor=(255, 255, 255), size=24)[0]
        text_rect = text_surf.get_rect(center=rect.center)
        surface.blit(text_surf, text_rect)


    if start_game and not positions_correct:
        draw_button(reset_button_rect, "Reset", True)
        draw_button(undo_button_rect, "Undo", True)
        draw_button(check_button_rect, "Submit", True)
        draw_button(rules_button_rect, "Rules", True)
        draw_button(music_button_rect, "Music", True)
        draw_button(volume_up_button_rect, "Vol +", True)
        draw_button(volume_down_button_rect, "Vol -", True)
    # Draw "Next Round" button
    if positions_correct:
        global cubes
        cubes = []
        draw_button(next_round_button_rect, "Next Round", True)


def draw_clues(surface, clues):
    global screen_width, screen_height
    
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
def play_game():
    global cubes
    if current_round >= len(default_positions):
        print(f"Configuration for round {current_round} is missing.")
        return
    cubes = [] 
    starting_positions = default_positions[current_round]
    for color_name, grid_pos in starting_positions.items():
        color_rgb = COLORS[color_name]
        cube_rect = pygame.Rect(grid_origin[0] + grid_pos[0] * cell_size,
                                grid_origin[1] + grid_pos[1] * cell_size, cell_size, cell_size)
        
        is_movable = True if current_round == 9 else False

        cubes.append({
            'color': color_rgb,
            'rect': cube_rect,
            'grid_pos': grid_pos,
            'color_name': color_name,
            'movable': is_movable,
            'correct_pos': rounds_correct_positions[current_round][color_name] 
        })

    off_grid_start_y = container_y + (container_height - cell_size) // 2

    placed_colors = starting_positions.keys()
    x_offset = 0
    for color_name, correct_pos in rounds_correct_positions[current_round].items():
        if color_name not in placed_colors:
            color_rgb = COLORS[color_name]
            cube_rect = pygame.Rect(x_offset, off_grid_start_y, cell_size, cell_size)
            original_pos = (x_offset, off_grid_start_y)  
            cubes.append({
                'color': color_rgb,
                'rect': cube_rect,
                'grid_pos': None, 
                'color_name': color_name,
                'movable': True,
                'original_pos': original_pos,
                'correct_pos': correct_pos
            })
            x_offset += cell_size + 10


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
    if 'original_pos' in cube:
        cube['rect'].topleft = cube['original_pos']
    else:
        # Handle the case where a cube might not have an original_pos for some reason
        print("Cube does not have an original position.")

# --------------------------Testing functions ---------------------------------------
def autocomplete_cubes():
    global cubes, positions_correct, message
    # Update each cube's grid position to its correct position
    for cube in cubes:
        cube['grid_pos'] = cube['correct_pos']
        # Also update the cube's rect position accordingly
        cube_rect_x = grid_origin_x + cube['correct_pos'][0] * cell_size
        cube_rect_y = grid_origin_y + cube['correct_pos'][1] * cell_size
        cube['rect'].topleft = (cube_rect_x, cube_rect_y)

#     positions_correct = True
#     message = "Correct! Click 'Next Round' to continue."
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
    play_game()  # Place initial cubes for the new level
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
    play_game()  # Place initial cubes for the previous level
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
        play_game()
    elif next_round_button_rect.collidepoint(event.pos) and positions_correct:
        if current_round < len(rounds_correct_positions) - 1:
            current_round += 1
            player_start_time = pygame.time.get_ticks()
            start_game = True
            positions_correct = False
            play_game()
        elif current_round == 14:
            current_round = 0
            start_game = True
            positions_correct = False

play_game()
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

            # ---- Landing Page Buttons --------

            if start_game_button_rect.collidepoint(event.pos):
                menu_visible = False  # Hide the menu only if "Start Game" is clicked
                start_game = True
            elif not start_game and quit_button_rect.collidepoint(event.pos):  # Check if the quit button was clicked and game hasn't started
                pygame.quit()
                exit()
                
            handle_game_logic(event)

            # ---- End Landing Page Buttons --------
            # ---- Piece Select Listener --------

            if not selected_cube:  # Only select a new cube if we aren't already dragging one
                selected_cube = get_clicked_cube(event.pos)
                if selected_cube:  # If a cube is selected, remove it from its grid position for free dragging
                    record_move(
                        selected_cube, selected_cube['rect'].copy(), selected_cube['grid_pos'])
                    selected_cube['grid_pos'] = None

            # Handle button clicks separately from cube selection
            handle_game_logic(event)

            # ---- End Piece Select Listener --------

            # -----------Main Button Click listeners-------

            # Click listeners - Rules
            if rules_button_rect.collidepoint(event.pos):
                show_rules = not show_rules  # Toggle rules visibility
            elif show_rules and not rules_button_rect.collidepoint(event.pos):
                show_rules = False

            # Click listeners - Submit
            if check_button_rect.collidepoint(event.pos):
                show_validate = not show_validate  # Toggle rules visibility
            elif show_validate and not check_button_rect.collidepoint(event.pos):
                show_validate = False
            
            # Click listeners - Music
            if music_button_rect.collidepoint(event.pos):
                toggle_music()
            elif volume_up_button_rect.collidepoint(event.pos):
                increase_volume()
            elif volume_down_button_rect.collidepoint(event.pos):
                decrease_volume()

            # -----------End Main Button Click listeners-------
                
        elif event.type == pygame.MOUSEBUTTONUP:
            if selected_cube:
                snap_cube_to_grid(selected_cube)
                selected_cube = None  # Deselect cube after dropping it

        elif event.type == pygame.MOUSEMOTION:
            if selected_cube:  # Move the selected cube with mouse
                selected_cube['rect'].center = event.pos

        # -----------TESTING Level Skip Shortcuts-------
                
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:  # 'N' key for 'Next Level'
                skip_to_next_level()
            elif event.key == pygame.K_a:  # Assuming 'A' key for autocomplete
                autocomplete_cubes()
            elif event.key == pygame.K_b:  # 'B' key for 'Previous Level'
                go_to_previous_level()

        # -----------TESTING End Level Skip Shortcuts-------

    screen.fill((0, 0, 0))
    if 0 <= current_round < len(background_images):
        current_background = background_images[current_round]
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
