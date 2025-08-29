import pygame
import sys
import os
import platform
import getpass
from datetime import datetime
from pathlib import Path
import random

# Ensure directory exists
Path("Fraction/Limited Challenges").mkdir(parents=True, exist_ok=True)


class LevelChallenge:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.font = pygame.font.SysFont("SimHei", 36)
        self.small_font = pygame.font.SysFont("SimHei", 24)
        self.difficulties = ["Easy", "Normal", "Hard", "Nightmare", "Back"]
        self.selected_difficulty = 0
        self.current_level = 1
        self.snake_length = 1
        self.running = True
        self.in_menu = True

        # Level goal configuration
        self.level_goals = {
            "Easy": [100 + i * 50 for i in range(20)],
            "Normal": [200 + i * 150 for i in range(20)],
            "Hard": [400 + i * 350 for i in range(20)],
            "Nightmare": [900 + i * 150 for i in range(20)]
        }

        # Length increase configuration
        self.length_multipliers = {
            "Easy": 1.5,
            "Normal": 1.25,
            "Hard": 0.75,
            "Nightmare": 0.25
        }

        # Bomb effect configuration
        self.bomb_effects = {
            "Easy": 0,  # No bombs
            "Normal": 0,  # No bombs
            "Hard": 0.5,  # Reduce length by 50%
            "Nightmare": 0.75  # Reduce length by 75%
        }

        # Wall effect configuration
        self.wall_effects = {
            "Easy": False,  # Not killed by walls
            "Normal": 0.3,  # 30% chance of being killed by walls
            "Hard": True,  # Killed by walls
            "Nightmare": True  # Killed by walls
        }

    def get_system_info(self):
        """Get system information"""
        computer_name = platform.node()
        user_name = getpass.getuser()
        return computer_name, user_name

    def record_data(self, difficulty, level, success):
        """Record level data"""
        computer_name, user_name = self.get_system_info()
        timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        status = "Completed" if success else "Failed"

        filename = f"Fraction/Limited Challenges/{difficulty}.txt"
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"{timestamp} {computer_name} {user_name} Level {level} {status}\n")

    def check_level_complete(self, difficulty):
        """Check if level is completed"""
        return self.snake_length >= self.level_goals[difficulty][self.current_level - 1]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.in_menu:
                    if event.key == pygame.K_UP:
                        self.selected_difficulty = (self.selected_difficulty - 1) % len(self.difficulties)
                    elif event.key == pygame.K_DOWN:
                        self.selected_difficulty = (self.selected_difficulty + 1) % len(self.difficulties)
                    elif event.key == pygame.K_RETURN:
                        if self.selected_difficulty == 4:  # Back
                            self.running = False
                        else:
                            self.start_challenge(self.difficulties[self.selected_difficulty])
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False
                else:
                    # In-game controls
                    if event.key == pygame.K_ESCAPE:
                        self.in_menu = True

    def start_challenge(self, difficulty):
        """Start the challenge"""
        self.in_menu = False
        self.current_difficulty = difficulty
        self.current_level = 1
        self.snake_length = 1
        # Game state should be initialized here

    def handle_food_eaten(self):
        """Handle logic when food is eaten"""
        multiplier = self.length_multipliers[self.current_difficulty]
        self.snake_length += multiplier

        # Check if current level is completed
        if self.check_level_complete(self.current_difficulty):
            self.record_data(self.current_difficulty, self.current_level, True)
            if self.current_level < 20:
                self.current_level += 1
            else:
                # All levels completed
                self.in_menu = True

    def handle_bomb_hit(self):
        """Handle logic when bomb is hit"""
        effect = self.bomb_effects[self.current_difficulty]
        if effect > 0:
            self.snake_length *= (1 - effect)
            if self.snake_length < 1:
                self.snake_length = 1

    def render(self):
        self.screen.fill((0, 0, 0))

        if self.in_menu:
            title = self.font.render("Select Difficulty", True, (0, 255, 0))
            self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 100))

            for i, difficulty in enumerate(self.difficulties):
                color = (255, 255, 255) if i == self.selected_difficulty else (100, 100, 100)
                text = self.small_font.render(difficulty, True, color)
                self.screen.blit(text, (self.width // 2 - text.get_width() // 2, 200 + i * 50))
        else:
            # Render game interface
            title = self.font.render(f"{self.current_difficulty} - Level {self.current_level}", True, (0, 255, 0))
            self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 30))

            # Display current length and goal
            goal = self.level_goals[self.current_difficulty][self.current_level - 1]
            info = self.small_font.render(f"Current Length: {self.snake_length:.1f} / Goal: {goal}", True,
                                          (255, 255, 255))
            self.screen.blit(info, (50, 50))

            # Display control hint
            hint = self.small_font.render("Press ESC to return to menu", True, (100, 100, 100))
            self.screen.blit(hint, (self.width - 200, self.height - 50))

        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            self.handle_events()
            self.render()
            clock.tick(30)