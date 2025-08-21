# Function/start_game.py

import pygame
from Function.game.game_core import game_loop


def start_game():
    # Get the currently displayed screen
    screen = pygame.display.get_surface()
    # Start the game loop
    game_loop(screen)
