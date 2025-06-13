"""
Food class for Snake Game
"""
import pygame
import random
import math
from constants import GRID_WIDTH, GRID_HEIGHT, GRID_SIZE, RED, YELLOW, BLACK

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
