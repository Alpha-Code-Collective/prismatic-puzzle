# Software Requirements

## Vision

- What is the vision of this product?
    - A digital version of the game Chromacube as a python game application to exercise one’s brain for developing children and the elderly.
- What pain point does this project solve?
    - Cognitive stimulation, learning and skills development and lack of educational content in logical reasoning
- Why should we care about your product?
    - Offers a rich and multifaceted experience that not only entertains but also contributes to personal development and well-being. Its blend of cognitive challenges, educational content, and accessible gameplay makes it a valuable game for a wide audience.

## Scope (In/Out)

- IN - What will your product do
    - Displays a game that allows the player to solve a puzzle given colors and clues

- OUT - What will your product not do.
    - It will never turn into an IOS or Android app.
    - Will not be playable on a web browser

- What will your MVP functionality be?
    - A game that includes progressive difficulty as the player moves through the levels
    - Includes puzzle validation and feedback to inform the player if the solution is correct or incorrect
    - Rules on how to play the game is available on start and accessible throughout gameplay
    - Player can reset the puzzle so they can start over
    - Game is accessible and includes color names for reference and dynamic backgrounds to inform the player of the current level

## Stretch

- What are your stretch goals?
    - Two player mode
    - Scoring system

- What stretch goals are you going to aim for?
    - Two player mode
    - Scoring system

## Functional Requirements

- List the functionality of your product. This will consist of tasks such as the following:
    - A player can play the game
Data Flow

- Describe the flow of data in your application. Write out what happens from the time the user begins using the app to the time the user is done with the app. Think about the “Happy Path” of the application. Describe through visuals and text what requests are made, and what data is processed, in addition to any other details about how the user moves through the site.
    - Player starts game
    - Game displays the instructions
    - Game displays board, clues, blocks to be inserted 
    - Player can validate solution or clear board
    - If solution is correct, player starts new game

## Non-Functional Requirements (301 & 401 only)

- Non-functional requirements are requirements that are not directly related to the functionality of the application but still important to the app.

- Usability
    - Intuitive gameplay and accessible to color-impaired 
    - Instructions available on start and throughout gameplay
    - Feedback mechanism to alert player if solution is valid or incorrect
- Testability
    - Validating player solution to actual solution
    - Preventing player from “brute-forcing” way to the solution
    - Maintainable code base to enable scalability for additional levels

