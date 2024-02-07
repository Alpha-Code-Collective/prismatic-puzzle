def check_cubes_position(cubes):
    positions_correct = all(
        cube['grid_pos'] == cube['correct_pos'] for cube in cubes)
    message = "Correct! Click 'Next Round' to continue." if positions_correct else "Not quite right, try again."
    return positions_correct, message


