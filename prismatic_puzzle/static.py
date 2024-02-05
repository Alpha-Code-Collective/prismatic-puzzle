COLORS = {
    'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255),
    'yellow': (255, 255, 0), 'orange': (255, 165, 0), 'purple': (128, 0, 128),
    'pink': (255, 192, 203), 'brown': (165, 42, 42), 'indigo': (75, 0, 130),
    'grey': (128, 128, 128), 'white': (255, 255, 255), 'violet': (238, 130, 238)
}

CLUES = [
   # Round 1 clues
    [
        "round 1 testing",
        "x is in the same row as y",
        "x is in the same row as y",
        "x is in the same row as y"
    ],
    # Round 2 clues
    [
        "round 2 testing",
        "x is in the same row as y",
        "x is in the same row as y",
        "x is in the same row as y"
    ],
    # Round 3 clues
    [
        "round 3 testing",
        "x is in the same row as y",
        "x is in the same row as y",
        "x is in the same row as y"
    ],
    # Round 4 clues
    [
        "round 4 testing",
        "x is in the same row as y",
        "x is in the same row as y",
        "x is in the same row as y"
    ],
    # Round 5 clues
    [
        "round 5 testing",
        "x is in the same row as y",
        "x is in the same row as y",
        "x is in the same row as y"
    ],
    # Round 6 clues
    [
        "round 6 testing",
        "x is in the same row as y",
        "x is in the same row as y",
        "x is in the same row as y"
    ],
    # Round 7 clues
    [
        "round 7 testing",
        "x is in the same row as y",
        "x is in the same row as y",
        "x is in the same row as y"
    ],
    # Round 8 clues
    [
        "round 8 testing",
        "x is in the same row as y",
        "x is in the same row as y",
        "x is in the same row as y"
    ],
    # Round 9 clues
    [
        "round 9 testing",
        "x is in the same row as y",
        "x is in the same row as y",
        "x is in the same row as y"
    ],
    # Round 10 clues
    [
        "round 10 testing",
        "x is in the same row as y",
        "x is in the same row as y",
        "x is in the same row as y"
    ],

]


rounds_correct_positions = [
    # Round 1
    {
        'red': (2, 3), 'green': (0, 1), 'blue': (1, 2),
        'yellow': (0, 2), 'orange': (1, 1), 'purple': (2, 0),
        'pink': (2, 1), 'brown': (0, 3), 'indigo': (1, 0),
        'grey': (1, 3), 'white': (2, 2), 'violet': (0, 0),
    },
    # Round 2
    {
        'red': (1, 3), 'green': (2, 2), 'blue': (0, 1),
        'yellow': (1, 0), 'orange': (0, 2), 'purple': (1, 1),
        'pink': (2, 0), 'brown': (0, 0), 'indigo': (2, 1),
        'grey': (0, 3), 'white': (1, 2), 'violet': (2, 3),
    },
    # Round 3
    {
        'red': (0, 2), 'green': (1, 2), 'blue': (2, 2),
        'yellow': (0, 1), 'orange': (1, 1), 'purple': (2, 1),
        'pink': (0, 0), 'brown': (1, 0), 'indigo': (2, 0),
        'grey': (0, 3), 'white': (1, 3), 'violet': (2, 3),
    },
    # Round 4
    {
        'red': (1, 1), 'green': (0, 3), 'blue': (2, 3),
        'yellow': (1, 2), 'orange': (0, 0), 'purple': (2, 0),
        'pink': (1, 0), 'brown': (0, 2), 'indigo': (2, 1),
        'grey': (1, 3), 'white': (0, 1), 'violet': (2, 2),
    },
    # Round 5
    {
        'red': (2, 1), 'green': (1, 3), 'blue': (0, 0),
        'yellow': (2, 0), 'orange': (1, 0), 'purple': (0, 1),
        'pink': (2, 2), 'brown': (1, 2), 'indigo': (0, 2),
        'grey': (2, 3), 'white': (1, 1), 'violet': (0, 3),
    },
    # Round 6
    {
        'red': (1, 2), 'green': (2, 1), 'blue': (0, 3),
        'yellow': (1, 1), 'orange': (2, 0), 'purple': (0, 2),
        'pink': (1, 0), 'brown': (2, 2), 'indigo': (0, 0),
        'grey': (1, 3), 'white': (2, 3), 'violet': (0, 1),
    },
    # Round 7
    {
        'red': (0, 1), 'green': (1, 0), 'blue': (2, 2),
        'yellow': (0, 0), 'orange': (1, 2), 'purple': (2, 3),
        'pink': (0, 2), 'brown': (1, 1), 'indigo': (2, 0),
        'grey': (0, 3), 'white': (1, 3), 'violet': (2, 1),
    },
    # Round 8
    {
        'red': (2, 2), 'green': (0, 0), 'blue': (1, 1),
        'yellow': (2, 3), 'orange': (0, 1), 'purple': (1, 2),
        'pink': (2, 0), 'brown': (0, 2), 'indigo': (1, 3),
        'grey': (2, 1), 'white': (0, 3), 'violet': (1, 0),
    },
    # Round 9
    {
        'red': (1, 0), 'green': (2, 3), 'blue': (0, 1),
        'yellow': (1, 3), 'orange': (2, 1), 'purple': (0, 2),
        'pink': (1, 1), 'brown': (2, 0), 'indigo': (0, 3),
        'grey': (1, 2), 'white': (2, 2), 'violet': (0, 0),
    },
    # Round 10
    {
        'red': (2, 0), 'green': (0, 2), 'blue': (1, 3),
        'yellow': (2, 1), 'orange': (0, 3), 'purple': (1, 0),
        'pink': (2, 3), 'brown': (0, 1), 'indigo': (1, 2),
        'grey': (2, 2), 'white': (0, 0), 'violet': (1, 1),
    },
]