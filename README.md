# Snake Game

A classic 2D Snake game built with Pygame where the player controls a growing snake that gains one block in length each time it eats food, avoiding collisions with walls and itself.

## Features

- Classic Snake gameplay mechanics
- Score tracking
- Game over detection with restart option
- Smooth controls
- Grid-based movement

## Requirements

- Python 3.6+
- Pygame

## Installation

1. Clone this repository:
```
git clone https://github.com/NamNam1209/snake_game.git
cd snake_game
```

2. Install the required dependencies:
```
pip install pygame
```

## How to Play

Run the game:
```
python main.py
```

### Controls

- Arrow keys (↑, ↓, ←, →) to control the snake's direction
- Press 'R' to restart after game over

### Game Rules

- The snake moves continuously in the current direction
- Eating regular food (red squares) increases the snake's length by 1 and your score
- Special bonus food (yellow stars) appears randomly after eating regular food
- Eating bonus food increases the snake's length by 3 and gives triple points
- The game ends if the snake hits the walls or itself
- Try to achieve the highest score possible!

## Project Structure

```
snake_game/
├── main.py         # Main game file
├── assets/         # Directory for any game assets
└── README.md       # This file
```

## Future Enhancements

- Add sound effects
- Implement difficulty levels
- Add high score tracking
- Create different types of food with special effects
- Add obstacles

## License

This project is licensed under the MIT License - see the LICENSE file for details.
