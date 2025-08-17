# Function/exit_game.py
import sys
import pygame

def exit_game():
    print("Exit Game...")
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    exit_game()