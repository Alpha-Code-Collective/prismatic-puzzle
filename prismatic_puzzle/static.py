COLORS = {
    "Coral": (255, 127, 80),
    "Emerald": (4, 99, 7),
    "Cobalt": (0, 71, 171),
    "Mustard": (255, 219, 88),
    "Orange": (255, 103, 0),
    "Purple": (104, 40, 96),
    "Magenta": (255, 0, 255),
    "Brown": (150, 75, 0),
    "Mint": (0, 245, 163),
    "Teal": (0, 128, 128),
    "White": (255, 255, 255),
    "Grey": (103, 103, 103),
}

CLUES = [
    # Round 1 clues
    [
        "Coral and Magenta are in the same column.",
        "Grey sits next to Magenta.",
        "Either Teal or Grey sits next to Cobalt.",
        "Coral sits next to White.",
    ],
    # Round 2 clues
    [
        "White isn't in a corner space but Mustard is.",
        "Coral is the farthest distance from Emerald, which sits next to Teal.",
        "Purple is in the same column as Mint, which is in the same row as Orange.",
    ],
    # Round 3 clues
    [
        "White and Cobalt are in the same column.",
        "Mustard and Orange are in the same column.",
        "Brown is closer to Emerald than Teal.",
        "Mustard is not in the same row as White, which is not in the same column as Teal.",
        "Coral sits next to a color found in the Irish flag.",
    ],
    # Round 4 clues
    [
        "Emerald, Teal, and Mint are in the same row.",
        "Grey and White are in the opposite corners.",
        "Teal, Emerald and Brown sit next to Magenta.",
        "White sits next to Mint.",
        "Orange and Purple are in the same row.",
        "Grey, Emerald & Mustard are in the same column.",
    ],
    # Round 5 clues
    [
        "Colors that start with 'B', 'G' and 'C' are in the top corners.",
        "Colors that start with 'M' are in the same column.",
        "Neither Coral nor Teal sit next to Magenta.",
        "Coral and Brown are in the same row.",
        "Emerald sits next to Mustard.",
    ],
    # Round 6 clues
    [
        "Orange, Mint, and Purple are in the same row.",
        "Cobalt is in the same column as Mustard.",
        "All rows are in alphabetical order from left to right.",
        "Orange is not in the same column as Magenta.",
    ],
    # Round 7 clues
    [
        "Colors that start with the same letter are in the same column.",
        "Mint sits between Purple and Emerald.",
        "Teal and Coral are as far apart as they can be.",
        "Teal is in the same column as White, which is in the same row as Magenta,", 
        "which is in the same column as Mustard, which is in the same row as Coral.",
        "Orange sits next to Emerald.",
    ],
    # Round 8 clues
    [
        "Teal and Brown are in the middle row and middle two columns.",
        "All rows are in alphabetical order from left to right.",
        "White is in the same column as Magenta and Purple.",
        "Mustard sits above Brown.",
    ],
    # Round 9 clues
    [
        "Two rows are in alphabetical order from left to right.",
        "If Orange is in a corner space, then White sits between Mint and Emerald.",
        "Teal, Mint, and Purple are in the same row.",
        "Teal is opposite from Mustard.",
    ],
    # Round 10 clues
    [
        "Place Orange and White after completing the rest of the clues in order.",
        "Swap Mint with a color that starts with 'C'.",
        "Shift all blocks down so that open spaces are at the top of the board.",
        "Reverse the order of the middle row.",
        "Swap the colors in the left-most column.",
        "Shift blocks left so that open spaces are at the right.",
        "Cobalt should be in the top row",
        "Place Orange next to Coral",
    ],
    #Round 11 clues
    [
        "Orange is 2 spaces below Cobalt, which is 2 spaces to the left of Emerald", 
        "which is above White",
        "Brown sits to the right of Mint, which is 2 spaces below Teal", 
        "which is 2 spaces to the right of Grey.",
        "Mustard sits below Purple, which is 2 spaces to the left of Coral."
    ],
    # round 12
    [
        "Mustard sits next to 'E', 'C', 'O' and one other color.",
        "A halloween pair sits on the bottom row.",
        "Magenta, White and Brown so not share a row or column.",
        "Teal sits below Cobalt, which is in the same row as Brown"
    ],
    # round 13
    [
        "Brown knows Orange, Cobalt, and one other.",
        "Grey and Brown have heard of each other, but don't know each other",
        "Teal knows Coral, Purple, and one other.",
        "Teal can see Orange and White but doesn't know them." ,
        "The only color Teal can both see and know is Purple.",
        "Cobalt knows White and can see Mustard.",
        "Coral has never heard of Mint but knows Emerald."
    ],
    # round 14
    [
        "Emerald only knows colors that are 4 letters long.",
        "Brown can see Magenta and Purple,",
        "and has heard of Ornage, but doesn't know any of them.",
        "Grey only knows Orange, Mint and Mustard, but has heard of White."
    ],
    # round 15
    [
       "Grey and Mustard hate each other. Magenta and Orange also hate each other",
       "White knows Mint, Teal, and Emerald and a color that starts with 'C'.",
       "Purple can see Orange but only knows Emerald, Cobalt, and Grey.",
       "Brown has heard of Purple, knows Mint, and can see Mustard.",
       "Teal doesn't know Purple or Brown, Emerald doens't know Mustard or Brown.",
       "Cobalt doesn't know Magenta or Orange.",
       "Emerald has heard of, but doesn't know Mint.",
    ]
]
default_positions = [
    # Round 1
    {"Coral": (1, 2), "Emerald": (0, 0), "Cobalt": (2, 2)},
    # round 2
    {
        "Grey": (1, 1),
        "Cobalt": (1, 0),
        "Brown": (2, 1),
        "Orange": (3, 1),
        "Coral": (3, 0),
        "Magenta": (2, 0),
    },
    # round 3
    {
        "Emerald": (0, 1),
        "Mint": (1, 2),
        "Grey": (2, 1),
        "Purple": (3, 2),
        "Magenta": (1, 0),
        "Coral": (3, 0),
    },
    # round 4
    {
        "Orange": (1, 2),
        "Coral": (2, 2),
        "Magenta": (2, 1),
        "Cobalt": (1, 0),
    },
    # round 5
    {
        "Orange": (2, 0),
        "Emerald": (0, 1),
        "Teal": (2, 1),
        "Purple": (2, 2),
        "Cobalt": (3, 2),
        "White": (3, 1),
    },
    # round 6
    {
        "Coral": (1, 2),
        "Emerald": (1, 0),
        "Teal": (3, 2),
        "White": (3, 1),
        "Grey": (0, 1),
    },
    # round 7
    {
        "Cobalt": (0, 0),
        "Mint": (2, 1),
        "Brown": (3, 2),
    },
    # round 8
    {},
    # round 9
    {
        "Coral": (0, 0),
        "Cobalt": (0, 2),
        "Mustard": (3, 1),
    },
    {
        "Mint": (0, 0),
        "Teal": (1, 0),
        "Coral": (2, 0),
        "Cobalt": (3, 0),
        "Emerald": (1, 1),
        "Mustard": (3, 1),
        "Magenta": (0, 2),
        "Grey": (1, 2),
        "Purple": (2, 2),
        "Brown": (3, 2),
    },
    # round 11
    {},
    # round 12
    {
        "Coral": (0, 1), 
        "Mint": (0, 2), 
        "White": (2, 1)
    },
    # round 13
    {
        "Teal": (3, 1),
        "Coral": (3, 0),
        "Cobalt": (0, 2),
        "Magenta": (0, 0),
        "Grey": (1, 0),
        "Purple": (2, 1),
        "Brown": (1, 2),
        "Orange": (1,1)
    },
    # round 14
    {
        "Emerald": (0, 0),
        "Purple": (1, 2)
    },
    # round 15
    {
        "Mustard": (3, 0),
        "White": (2, 1),
        "Grey": (0, 2)
    }
]


# may need to fix 1-4, 0,0 starts at top left not botton left
rounds_correct_positions = [
    # Round 1
    {
        "Coral": (1, 2),
        "Emerald": (0, 0),
        "Cobalt": (2, 2),
        "Mustard": (3, 1),
        "Orange": (1, 1),
        "Purple": (3, 0),
        "Magenta": (1, 0),
        "Brown": (2, 1),
        "Mint": (0, 1),
        "Teal": (3, 2),
        "White": (0, 2),
        "Grey": (2, 0),
    },
    # Round 2
    {
        "Coral": (3, 0),
        "Emerald": (0, 2),
        "Cobalt": (1, 0),
        "Mustard": (3, 2),
        "Orange": (3, 1),
        "Purple": (0, 0),
        "Magenta": (2, 0),
        "Brown": (2, 1),
        "Mint": (0, 1),
        "Teal": (1, 2),
        "White": (2, 2),
        "Grey": (1, 1),
    },
    # Round 3
    {
        "Coral": (3, 0),
        "Emerald": (0, 1),
        "Cobalt": (0, 2),
        "Mustard": (2, 2),
        "Orange": (2, 0),
        "Purple": (3, 2),
        "Magenta": (1, 0),
        "Brown": (1, 1),
        "Mint": (1, 2),
        "Teal": (3, 1),
        "White": (0, 0),
        "Grey": (2, 1),
    },
    # Round 4
    {
        "Coral": (2, 2),
        "Emerald": (3, 1),
        "Cobalt": (1, 0),
        "Mustard": (3, 0),
        "Orange": (1, 2),
        "Purple": (0, 2),
        "Magenta": (2, 1),
        "Brown": (2, 0),
        "Mint": (0, 1),
        "Teal": (1, 1),
        "White": (0, 0),
        "Grey": (3, 2),
    },
    # Round 5
    {
        "Coral": (3, 0),
        "Emerald": (0, 1),
        "Cobalt": (3, 2),
        "Mustard": (1, 1),
        "Orange": (2, 0),
        "Purple": (2, 2),
        "Magenta": (1, 0),
        "Brown": (0, 0),
        "Mint": (1, 2),
        "Teal": (2, 1),
        "White": (3, 1),
        "Grey": (0, 2),
    },
    # Round 6
    {
        "Coral": (1, 2),
        "Emerald": (1, 1),
        "Cobalt": (0, 3),
        "Mustard": (1, 1),
        "Orange": (2, 0),
        "Purple": (0, 2),
        "Magenta": (1, 0),
        "Brown": (2, 2),
        "Mint": (0, 0),
        "Teal": (1, 3),
        "White": (2, 3),
        "Grey": (1, 2),
    },
    # Round 7
    {
        "Coral": (0, 1),
        "Emerald": (1, 0),
        "Cobalt": (2, 2),
        "Mustard": (0, 0),
        "Orange": (1, 2),
        "Purple": (2, 3),
        "Magenta": (0, 2),
        "Brown": (1, 1),
        "Mint": (2, 0),
        "Teal": (0, 3),
        "White": (1, 3),
        "Grey": (2, 1),
    },
    # Round 8
    {
        "Coral": (2, 2),
        "Emerald": (0, 0),
        "Cobalt": (1, 1),
        "Mustard": (2, 3),
        "Orange": (0, 1),
        "Purple": (1, 2),
        "Magenta": (2, 0),
        "Brown": (0, 2),
        "Mint": (1, 3),
        "Teal": (2, 1),
        "White": (0, 3),
        "Grey": (1, 0),
    },
    # Round 9
    {
        "Coral": (1, 0),
        "Emerald": (2, 3),
        "Cobalt": (0, 1),
        "Mustard": (1, 3),
        "Orange": (2, 1),
        "Purple": (0, 2),
        "Magenta": (1, 1),
        "Brown": (2, 0),
        "Mint": (0, 3),
        "Teal": (1, 2),
        "White": (2, 2),
        "Grey": (0, 0),
    },
    # Round 10
    {
        "Coral": (2, 0),
        "Emerald": (0, 2),
        "Cobalt": (1, 3),
        "Mustard": (2, 1),
        "Orange": (0, 3),
        "Purple": (1, 0),
        "Magenta": (2, 3),
        "Brown": (0, 1),
        "Mint": (1, 2),
        "Teal": (2, 2),
        "White": (0, 0),
        "Grey": (1, 1),
    },
    # Round 11
    {
        "Coral": (2, 1),
        "Emerald": (3, 0),
        "Cobalt": (1, 0),
        "Mustard": (0, 2),
        "Orange": (1, 2),
        "Purple": (0, 1),
        "Magenta": (1, 1),
        "Brown": (3, 2),
        "Mint": (2, 2),
        "Teal": (2, 0),
        "White": (3, 1),
        "Grey": (0, 0),
    },
    # round 12
    {
        "Coral": (0, 1),
        "Emerald": (1, 0),
        "Cobalt": (3, 0),
        "Mustard": (1, 1),
        "Orange": (1, 2),
        "Purple": (2, 0),
        "Magenta": (3, 2),
        "Brown": (0, 0),
        "Mint": (0, 2),
        "Teal": (3, 1),
        "White": (2, 1),
        "Grey": (2, 2),
    },
    # round 13
    {
        "Teal": (3, 1),
        "Coral": (3, 0),
        "Cobalt": (0, 2),
        "Magenta": (0, 0),
        "Grey": (1, 0),
        "Purple": (2, 1),
        "Brown": (1, 2),
        "Orange": (1, 1),
        "White": (0, 1),
        "Mustard": (3, 2),
        "Mint": (2, 2),
        "Emerald": (2, 0)   
    },
    # round 14
    {
        "Emerald": (0, 0),
        "Purple": (1, 2),
        "Mint": (1, 0),
        "Grey": (2, 0),
        "Orange": (3, 0),
        "Teal": (0, 1),
        "Coral": (1, 1),
        "Mustard": (2, 1),
        "Cobalt": (3, 1),
        "Magenta": (0, 2),
        "Purple": (1, 2),
        "White": (2, 2),
        "Brown": (3, 2)
            
    },
    {
        "Emerald": (2, 2),
        "Purple": (1, 2),
        "Mint": (2, 0),
        "Grey": (0, 2),
        "Orange": (3, 2),
        "Teal": (3, 1),
        "Coral": (0, 1),
        "Mustard": (3, 0),
        "Cobalt": (1, 1),
        "Magenta": (0, 0),
        "Purple": (1, 2),
        "White": (2, 1),
        "Brown": (1, 0)
    }
]
