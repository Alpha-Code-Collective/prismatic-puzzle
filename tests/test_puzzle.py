import unittest
from prismatic_puzzle.puzzle import check_cubes_position

class TestGameLogic(unittest.TestCase):
    def test_cubes_correct_position(self):
        cubes = [{'color_name': 'red', 'grid_pos': (0, 0)}, {'color_name': 'blue', 'grid_pos': (1, 1)}]
        rounds_correct_positions = [{'red': (0, 0), 'blue': (1, 1)}]
        current_round = 0
        self.assertTrue(check_cubes_position(cubes, rounds_correct_positions, current_round))

    def test_cubes_incorrect_position(self):
        cubes = [{'color_name': 'red', 'grid_pos': (1, 1)}, {'color_name': 'blue', 'grid_pos': (0, 0)}]
        rounds_correct_positions = [{'red': (0, 0), 'blue': (1, 1)}]
        current_round = 0
        self.assertFalse(check_cubes_position(cubes, rounds_correct_positions, current_round))

if __name__ == '__main__':
    unittest.main()