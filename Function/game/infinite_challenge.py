import pygame
import sys
import platform
import getpass
from datetime import datetime
from pathlib import Path
import time

# Ensure directories exist
Path("Fraction/Infinite Challenge/Limited time").mkdir(parents=True, exist_ok=True)
Path("Fraction/Infinite Challenge/Unlimited time").mkdir(parents=True, exist_ok=True)


class InfiniteChallenge:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.font = pygame.font.SysFont("SimHei", 36)
        self.small_font = pygame.font.SysFont("SimHei", 24)
        self.options = ["Limited Time", "Unlimited Time", "Back"]
        self.time_options = ["10 Minutes", "20 Minutes", "30 Minutes", "1 Hour", "Back"]
        self.selected_option = 0
        self.selected_time = 0
        self.running = True
        self.in_main_menu = True
        self.in_time_menu = False
        self.in_game = False
        self.snake_length = 1
        self.start_time = 0
        self.time_limit = 0  # in seconds
        self.current_mode = ""

    def get_system_info(self):
        """Get system information"""
        computer_name = platform.node()
        user_name = getpass.getuser()
        return computer_name, user_name

    def record_limited_time_data(self, time_option):
        """Record data for limited time mode"""
        computer_name, user_name = self.get_system_info()
        timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

        # Convert time option to filename
        file_map = {
            "10 Minutes": "10_minutes.txt",
            "20 Minutes": "20_minutes.txt",
            "30 Minutes": "30_minutes.txt",
            "1 Hour": "1_hour.txt",
        }

        filename = f"Fraction/Infinite Challenge/Limited time/{file_map[time_option]}"
        with open(filename, "a", encoding="utf-8") as f:
            f.write(
                f"{timestamp} {computer_name} {user_name} {int(self.snake_length)}\n"
            )

    def record_unlimited_time_data(self):
        """Record data for unlimited time mode"""
        computer_name, user_name = self.get_system_info()
        timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

        filename = "Fraction/Infinite Challenge/Unlimited time/limitless.txt"
        with open(filename, "a", encoding="utf-8") as f:
            f.write(
                f"{timestamp} {computer_name} {user_name} {int(self.snake_length)}\n"
            )

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.in_main_menu:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(
                            self.options
                        )
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(
                            self.options
                        )
                    elif event.key == pygame.K_RETURN:
                        if self.selected_option == 0:  # Limited Time
                            self.in_main_menu = False
                            self.in_time_menu = True
                        elif self.selected_option == 1:  # Unlimited Time
                            self.start_unlimited_challenge()
                        elif self.selected_option == 2:  # Back
                            self.running = False
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False
                elif self.in_time_menu:
                    if event.key == pygame.K_UP:
                        self.selected_time = (self.selected_time - 1) % len(
                            self.time_options
                        )
                    elif event.key == pygame.K_DOWN:
                        self.selected_time = (self.selected_time + 1) % len(
                            self.time_options
                        )
                    elif event.key == pygame.K_RETURN:
                        if self.selected_time == 4:  # Back
                            self.in_time_menu = False
                            self.in_main_menu = True
                        else:
                            time_option = self.time_options[self.selected_time]
                            self.start_limited_challenge(time_option)
                    elif event.key == pygame.K_ESCAPE:
                        self.in_time_menu = False
                        self.in_main_menu = True
                elif self.in_game:
                    if event.key == pygame.K_ESCAPE:
                        # Save data and return to menu
                        if self.current_mode == "limited":
                            self.record_limited_time_data(self.time_option)
                        else:
                            self.record_unlimited_time_data()
                        self.in_game = False
                        self.in_main_menu = True

    def start_limited_challenge(self, time_option):
        """Start limited time challenge"""
        self.current_mode = "limited"
        self.time_option = time_option
        self.in_time_menu = False
        self.in_game = True
        self.snake_length = 1

        # Convert to seconds
        time_map = {
            "10 Minutes": 600,
            "20 Minutes": 1200,
            "30 Minutes": 1800,
            "1 Hour": 3600,
        }
        self.time_limit = time_map[time_option]
        self.start_time = time.time()

    def start_unlimited_challenge(self):
        """Start unlimited time challenge"""
        self.current_mode = "unlimited"
        self.in_main_menu = False
        self.in_game = True
        self.snake_length = 1
        self.start_time = time.time()

    def check_time_limit(self):
        """Check if time limit has been reached"""
        if self.current_mode == "limited":
            elapsed = time.time() - self.start_time
            if elapsed >= self.time_limit:
                self.record_limited_time_data(self.time_option)
                self.in_game = False
                self.in_main_menu = True
                return True
        return False

    def handle_food_eaten(self):
        """Handle logic when food is eaten"""
        # Apply different length increase rules based on mode
        if self.current_mode == "limited":
            self.snake_length += 1  # Basic length increase
        else:  # unlimited
            self.snake_length += 1  # Basic length increase

    def handle_bomb_hit(self):
        """Handle logic when bomb is hit"""
        if self.current_mode == "limited":
            # Limited time mode: reduce length by 50%
            self.snake_length *= 0.5
        else:
            # Unlimited time mode: reduce length by 75%
            self.snake_length *= 0.25

        if self.snake_length < 1:
            self.snake_length = 1

    def render(self):
        self.screen.fill((0, 0, 0))

        if self.in_main_menu:
            title = self.font.render(
                "Select Infinite Challenge Mode", True, (0, 255, 0)
            )
            self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 100))

            for i, option in enumerate(self.options):
                color = (
                    (255, 255, 255) if i == self.selected_option else (100, 100, 100)
                )
                text = self.small_font.render(option, True, color)
                self.screen.blit(
                    text, (self.width // 2 - text.get_width() // 2, 200 + i * 50)
                )
        elif self.in_time_menu:
            title = self.font.render("Select Time Limit", True, (0, 255, 0))
            self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 100))

            for i, time_opt in enumerate(self.time_options):
                color = (255, 255, 255) if i == self.selected_time else (100, 100, 100)
                text = self.small_font.render(time_opt, True, color)
                self.screen.blit(
                    text, (self.width // 2 - text.get_width() // 2, 200 + i * 50)
                )
        elif self.in_game:
            # Render game interface
            if self.current_mode == "limited":
                title = self.font.render(
                    f"Limited Time: {self.time_option}", True, (0, 255, 0)
                )
                elapsed = time.time() - self.start_time
                remaining = max(0, self.time_limit - elapsed)
                time_text = self.small_font.render(
                    f"Time Remaining: {int(remaining // 60)}m{int(remaining % 60)}s",
                    True,
                    (255, 255, 255),
                )
                self.screen.blit(time_text, (50, 80))
            else:
                title = self.font.render("Unlimited Time Mode", True, (0, 255, 0))
                elapsed = time.time() - self.start_time
                time_text = self.small_font.render(
                    f"Time Elapsed: {int(elapsed // 60)}m{int(elapsed % 60)}s",
                    True,
                    (255, 255, 255),
                )
                self.screen.blit(time_text, (50, 80))

            self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 30))

            # Display current length
            length_text = self.small_font.render(
                f"Current Length: {int(self.snake_length)}", True, (255, 255, 255)
            )
            self.screen.blit(length_text, (50, 50))

            # Display control hint
            hint = self.small_font.render(
                "Press ESC to end and save score", True, (100, 100, 100)
            )
            self.screen.blit(hint, (self.width - 250, self.height - 50))

        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            self.handle_events()
            if self.in_game:
                self.check_time_limit()
            self.render()
            clock.tick(30)
