# Prismatic Puzzle

### Author: Andrea Thiel, Bradley Hower, Christopher Acosta, Errol Vidad, Mike Ascalon

### Links and Resources
- Back-end server url (when applicable): None
- Front-end application (when applicable): None

### Setup
- .venv requirements (where applicable)
- run pip install -r requirements.txt

### How to initialize/run your application (where applicable)

- If on a mac computer, change line 9 and 10 to this:
    - from static import COLORS, CLUES, rounds_correct_positions, default_positions
    - from solution_logic import check_cubes_position
    - run python -m prismatic_puzzle.puzzle
- If on a windows computer, change line 9 and 10 to this:
    - from .static import COLORS, CLUES, rounds_correct_positions
    - from .solution_logic import check_cubes_position  
    - run python -m prismatic_puzzle.puzzle  

### Tests
How do you run tests?

N/A

### Wire Frame

[Wire Frame](./supporting-docs/Prismatic%20Puzzle%20Wire%20Frame.png)

### Domain

[Domain Model](./supporting-docs/Domain%20Model.png)
