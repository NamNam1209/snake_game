"""
Screen rendering functions for Snake Game
"""
import pygame
import time
from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, GRAY, GOLD,
    FONT, SMALL_FONT, BIG_FONT
)
from models.enums import GameState

def draw_grid(surface, grid_size):
    """Draw the game grid"""
    for x in range(0, SCREEN_WIDTH, grid_size):
        pygame.draw.line(surface, GRAY, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, grid_size):
        pygame.draw.line(surface, GRAY, (0, y), (SCREEN_WIDTH, y))

def draw_menu(surface, big_font, font, buttons):
    """Draw the main menu screen"""
    surface.fill(WHITE)
    
    # Draw title
    title_text = big_font.render('Snake Game', True, BLACK)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
    surface.blit(title_text, title_rect)
    
    # Draw subtitle
    subtitle_text = font.render('Select Difficulty:', True, BLACK)
    subtitle_rect = subtitle_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
    surface.blit(subtitle_text, subtitle_rect)
    
    # Draw buttons
    for button in buttons:
        button.draw(surface)

def draw_countdown(surface, big_font, font, start_time, duration):
    """Draw the countdown screen"""
    surface.fill(WHITE)
    
    # Calculate remaining time
    elapsed = time.time() - start_time
    remaining = max(0, duration - elapsed)
    countdown_text = str(int(remaining) + 1)
    
    # Draw countdown
    text_surface = big_font.render(countdown_text, True, BLACK)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    surface.blit(text_surface, text_rect)
    
    # Draw "Get Ready!" text
    ready_text = font.render("Get Ready!", True, BLACK)
    ready_rect = ready_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
    surface.blit(ready_text, ready_rect)

def draw_game(surface, grid_size, snake, food, score, game_time, difficulty):
    """Draw the main game screen"""
    surface.fill(WHITE)
    draw_grid(surface, grid_size)
    snake.draw(surface)
    food.draw(surface)
    
    # Draw score
    score_text = FONT.render(f'Score: {score}', True, BLACK)
    surface.blit(score_text, (10, 10))
    
    # Draw time
    time_text = FONT.render(f'Time: {int(game_time)}s', True, BLACK)
    time_rect = time_text.get_rect(midtop=(SCREEN_WIDTH // 2, 10))
    surface.blit(time_text, time_rect)
    
    # Draw difficulty
    diff_text = FONT.render(f'Difficulty: {difficulty.name}', True, BLACK)
    diff_rect = diff_text.get_rect(topright=(SCREEN_WIDTH - 10, 10))
    surface.blit(diff_text, diff_rect)
    
    # Draw food count
    food_text = SMALL_FONT.render(
        f'Regular: {snake.regular_food_eaten} | Bonus: {snake.bonus_food_eaten}', 
        True, BLACK
    )
    food_rect = food_text.get_rect(bottomleft=(10, SCREEN_HEIGHT - 10))
    surface.blit(food_text, food_rect)

def draw_game_over(surface, snake, game_time):
    """Draw the game over screen"""
    # Draw semi-transparent overlay
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 128))  # Semi-transparent black
    surface.blit(overlay, (0, 0))
    
    # Draw game over message
    game_over_text = BIG_FONT.render('Game Over!', True, WHITE)
    text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60))
    surface.blit(game_over_text, text_rect)
    
    # Draw final score
    score_text = FONT.render(f'Final Score: {snake.score}', True, WHITE)
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 10))
    surface.blit(score_text, score_rect)
    
    # Draw time played
    time_text = FONT.render(f'Time: {int(game_time)}s', True, WHITE)
    time_rect = time_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
    surface.blit(time_text, time_rect)
    
    # Draw food eaten
    food_text = FONT.render(
        f'Food: {snake.regular_food_eaten} regular, {snake.bonus_food_eaten} bonus', 
        True, WHITE
    )
    food_rect = food_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    surface.blit(food_text, food_rect)
    
    # Draw restart instruction
    restart_text = FONT.render('Press R to restart or M for menu', True, WHITE)
    restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 90))
    surface.blit(restart_text, restart_rect)

def draw_victory(surface, snake, game_time):
    """Draw the victory screen"""
    # Draw semi-transparent overlay
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 128))  # Semi-transparent black
    surface.blit(overlay, (0, 0))
    
    # Draw victory message
    victory_text = BIG_FONT.render('Victory!', True, GOLD)
    text_rect = victory_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60))
    surface.blit(victory_text, text_rect)
    
    # Draw final score
    score_text = FONT.render(f'Final Score: {snake.score}', True, WHITE)
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 10))
    surface.blit(score_text, score_rect)
    
    # Draw time played
    time_text = FONT.render(f'Time: {int(game_time)}s', True, WHITE)
    time_rect = time_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
    surface.blit(time_text, time_rect)
    
    # Draw food eaten
    food_text = FONT.render(
        f'Food: {snake.regular_food_eaten} regular, {snake.bonus_food_eaten} bonus', 
        True, WHITE
    )
    food_rect = food_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    surface.blit(food_text, food_rect)
    
    # Draw restart instruction
    restart_text = FONT.render('Press R to restart or M for menu', True, WHITE)
    restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 90))
    surface.blit(restart_text, restart_rect)

def draw_highscores(surface, highscores, back_button):
    """Draw the high scores screen"""
    surface.fill(WHITE)
    
    # Draw title
    title_text = BIG_FONT.render('High Scores', True, BLACK)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 40))
    surface.blit(title_text, title_rect)
    
    # Draw highscore table headers
    header_y = 100
    surface.blit(SMALL_FONT.render("Rank", True, BLACK), (20, header_y))
    surface.blit(SMALL_FONT.render("Name", True, BLACK), (60, header_y))
    surface.blit(SMALL_FONT.render("Score", True, BLACK), (150, header_y))
    surface.blit(SMALL_FONT.render("Time", True, BLACK), (210, header_y))
    surface.blit(SMALL_FONT.render("Food", True, BLACK), (270, header_y))
    surface.blit(SMALL_FONT.render("Diff", True, BLACK), (330, header_y))
    
    # Draw horizontal line
    pygame.draw.line(surface, BLACK, (20, header_y + 25), (380, header_y + 25), 2)
    
    # Draw highscores
    if highscores:
        for i, score in enumerate(highscores):
            y = header_y + 35 + i * 25
            
            # Rank
            surface.blit(SMALL_FONT.render(f"{i+1}", True, BLACK), (20, y))
            
            # Name
            surface.blit(SMALL_FONT.render(score['name'][:8], True, BLACK), (60, y))
            
            # Score
            surface.blit(SMALL_FONT.render(f"{score['score']}", True, BLACK), (150, y))
            
            # Time
            surface.blit(SMALL_FONT.render(f"{int(score['time_played'])}s", True, BLACK), (210, y))
            
            # Food (regular + bonus)
            food_text = f"{score['regular_food']}+{score['bonus_food']}"
            surface.blit(SMALL_FONT.render(food_text, True, BLACK), (270, y))
            
            # Difficulty
            diff_text = score['difficulty'][:1]  # Just first letter
            surface.blit(SMALL_FONT.render(diff_text, True, BLACK), (330, y))
    else:
        no_scores_text = FONT.render("No scores yet!", True, BLACK)
        no_scores_rect = no_scores_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        surface.blit(no_scores_text, no_scores_rect)
    
    # Draw back button
    back_button.draw(surface)
