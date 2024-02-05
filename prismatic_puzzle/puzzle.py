import pygame
import pygame.freetype
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode((1000, 1300))
pygame.display.set_caption('Chroma Cube')
clock = pygame.time.Clock()

# Define colors, clues, and correct positions
COLORS = {
    'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255),
    'yellow': (255, 255, 0), 'orange': (255, 165, 0), 'purple': (128, 0, 128),
    'pink': (255, 192, 203), 'brown': (165, 42, 42), 'indigo': (75, 0, 130),
    'grey': (128, 128, 128), 'white': (255, 255, 255), 'violet': (238, 130, 238)
}
# For simplicity, we're not defining clues or correct positions here. You'll need to design this based on your game's logic.
CLUES = ["Clue 1", "Clue 2", "Clue 3", "Clue 4"]

# GUI settings
button_font = pygame.freetype.SysFont("Arial", 24)
clue_font = pygame.freetype.SysFont("Arial", 20)
button_color = (0, 150, 0)
button_rect = pygame.Rect(425, 50, 150, 50)
check_button_rect = pygame.Rect(425, 150, 150, 50)  # Button to check positions

# Grid settings
grid_origin = (300, 300)
cell_size = 100
grid_cols, grid_rows = 3, 4
grid_positions = [(x, y) for x in range(grid_cols) for y in range(grid_rows)]

# Assign correct spots for each cube (This part is simplified for demonstration)
# In a real game, you'd map these to specific clues and logic.
correct_positions = {
    'red': (0, 0), 'green': (1, 0), 'blue': (2, 1),
    'yellow': (2, 2), 'orange': (1, 1), 'purple': (2, 3),
    'pink': (0, 1), 'brown': (1, 2), 'indigo': (0, 2),
    'grey': (0, 3), 'white': (2, 0), 'violet': (1, 3)
}
cubes = []
selected_cube = None
start_game = False
message = ""
CLUES = [
    "1. Blue is directly above Yellow.",
    "2. Grey is in the same row as Pink but not next to it.",
    "3. Purple is in the bottom right corner.",
    "4. White is to the right of Brown, in the same column as Blue.",
    "5. Red is in the top left corner.",
    "6. Green is next to Red, but not on top of Yellow.",
    "7. Orange is in the same column as Purple, but not in the bottom row.",
    "8. Indigo is in the same row as Yellow and Violet.",
    "9. Pink is in the top row.",
    "10. Violet is to the right of Blue.",
    "11. Brown is somewhere above Grey."
]
color_name_font = pygame.freetype.SysFont("Arial", 18)  # Smaller font for color names
def draw_cubes(surface):
    for cube in cubes:
        pygame.draw.rect(surface, cube['color'], cube['rect'])
        # Render the color name text within the cube
        text_surf, text_rect = clue_font.render(cube['color_name'], (0, 0, 0))  # Black text
        # Calculate text position to center it in the cube
        text_rect.center = cube['rect'].center
        surface.blit(text_surf, text_rect)
def draw_grid(surface):
    for row in range(grid_rows):
        for col in range(grid_cols):
            rect = pygame.Rect(grid_origin[0] + col * cell_size, grid_origin[1] + row * cell_size, cell_size, cell_size)
            pygame.draw.rect(surface, (255, 255, 255), rect, 3)

def draw_buttons(surface):
    # Start button
    button_font.render_to(surface, (button_rect.x + 20, button_rect.y + 15), "Start", (255, 255, 255))
    pygame.draw.rect(surface, button_color, button_rect, 0, 5)
    # Check button
    button_font.render_to(surface, (check_button_rect.x + 20, check_button_rect.y + 15), "Check", (255, 255, 255))
    pygame.draw.rect(surface, button_color, check_button_rect, 0, 5)

def draw_clues(surface, clues):
    y_offset = 850  # Moved up from previous position
    for clue in clues:
        clue_font.render_to(surface, (50, y_offset), clue, (255, 255, 255))
        y_offset += 30
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
def place_initial_cubes():
    global cubes
    cubes = []
    # Randomly place 4 cubes on the grid
    initial_positions = random.sample(grid_positions, 4)
    for color_name, grid_pos in zip(COLORS.keys(), initial_positions):
        color_rgb = COLORS[color_name]
        cube_rect = pygame.Rect(grid_origin[0] + grid_pos[0] * cell_size, grid_origin[1] + grid_pos[1] * cell_size, cell_size, cell_size)
        cubes.append({'color': color_rgb, 'rect': cube_rect, 'grid_pos': grid_pos, 'color_name': color_name, 'correct_pos': correct_positions[color_name]})

    # Place remaining cubes off to the side
    x_offset = 50
    for color_name in list(COLORS.keys())[4:]:
        color_rgb = COLORS[color_name]
        cube_rect = pygame.Rect(x_offset, 1100, cell_size, cell_size)
        cubes.append({'color': color_rgb, 'rect': cube_rect, 'grid_pos': None, 'color_name': color_name, 'correct_pos': correct_positions[color_name]})
        x_offset += 100

def check_cubes_position():
    global message
    if all(cube['grid_pos'] == cube['correct_pos'] for cube in cubes):
        message = "Congratulations! All cubes are in the correct spot!"
    else:
        message = "Not quite right, try again."

def draw_message(surface, message):
    if message:
        clue_font.render_to(surface, (300, 900), message, (0, 255, 0))
def get_clicked_cube(pos):
    for cube in cubes:
        if cube['rect'].collidepoint(pos):
            return cube
    return None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos) and not start_game:
                start_game = True
                place_initial_cubes()
            elif check_button_rect.collidepoint(event.pos) and start_game:
                check_cubes_position()
            else:
                selected_cube = get_clicked_cube(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            if selected_cube:
                snap_cube_to_grid(selected_cube)
                selected_cube = None
        elif event.type == pygame.MOUSEMOTION and selected_cube:
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
