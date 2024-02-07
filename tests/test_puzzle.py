import unittest
from prismatic_puzzle.solution_logic import check_cubes_position


class TestGameLogic(unittest.TestCase):
    def test_cubes_all_correct_position(self):
        cubes = [
            {'color_name': 'red', 'grid_pos': (0, 0), 'correct_pos': (0, 0)},
            {'color_name': 'blue', 'grid_pos': (1, 1), 'correct_pos': (1, 1)}
        ]
        positions_correct, message = check_cubes_position(cubes)
        self.assertEqual(message, "Correct! Click 'Next Round' to continue.")
        self.assertTrue(positions_correct)

    def test_cubes_one_incorrect_position(self):
        cubes = [
            {'color_name': 'red', 'grid_pos': (1, 1), 'correct_pos': (0, 0)},
            {'color_name': 'blue', 'grid_pos': (0, 0), 'correct_pos': (1, 1)}
        ]
        positions_correct, message = check_cubes_position(cubes)
        self.assertEqual(message, "Not quite right, try again.")
        self.assertFalse(positions_correct)


if __name__ == '__main__':
    unittest.main()
