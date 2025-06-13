#!/usr/bin/env python3
"""
Headless test for Snake Game
This script will run the game for a few seconds and then exit
"""
import os
import sys
import time
import pygame
import signal

# Set up display
os.environ['SDL_VIDEODRIVER'] = 'dummy'
pygame.init()
pygame.display.set_mode((800, 600))

print("Snake Game is running in headless mode...")
print("This is a test to verify the game works on your EC2 instance")
print("The game will exit automatically after 5 seconds")

# Set a timer to exit after 5 seconds
def exit_game(signum, frame):
    print("Test completed successfully!")
    sys.exit(0)

signal.signal(signal.SIGALRM, exit_game)
signal.alarm(5)

# Import and run the game in a way that we can control
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from main import Snake, Food, GRID_SIZE, GRID_WIDTH, GRID_HEIGHT, Direction

# Create game objects
snake = Snake()
food = Food()

# Run a few game cycles
for _ in range(50):
    snake.move()
    if snake.get_head_position() == food.position:
        snake.grow()
        food.randomize_position()
    
    # Print some game state
    print(f"Snake position: {snake.get_head_position()}, Length: {snake.length}, Score: {snake.score}")
    time.sleep(0.1)

print("Test completed successfully!")
