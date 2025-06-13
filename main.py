#!/usr/bin/env python3
"""
Snake Game - A classic 2D game built with Pygame
"""
import pygame
import random
import sys
import math
from enum import Enum

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400  # Reduced screen size for 10x10 grid
SCREEN_HEIGHT = 400
GRID_SIZE = 40  # Increased grid size to make each cell 40x40 pixels
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE  # 10 cells wide
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE  # 10 cells high
SNAKE_SPEED = 10  # Lower is slower

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)  # Color for bonus food

# Direction enum
class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Snake:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.length = 1
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = Direction.RIGHT
        self.score = 0
        self.is_alive = True
    
    def get_head_position(self):
        return self.positions[0]
    
    def change_direction(self, direction):
        # Prevent 180-degree turns
        if (direction == Direction.UP and self.direction != Direction.DOWN or
            direction == Direction.DOWN and self.direction != Direction.UP or
            direction == Direction.LEFT and self.direction != Direction.RIGHT or
            direction == Direction.RIGHT and self.direction != Direction.LEFT):
            self.direction = direction
    
    def move(self):
        if not self.is_alive:
            return
        
        head_x, head_y = self.get_head_position()
        
        if self.direction == Direction.UP:
            head_y -= 1
        elif self.direction == Direction.DOWN:
            head_y += 1
        elif self.direction == Direction.LEFT:
            head_x -= 1
        elif self.direction == Direction.RIGHT:
            head_x += 1
        
        # Check for wall collision
        if (head_x < 0 or head_x >= GRID_WIDTH or 
            head_y < 0 or head_y >= GRID_HEIGHT):
            self.is_alive = False
            return
        
        # Check for self collision
        if (head_x, head_y) in self.positions[1:]:
            self.is_alive = False
            return
        
        # Add new head position
        self.positions.insert(0, (head_x, head_y))
        
        # Remove tail if not growing
        if len(self.positions) > self.length:
            self.positions.pop()
    
    def grow(self, amount=1):
        self.length += amount
        self.score += 10 * amount
    
    def draw(self, surface):
        for i, (x, y) in enumerate(self.positions):
            color = GREEN if i == 0 else GREEN  # Head same color as body for now
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, BLACK, rect, 1)  # Border


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.is_bonus = False
        self.randomize_position()
    
    def randomize_position(self):
        self.position = (
            random.randint(0, GRID_WIDTH - 1),
            random.randint(0, GRID_HEIGHT - 1)
        )
    
    def make_bonus(self):
        self.is_bonus = True
    
    def make_regular(self):
        self.is_bonus = False
    
    def draw(self, surface):
        x, y = self.position
        center_x = x * GRID_SIZE + GRID_SIZE // 2
        center_y = y * GRID_SIZE + GRID_SIZE // 2
        
        if self.is_bonus:
            # Draw a star (bonus food)
            self.draw_star(surface, center_x, center_y, GRID_SIZE // 2, YELLOW)
        else:
            # Draw regular food (square)
            rect = pygame.Rect(
                x * GRID_SIZE,
                y * GRID_SIZE,
                GRID_SIZE, GRID_SIZE
            )
            pygame.draw.rect(surface, RED, rect)
            pygame.draw.rect(surface, BLACK, rect, 1)  # Border
    
    def draw_star(self, surface, x, y, size, color):
        # Draw a 5-pointed star
        points = []
        for i in range(10):
            # Alternate between outer and inner points
            angle = math.pi / 5 * i - math.pi / 2
            radius = size if i % 2 == 0 else size / 2
            point_x = x + radius * math.cos(angle)
            point_y = y + radius * math.sin(angle)
            points.append((point_x, point_y))
        
        pygame.draw.polygon(surface, color, points)
        pygame.draw.polygon(surface, BLACK, points, 1)  # Border


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 24)
        self.reset()
    
    def reset(self):
        self.snake = Snake()
        self.food = Food()
        self.game_over = False
        self.food_eaten_count = 0
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_r:
                        self.reset()
                else:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction(Direction.UP)
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction(Direction.DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction(Direction.LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction(Direction.RIGHT)
    
    def update(self):
        if self.game_over:
            return
        
        self.snake.move()
        
        # Check if snake is still alive
        if not self.snake.is_alive:
            self.game_over = True
            return
        
        # Check if snake ate food
        if self.snake.get_head_position() == self.food.position:
            # Determine growth amount based on food type
            if self.food.is_bonus:
                self.snake.grow(3)  # Bonus food makes snake grow by 3
            else:
                self.snake.grow(1)  # Regular food makes snake grow by 1
                self.food_eaten_count += 1
            
            # Make sure food doesn't spawn on snake
            while True:
                self.food.randomize_position()
                if self.food.position not in self.snake.positions:
                    break
            
            # Randomly decide if the next food should be a bonus
            # After eating at least one regular food
            if not self.food.is_bonus and random.random() < 0.3:  # 30% chance
                self.food.make_bonus()
            else:
                self.food.make_regular()
    
    def draw_grid(self):
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, GRAY, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, GRAY, (0, y), (SCREEN_WIDTH, y))
    
    def draw(self):
        self.screen.fill(WHITE)
        self.draw_grid()
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        
        # Draw score
        score_text = self.font.render(f'Score: {self.snake.score}', True, BLACK)
        self.screen.blit(score_text, (10, 10))
        
        # Draw game over message
        if self.game_over:
            game_over_text = self.font.render('Game Over! Press R to restart', True, BLACK)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(game_over_text, text_rect)
        
        pygame.display.update()
    
    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(SNAKE_SPEED)


if __name__ == "__main__":
    game = Game()
    game.run()
