"""
Snake class for Snake Game
"""
import pygame
from models.enums import Direction
from constants import GRID_WIDTH, GRID_HEIGHT, GRID_SIZE, GREEN, BLACK

class Snake:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.length = 1
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = Direction.RIGHT
        self.score = 0
        self.is_alive = True
        self.regular_food_eaten = 0
        self.bonus_food_eaten = 0
    
    def get_head_position(self):
        return self.positions[0]
    
    def change_direction(self, direction):
        # Prevent 180-degree turns
        if (direction == Direction.UP and self.direction != Direction.DOWN or
            direction == Direction.DOWN and self.direction != Direction.UP or
            direction == Direction.LEFT and self.direction != Direction.RIGHT or
            direction == Direction.RIGHT and self.direction != Direction.LEFT):
            self.direction = direction
        # If invalid direction, just keep current direction
        # This prevents accidental game over by pressing opposite direction
    
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
    
    def grow(self, amount=1, is_bonus=False):
        self.length += amount
        self.score += 10 * amount
        
        if is_bonus:
            self.bonus_food_eaten += 1
        else:
            self.regular_food_eaten += 1
    
    def draw(self, surface):
        for i, (x, y) in enumerate(self.positions):
            color = GREEN if i == 0 else GREEN  # Head same color as body for now
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, BLACK, rect, 1)  # Border
