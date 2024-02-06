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
default_positions = [
    # Round 1
    {
        'red': (3, 0), 'green': (1, 0), 'blue': (2, 0)
    },
    # Round 2
    {
        'pink': (0, 2), 'brown': (2, 0), 'indigo': (3, 2)
    }
    ## Need all 10 rounds!!!
]

rounds_correct_positions = [
    # Round 1
    {
        'red': (3, 0), 'green': (1, 0), 'blue': (2, 0),
        'yellow': (0, 1), 'orange': (1, 1), 'purple': (2, 1),
        'pink': (3, 1), 'brown': (0, 2), 'indigo': (1, 2),
        'grey': (2, 2), 'white': (3, 2), 'violet': (0, 0),
    },
    # Round 2
    {
        'red': (1, 2), 'green': (3, 1), 'blue': (0, 0),
        'yellow': (1, 0), 'orange': (2, 1), 'purple': (3, 0),
        'pink': (0, 2), 'brown': (2, 0), 'indigo': (3, 2),
        'grey': (1, 1), 'white': (2, 2), 'violet': (0, 1),
    },
    # Round 3
    {
        'red': (0, 1), 'green': (2, 2), 'blue': (3, 1),
        'yellow': (0, 2), 'orange': (1, 1), 'purple': (2, 0),
        'pink': (3, 2), 'brown': (0, 0), 'indigo': (1, 2),
        'grey': (2, 1), 'white': (3, 0), 'violet': (1, 0),
    },
    # Round 4
    {
        'red': (2, 1), 'green': (1, 2), 'blue': (0, 2),
        'yellow': (3, 1), 'orange': (1, 0), 'purple': (2, 2),
        'pink': (0, 1), 'brown': (3, 0), 'indigo': (1, 1),
        'grey': (2, 0), 'white': (0, 0), 'violet': (3, 2),
    },
    # Round 5
    {
        'red': (3, 2), 'green': (2, 0), 'blue': (1, 1),
        'yellow': (0, 0), 'orange': (3, 1), 'purple': (2, 1),
        'pink': (1, 2), 'brown': (0, 1), 'indigo': (3, 0),
        'grey': (2, 2), 'white': (1, 0), 'violet': (0, 2),
    },
    # Round 6
    {
        'red': (1, 0), 'green': (2, 2), 'blue': (3, 0),
        'yellow': (0, 2), 'orange': (1, 1), 'purple': (2, 0),
        'pink': (3, 1), 'brown': (0, 0), 'indigo': (1, 2),
        'grey': (2, 1), 'white': (3, 2), 'violet': (0, 1),
    },
    # Round 7
    {
        'red': (2, 0), 'green': (0, 1), 'blue': (1, 2),
        'yellow': (2, 1), 'orange': (3, 0), 'purple': (0, 2),
        'pink': (1, 0), 'brown': (3, 1), 'indigo': (0, 0),
        'grey': (1, 1), 'white': (2, 2), 'violet': (3, 2),
    },
    # Round 8
    {
        'red': (0, 2), 'green': (1, 1), 'blue': (2, 2),
        'yellow': (3, 2), 'orange': (0, 0), 'purple': (1, 0),
        'pink': (2, 0), 'brown': (3, 0), 'indigo': (0, 1),
        'grey': (1, 2), 'white': (2, 1), 'violet': (3, 1),
    },
    # Round 9
    {
        'red': (3, 1), 'green': (2, 1), 'blue': (1, 2),
        'yellow': (0, 2), 'orange': (3, 0), 'purple': (2, 2),
        'pink': (1, 0), 'brown': (0, 0), 'indigo': (3, 2),
        'grey': (2, 0), 'white': (1, 1), 'violet': (0, 1),
    },
    # Round 10
    {
        'red': (1, 1), 'green': (0, 0), 'blue': (3, 2),
        'yellow': (2, 1), 'orange': (1, 2), 'purple': (0, 1),
        'pink': (3, 0), 'brown': (2, 0), 'indigo': (1, 0),
        'grey': (0, 2), 'white': (3, 1), 'violet': (2, 2),
    },
]
