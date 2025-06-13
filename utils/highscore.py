"""
High Score Manager for Snake Game
"""
import json
import os
import time
from constants import HIGHSCORE_FILE

class HighScoreManager:
    def __init__(self, filename=HIGHSCORE_FILE):
        self.filename = filename
        self.highscores = []
        self.load_highscores()
    
    def load_highscores(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    self.highscores = json.load(f)
            except:
                self.highscores = []
        else:
            self.highscores = []
    
    def save_highscores(self):
        with open(self.filename, 'w') as f:
            json.dump(self.highscores, f)
    
    def add_score(self, name, score, time_played, regular_food, bonus_food, difficulty):
        new_score = {
            'name': name,
            'score': score,
            'time_played': time_played,
            'regular_food': regular_food,
            'bonus_food': bonus_food,
            'difficulty': difficulty,
            'timestamp': time.time()
        }
        
        self.highscores.append(new_score)
        
        # Sort by score (descending) and time (ascending)
        self.highscores.sort(key=lambda x: (-x['score'], x['time_played']))
        
        # Keep only top 10 scores
        if len(self.highscores) > 10:
            self.highscores = self.highscores[:10]
        
        self.save_highscores()
    
    def get_highscores(self):
        return self.highscores
