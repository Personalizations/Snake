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

# Game constants
GRID_SIZE = 20
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Color definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)  # Snake body
DARK_GREEN = (0, 200, 0)  # Snake head
RED = (255, 0, 0)  # Food
BLUE = (0, 0, 255)  # Bomb


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

        # Grid configuration
        self.grid_width = self.width // GRID_SIZE
        self.grid_height = self.height // GRID_SIZE

        # Game state initialization
        self.snake = []
        self.direction = RIGHT
        self.next_direction = RIGHT
        self.food = None
        self.bomb = None
        self.fps = 10

        # Level goal configuration
        self.level_goals = {
            "Easy": [100 + i * 50 for i in range(20)],
            "Normal": [200 + i * 150 for i in range(20)],
            "Hard": [400 + i * 350 for i in range(20)],
            "Nightmare": [900 + i * 150 for i in range(20)],
        }

        # Length growth configuration
        self.length_multipliers = {
            "Easy": 1.5,
            "Normal": 1.25,
            "Hard": 0.75,
            "Nightmare": 0.25,
        }

        # Bomb effect configuration
        self.bomb_effects = {
            "Easy": 0,  # No bombs
            "Normal": 0,  # No bombs
            "Hard": 0.5,  # 50% length reduction
            "Nightmare": 0.75,  # 75% length reduction
        }

        # Wall effect configuration
        self.wall_effects = {
            "Easy": False,  # No death on wall collision
            "Normal": 0.3,  # 30% chance of death on wall collision
            "Hard": True,  # Death on wall collision
            "Nightmare": True,  # Death on wall collision
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

    def generate_food(self):
        """Generate food (not overlapping with snake or bomb)"""
        while True:
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)
            food_pos = (x, y)
            # Ensure food doesn't overlap with snake or bomb
            if food_pos not in self.snake and food_pos != self.bomb:
                return food_pos

    def generate_bomb(self):
        """Generate bomb (only in difficulties with bomb effects)"""
        if self.bomb_effects[self.current_difficulty] <= 0:
            return None

        while True:
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)
            bomb_pos = (x, y)
            # Ensure bomb doesn't overlap with snake or food
            if bomb_pos not in self.snake and bomb_pos != self.food:
                return bomb_pos

    def draw_snake(self):
        """Draw the snake"""
        # Draw snake head
        head_x, head_y = self.snake[0]
        pygame.draw.rect(
            self.screen,
            DARK_GREEN,
            (head_x * GRID_SIZE, head_y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        )
        # Draw snake body
        for segment in self.snake[1:]:
            x, y = segment
            pygame.draw.rect(
                self.screen,
                GREEN,
                (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            )

    def draw_food(self):
        """Draw the food"""
        if self.food:
            x, y = self.food
            pygame.draw.rect(
                self.screen,
                RED,
                (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            )

    def draw_bomb(self):
        """Draw the bomb"""
        if self.bomb and self.bomb_effects[self.current_difficulty] > 0:
            x, y = self.bomb
            pygame.draw.rect(
                self.screen,
                BLUE,
                (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            )

    def handle_collisions(self):
        """Handle collision detection"""
        head = self.snake[0]

        # Self collision detection
        if head in self.snake[1:]:
            self.record_data(self.current_difficulty, self.current_level, False)
            self.in_menu = True
            return

        # Wall collision detection
        if self.wall_effects[self.current_difficulty]:
            if (head[0] < 0 or head[0] >= self.grid_width or
                    head[1] < 0 or head[1] >= self.grid_height):
                self.record_data(self.current_difficulty, self.current_level, False)
                self.in_menu = True
                return
        elif isinstance(self.wall_effects[self.current_difficulty], float):
            # Probabilistic wall collision death (Normal difficulty)
            if (head[0] < 0 or head[0] >= self.grid_width or
                    head[1] < 0 or head[1] >= self.grid_height):
                if random.random() < self.wall_effects[self.current_difficulty]:
                    self.record_data(self.current_difficulty, self.current_level, False)
                    self.in_menu = True
                    return
                else:
                    # Wall penetration (exit from opposite side)
                    new_x = head[0] % self.grid_width
                    new_y = head[1] % self.grid_height
                    self.snake[0] = (new_x, new_y)
        else:
            # Wall penetration mode (Easy difficulty)
            new_x = head[0] % self.grid_width
            new_y = head[1] % self.grid_height
            self.snake[0] = (new_x, new_y)

    def handle_events(self):
        """Handle events"""
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
                        self.record_data(self.current_difficulty, self.current_level, False)
                        self.in_menu = True
                    # Direction controls
                    elif event.key == pygame.K_UP and self.direction != DOWN:
                        self.next_direction = UP
                    elif event.key == pygame.K_DOWN and self.direction != UP:
                        self.next_direction = DOWN
                    elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                        self.next_direction = LEFT
                    elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                        self.next_direction = RIGHT

    def start_challenge(self, difficulty):
        """Start the challenge"""
        self.in_menu = False
        self.current_difficulty = difficulty
        self.current_level = 1
        self.snake_length = 1
        self.fps = 10  # Initial speed

        # Initialize snake (starting from center)
        center_x = self.grid_width // 2
        center_y = self.grid_height // 2
        self.snake = [(center_x, center_y)]
        self.direction = RIGHT
        self.next_direction = RIGHT

        # Generate initial food and bomb
        self.food = self.generate_food()
        self.bomb = self.generate_bomb()

    def update_game_state(self):
        """Update game state"""
        if self.in_menu:
            return

        # Update direction
        self.direction = self.next_direction

        # Move snake
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        self.snake.insert(0, new_head)

        # Check food collision
        if new_head == self.food:
            self.handle_food_eaten()
            self.food = self.generate_food()
            # Difficulty increase: speed up every 3 levels
            if self.current_level % 3 == 0:
                self.fps += 1
        else:
            # Remove tail if no food eaten
            self.snake.pop()

        # Check bomb collision
        if new_head == self.bomb and self.bomb_effects[self.current_difficulty] > 0:
            self.handle_bomb_hit()
            self.bomb = self.generate_bomb()

        # Check collisions
        self.handle_collisions()

    def handle_food_eaten(self):
        """Handle food eaten logic"""
        multiplier = self.length_multipliers[self.current_difficulty]
        self.snake_length += multiplier

        # Check if level is completed
        if self.check_level_complete(self.current_difficulty):
            self.record_data(self.current_difficulty, self.current_level, True)
            if self.current_level < 20:
                self.current_level += 1
                # Generate new food and bomb
                self.food = self.generate_food()
                self.bomb = self.generate_bomb()
            else:
                # Completed all levels
                self.in_menu = True

    def handle_bomb_hit(self):
        """Handle bomb hit logic"""
        effect = self.bomb_effects[self.current_difficulty]
        if effect > 0:
            self.snake_length *= (1 - effect)
            # Ensure length is at least 1
            if self.snake_length < 1:
                self.snake_length = 1
            # Remove corresponding number of body segments
            remove_count = max(1, int(len(self.snake) * effect))
            for _ in range(remove_count):
                if len(self.snake) > 1:
                    self.snake.pop()

    def render(self):
        self.screen.fill(BLACK)

        if self.in_menu:
            title = self.font.render("Select Difficulty", True, (0, 255, 0))
            self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 100))

            for i, difficulty in enumerate(self.difficulties):
                color = (255, 255, 255) if i == self.selected_difficulty else (100, 100, 100)
                text = self.small_font.render(difficulty, True, color)
                self.screen.blit(
                    text, (self.width // 2 - text.get_width() // 2, 200 + i * 50)
                )
        else:
            # Draw game elements
            self.draw_snake()
            self.draw_food()
            self.draw_bomb()

            # Draw title
            title = self.font.render(
                f"{self.current_difficulty} - Level {self.current_level}",
                True,
                (0, 255, 0),
            )
            self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 30))

            # Display current length and goal
            goal = self.level_goals[self.current_difficulty][self.current_level - 1]
            info = self.small_font.render(
                f"Current Length: {self.snake_length:.1f} / Goal: {goal}",
                True,
                (255, 255, 255),
            )
            self.screen.blit(info, (50, 50))

            # Display control hint
            hint = self.small_font.render(
                "Press ESC to return to menu", True, (100, 100, 100)
            )
            self.screen.blit(hint, (self.width - 200, self.height - 50))

        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            self.handle_events()
            self.update_game_state()  # update game state
            self.render()
            clock.tick(self.fps)  # Control speed with current FPS
