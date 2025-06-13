#!/bin/bash

# Start Xvfb
Xvfb :99 -screen 0 800x600x24 &
export DISPLAY=:99

# Run the game
cd /home/ec2-user/q/snake_game
python3 main.py
