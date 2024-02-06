import pygame
import pygame.freetype
from sys import exit
import random
# Assuming the static.py file is correctly placed relative to this script.
from static import COLORS, CLUES, rounds_correct_positions, default_positions

pygame.init()
screen = pygame.display.set_mode((1200, 1000))
pygame.display.set_caption('Chroma Cube')
clock = pygame.time.Clock()

# GUI settings
title_font = pygame.freetype.SysFont("Arial", 36)
button_font = pygame.freetype.SysFont("Arial", 24)
clue_font = pygame.freetype.SysFont("Arial", 20)
button_color = (0, 150, 0)
check_button_rect = pygame.Rect(425, 150, 150, 50)  # "Submit" button
next_round_button_rect = pygame.Rect(425, 250, 150, 50)  # "Next Round" button, shown after correct submission
#####
rules_button_rect = pygame.Rect(1000, 25, 150, 50)  # Define the "Rules" button rectangle


# Grid settings
grid_origin = (450, 250)
cell_size = 100
grid_cols, grid_rows = 4, 3
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
            pygame.draw.rect(surface, (0, 180, 0), rect, 0, 5)  # Adjust color for hover effect
        
        # Blit the text surface onto the screen
        surface.blit(text_surf, text_rect)

    if start_game and not positions_correct:
        draw_button(check_button_rect, "Submit", True)
    # Draw "Next Round" button
    if positions_correct:
        draw_button(next_round_button_rect, "Next Round", True)

    pygame.draw.rect(surface, button_color, rules_button_rect)
    rules_surf, rules_rect = button_font.render("Rules", (0, 0, 0))
    rules_rect.center = rules_button_rect.center
    surface.blit(rules_surf, rules_rect)



def draw_clues(surface, clues):
    y_offset = 600
    for clue in clues[current_round]:
        clue_font.render_to(surface, (50, y_offset), clue, (255, 255, 255))
        y_offset += 30

def place_initial_cubes():
    global cubes
    cubes = []

    # Starting positions for cubes on the grid for the current round
    starting_positions = default_positions[current_round]

    # Place the specified cubes on their starting positions on the grid
    for color_name, grid_pos in starting_positions.items():
        color_rgb = COLORS[color_name]
        cube_rect = pygame.Rect(grid_origin[0] + grid_pos[0] * cell_size, grid_origin[1] + grid_pos[1] * cell_size, cell_size, cell_size)
        cubes.append({
            'color': color_rgb,
            'rect': cube_rect,
            'grid_pos': grid_pos,  # This time, we're assigning a grid position
            'color_name': color_name,
            'correct_pos': rounds_correct_positions[current_round][color_name]
        })

    # Adjust starting Y position for the cubes placed off the grid to ensure visibility
    off_grid_start_y = screen.get_height() - cell_size - 10

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
                'correct_pos': correct_pos
            })
            x_offset += cell_size + 10  # Adjust spacing to ensure cubes don't overlap

    # Note: Adjust x_offset increment and off_grid_start_y as needed based on your UI layout and total number of cubes




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
        clue_font.render_to(surface, (400, 600), message, (0, 255, 0))

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
                place_initial_cubes()
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
