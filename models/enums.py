"""
Enumerations for Snake Game
"""
from enum import Enum

# Game states
class GameState(Enum):
    MENU = 0
    COUNTDOWN = 1
    PLAYING = 2
    GAME_OVER = 3
    VICTORY = 4
    HIGHSCORE = 5

# Difficulty levels
class Difficulty(Enum):
    EASY = 0
    NORMAL = 1
    HARD = 2

# Direction enum
class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
