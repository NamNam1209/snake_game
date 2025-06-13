"""
Constants and configuration for Snake Game
"""
import pygame

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400  # Reduced screen size for 10x10 grid
SCREEN_HEIGHT = 400
GRID_SIZE = 40  # Increased grid size to make each cell 40x40 pixels
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE  # 10 cells wide
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE  # 10 cells high

# Game speed
BASE_SNAKE_SPEED = 10  # Lower is slower

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)  # Color for bonus food
BLUE = (0, 0, 255)
LIGHT_BLUE = (100, 100, 255)
LIGHT_GREEN = (100, 255, 100)
LIGHT_RED = (255, 100, 100)
PURPLE = (128, 0, 128)
LIGHT_PURPLE = (200, 100, 200)
GOLD = (255, 215, 0)

# High score file
HIGHSCORE_FILE = "highscores.json"

# Fonts
FONT = pygame.font.SysFont('Arial', 24)
SMALL_FONT = pygame.font.SysFont('Arial', 18)
BIG_FONT = pygame.font.SysFont('Arial', 48)

# Button dimensions
BUTTON_WIDTH = 120
BUTTON_HEIGHT = 50
BUTTON_MARGIN = 20

# Countdown settings
COUNTDOWN_DURATION = 2  # seconds
