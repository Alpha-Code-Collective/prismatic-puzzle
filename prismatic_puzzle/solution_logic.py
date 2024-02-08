def check_cubes_position(cubes):
    any_position_set = any(cube['grid_pos'] is not None for cube in cubes)

    # If no positions are set, we know immediately the setup is not correct
    if not any_position_set:
        return False, "Not quite right, try again."

    positions_correct = all(
        cube['grid_pos'] == cube['correct_pos'] for cube in cubes)
    message = "Correct! Click 'Next Round' to continue." if positions_correct else "Not quite right, try again."
    return positions_correct, message
