import sys
import platform
import getpass
from datetime import datetime
from pathlib import Path
import time
from Function.game.game_core import *  # Import game core components

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

        # Game core state (directly connected to game_core)
        self.snake = []
        self.direction = RIGHT
        self.next_direction = RIGHT
        self.food = None
        self.bomb = None
        self.score = 0
        self.fps = 10
        self.snake_length = 1

        # Time related
        self.start_time = 0
        self.time_limit = 0  # in seconds
        self.current_mode = ""
        self.time_option = ""

        # Audio system
        self.bg_music = BackgroundMusic("Assets/audio/background/background_music.wav")
        self.sounds = GameSounds()
        self.bg_music.load()

    def init_game_state(self):
        """Initialize game state (connecting to game_core's core logic)"""
        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.next_direction = RIGHT
        self.food = generate_food(
            self.snake
        )  # Use food generation function from game_core
        self.bomb = self.generate_bomb()
        self.score = 0
        self.snake_length = 1
        self.fps = 10
        self.bg_music.play()

    def generate_bomb(self):
        """Generate bomb (referencing level_challenge implementation)"""
        if random.random() < 0.3:  # 30% chance to generate bomb
            while True:
                x = random.randint(0, GRID_WIDTH - 1)
                y = random.randint(0, GRID_HEIGHT - 1)
                bomb = (x, y)
                if bomb not in self.snake and bomb != self.food:
                    return bomb
        return None

    def check_collisions(self):
        """Collision detection (connecting to game_core's collision logic)"""
        head = self.snake[0]

        # Self collision
        if head in self.snake[1:]:
            self.sounds.play_crash()
            return True

        # Boundary collision (infinite mode has boundaries by default)
        if (
            head[0] < 0
            or head[0] >= GRID_WIDTH
            or head[1] < 0
            or head[1] >= GRID_HEIGHT
        ):
            self.sounds.play_crash()
            return True

        return False

    def update_snake(self):
        """Update snake position (connecting to game_core's movement logic)"""
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        self.snake.insert(0, new_head)

    def handle_food_eaten(self):
        """Handle food consumption logic (connecting to game_core's food mechanism)"""
        if self.snake[0] == self.food:
            self.sounds.play_eat()
            self.score += 10
            self.snake_length += 1
            self.food = generate_food(self.snake)  # Regenerate food
            self.bomb = self.generate_bomb()
            self.fps += 0.5  # Increase speed with score
        else:
            self.snake.pop()

    def handle_bomb_hit(self):
        """Handle bomb collision"""
        if self.snake[0] == self.bomb and self.bomb:
            self.sounds.play_crash()
            # Bomb effects differ by mode
            if self.current_mode == "limited":
                self.snake_length = max(1, self.snake_length - 2)
            else:
                self.snake_length = max(1, self.snake_length - 3)
            self.snake = self.snake[: self.snake_length]
            self.bomb = self.generate_bomb()

    # System information and data recording methods remain unchanged
    def get_system_info(self):
        computer_name = platform.node()
        user_name = getpass.getuser()
        return computer_name, user_name

    def record_limited_time_data(self, time_option):
        computer_name, user_name = self.get_system_info()
        timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        file_map = {
            "10 Minutes": "10_minutes.txt",
            "20 Minutes": "20_minutes.txt",
            "30 Minutes": "30_minutes.txt",
            "1 Hour": "1_hour.txt",
        }
        filename = f"Fraction/Infinite Challenge/Limited time/{file_map[time_option]}"
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"{timestamp} {computer_name} {user_name} {self.score}\n")

    def record_unlimited_time_data(self):
        computer_name, user_name = self.get_system_info()
        timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        filename = "Fraction/Infinite Challenge/Unlimited time/limitless.txt"
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"{timestamp} {computer_name} {user_name} {self.score}\n")

    # Event handling (added in-game direction controls)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.in_main_menu or self.in_time_menu:
                    # Menu navigation logic remains unchanged
                    if event.key == pygame.K_UP:
                        if self.in_main_menu:
                            self.selected_option = (self.selected_option - 1) % len(
                                self.options
                            )
                        else:
                            self.selected_time = (self.selected_time - 1) % len(
                                self.time_options
                            )
                    elif event.key == pygame.K_DOWN:
                        if self.in_main_menu:
                            self.selected_option = (self.selected_option + 1) % len(
                                self.options
                            )
                        else:
                            self.selected_time = (self.selected_time + 1) % len(
                                self.time_options
                            )
                    elif event.key == pygame.K_RETURN:
                        if self.in_main_menu:
                            if self.selected_option == 0:
                                self.in_main_menu = False
                                self.in_time_menu = True
                            elif self.selected_option == 1:
                                self.start_unlimited_challenge()
                            elif self.selected_option == 2:
                                self.running = False
                        else:
                            if self.selected_time == 4:
                                self.in_time_menu = False
                                self.in_main_menu = True
                            else:
                                self.start_limited_challenge(
                                    self.time_options[self.selected_time]
                                )
                    elif event.key == pygame.K_ESCAPE:
                        if self.in_time_menu:
                            self.in_time_menu = False
                            self.in_main_menu = True
                        else:
                            self.running = False
                elif self.in_game:
                    # In-game controls (connecting to direction key logic)
                    if event.key == pygame.K_ESCAPE:
                        self.end_game()
                    elif event.key == pygame.K_UP and self.direction != DOWN:
                        self.next_direction = UP
                    elif event.key == pygame.K_DOWN and self.direction != UP:
                        self.next_direction = DOWN
                    elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                        self.next_direction = LEFT
                    elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                        self.next_direction = RIGHT

    def start_limited_challenge(self, time_option):
        self.current_mode = "limited"
        self.time_option = time_option
        self.in_time_menu = False
        self.in_game = True
        time_map = {
            "10 Minutes": 600,
            "20 Minutes": 1200,
            "30 Minutes": 1800,
            "1 Hour": 3600,
        }
        self.time_limit = time_map[time_option]
        self.start_time = time.time()
        self.init_game_state()

    def start_unlimited_challenge(self):
        self.current_mode = "unlimited"
        self.in_main_menu = False
        self.in_game = True
        self.start_time = time.time()
        self.init_game_state()

    def check_time_limit(self):
        if self.current_mode == "limited":
            elapsed = time.time() - self.start_time
            if elapsed >= self.time_limit:
                self.end_game()
                return True
        return False

    def end_game(self):
        if self.current_mode == "limited":
            self.record_limited_time_data(self.time_option)
        else:
            self.record_unlimited_time_data()
        self.bg_music.stop()
        self.in_game = False
        self.in_main_menu = True

    def render(self):
        self.screen.fill(BLACK)

        if self.in_main_menu or self.in_time_menu:
            # Menu rendering remains unchanged
            if self.in_main_menu:
                title = self.font.render("Select Infinite Challenge Mode", True, GREEN)
                options = self.options
                selected = self.selected_option
            else:
                title = self.font.render("Select Time Limit", True, GREEN)
                options = self.time_options
                selected = self.selected_time

            self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 100))
            for i, option in enumerate(options):
                color = (255, 255, 255) if i == selected else (100, 100, 100)
                text = self.small_font.render(option, True, color)
                self.screen.blit(
                    text, (self.width // 2 - text.get_width() // 2, 200 + i * 50)
                )
        elif self.in_game:
            # Game screen rendering (using game_core's drawing functions)
            draw_snake(self.screen, self.snake)  # Draw snake
            draw_food(self.screen, self.food)  # Draw food
            draw_score(self.screen, self.score)  # Draw score

            # Draw bomb
            if self.bomb:
                x, y = self.bomb
                pygame.draw.rect(
                    self.screen,
                    BLUE,
                    (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE),
                )

            # Mode information rendering
            if self.current_mode == "limited":
                title = self.font.render(
                    f"Limited Time: {self.time_option}", True, GREEN
                )
                elapsed = time.time() - self.start_time
                remaining = max(0, self.time_limit - elapsed)
                time_text = self.small_font.render(
                    f"Time Remaining: {int(remaining // 60)}m{int(remaining % 60)}s",
                    True,
                    (255, 255, 255),
                )
            else:
                title = self.font.render("Unlimited Time Mode", True, GREEN)
                elapsed = time.time() - self.start_time
                time_text = self.small_font.render(
                    f"Time Elapsed: {int(elapsed // 60)}m{int(elapsed % 60)}s",
                    True,
                    (255, 255, 255),
                )

            self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 30))
            self.screen.blit(time_text, (50, 80))
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
                # Game main loop logic
                self.direction = self.next_direction
                self.update_snake()
                self.handle_food_eaten()
                self.handle_bomb_hit()

                # Check game over conditions
                if self.check_collisions() or self.check_time_limit():
                    self.end_game()

            self.render()
            clock.tick(self.fps if self.in_game else 30)
