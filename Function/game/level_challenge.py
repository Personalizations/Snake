import sys
import platform
import getpass
from datetime import datetime
from pathlib import Path
from Function.game.game_core import *  # Import game core components

# Ensure directory exists
Path("Fraction/Limited Challenges").mkdir(parents=True, exist_ok=True)


class LevelChallenge:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.font = pygame.font.SysFont("Arial", 36)
        self.small_font = pygame.font.SysFont("Arial", 24)
        self.difficulties = ["Easy", "Normal", "Hard", "Nightmare", "Back"]
        self.selected_difficulty = 0
        self.current_level = 1
        self.snake_length = 1
        self.running = True
        self.in_menu = True

        # Game core state
        self.snake = []
        self.direction = RIGHT
        self.next_direction = RIGHT
        self.food = None
        self.bomb = None  # Add bomb
        self.fps = 10
        self.bg_music = BackgroundMusic("Assets/audio/background/background_music.wav")
        self.bg_music.load()

        # Initialize sound effects
        self.sounds = GameSounds()

        # Level goal configuration
        self.level_goals = {
            "Easy": [100 + i * 50 for i in range(20)],
            "Normal": [200 + i * 150 for i in range(20)],
            "Hard": [400 + i * 350 for i in range(20)],
            "Nightmare": [900 + i * 150 for i in range(20)],
        }

        # Other configurations remain unchanged...
        self.length_multipliers = {
            "Easy": 1.5,
            "Normal": 1.25,
            "Hard": 0.75,
            "Nightmare": 0.25,
        }
        self.bomb_effects = {"Easy": 0, "Normal": 0, "Hard": 0.5, "Nightmare": 0.75}
        self.wall_effects = {
            "Easy": False,
            "Normal": 0.3,
            "Hard": True,
            "Nightmare": True,
        }

    def init_game_state(self):
        """Initialize game state"""
        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.next_direction = RIGHT
        self.food = generate_food(self.snake)
        self.generate_bomb()
        self.fps = 10 + (self.current_level - 1) * 2  # Increase speed with level
        self.bg_music.play()

    def generate_bomb(self):
        """Generate bomb (Hard and higher difficulties)"""
        if self.current_difficulty in ["Hard", "Nightmare"] and random.random() < 0.3:
            while True:
                x = random.randint(0, GRID_WIDTH - 1)
                y = random.randint(0, GRID_HEIGHT - 1)
                self.bomb = (x, y)
                if self.bomb not in self.snake and self.bomb != self.food:
                    break
        else:
            self.bomb = None

    def check_collisions(self):
        """Check for collisions"""
        head = self.snake[0]

        # Self collision
        if head in self.snake[1:]:
            return True

        # Wall collision
        if self.wall_effects[self.current_difficulty]:
            if (
                head[0] < 0
                or head[0] >= GRID_WIDTH
                or head[1] < 0
                or head[1] >= GRID_HEIGHT
            ):
                return True
        elif random.random() < self.wall_effects[self.current_difficulty]:
            return True

        return False

    def update_snake(self):
        """Update snake position"""
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        # Handle wall passing (Easy/Normal modes)
        if not self.wall_effects[self.current_difficulty]:
            new_head = (new_head[0] % GRID_WIDTH, new_head[1] % GRID_HEIGHT)

        self.snake.insert(0, new_head)

    def handle_food_eaten(self):
        """Handle food consumption logic (overridden)"""
        if self.snake[0] == self.food:
            # Play eat sound effect
            self.sounds.play_eat()

            multiplier = self.length_multipliers[self.current_difficulty]
            self.snake_length += multiplier
            self.food = generate_food(self.snake)
            self.generate_bomb()
            self.fps += 0.5  # Increase speed
        else:
            self.snake.pop()

    def handle_bomb_hit(self):
        """Handle bomb collision (overridden)"""
        if self.snake[0] == self.bomb and self.bomb:
            effect = self.bomb_effects[self.current_difficulty]
            self.snake_length *= 1 - effect
            self.snake = self.snake[: max(1, int(len(self.snake) * (1 - effect)))]
            self.generate_bomb()
            if self.snake_length < 1:
                self.snake_length = 1

    def start_challenge(self, difficulty):
        """Start challenge (overridden)"""
        self.in_menu = False
        self.current_difficulty = difficulty
        self.current_level = 1
        self.snake_length = 1
        self.init_game_state()  # Initialize game state

    def handle_events(self):
        """Event handling (extended in-game controls)"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.in_menu:
                    # Menu controls remain unchanged...
                    if event.key == pygame.K_UP:
                        self.selected_difficulty = (self.selected_difficulty - 1) % len(
                            self.difficulties
                        )
                    elif event.key == pygame.K_DOWN:
                        self.selected_difficulty = (self.selected_difficulty + 1) % len(
                            self.difficulties
                        )
                    elif event.key == pygame.K_RETURN:
                        if self.selected_difficulty == 4:  # Back
                            self.running = False
                        else:
                            self.start_challenge(
                                self.difficulties[self.selected_difficulty]
                            )
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False
                else:
                    # In-game controls
                    if event.key == pygame.K_ESCAPE:
                        self.in_menu = True
                        self.bg_music.stop()
                    # Direction controls
                    elif event.key == pygame.K_UP and self.direction != DOWN:
                        self.next_direction = UP
                    elif event.key == pygame.K_DOWN and self.direction != UP:
                        self.next_direction = DOWN
                    elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                        self.next_direction = LEFT
                    elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                        self.next_direction = RIGHT

    def render(self):
        """Render (extended game screen)"""
        self.screen.fill(BLACK)

        if self.in_menu:
            # Menu rendering remains unchanged...
            title = self.font.render("Select Difficulty", True, (0, 255, 0))
            self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 100))
            for i, difficulty in enumerate(self.difficulties):
                color = (
                    (255, 255, 255)
                    if i == self.selected_difficulty
                    else (100, 100, 100)
                )
                text = self.small_font.render(difficulty, True, color)
                self.screen.blit(
                    text, (self.width // 2 - text.get_width() // 2, 200 + i * 50)
                )
        else:
            # Game screen rendering
            title = self.font.render(
                f"{self.current_difficulty} - Level {self.current_level}",
                True,
                (0, 255, 0),
            )
            self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 30))

            # Draw game elements
            draw_snake(self.screen, self.snake)
            draw_food(self.screen, self.food)
            if self.bomb:  # Draw bomb (purple)
                x, y = self.bomb
                pygame.draw.rect(
                    self.screen,
                    (128, 0, 128),
                    (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE),
                )

            # Display information
            goal = self.level_goals[self.current_difficulty][self.current_level - 1]
            info = self.small_font.render(
                f"Current Length: {self.snake_length:.1f} / Goal: {goal}",
                True,
                (255, 255, 255),
            )
            self.screen.blit(info, (50, 50))
            hint = self.small_font.render(
                "Press ESC to return to menu", True, (100, 100, 100)
            )
            self.screen.blit(hint, (self.width - 200, self.height - 50))

        pygame.display.flip()

    def run(self):
        """Run game main loop (extended)"""
        clock = pygame.time.Clock()
        while self.running:
            self.handle_events()
            if not self.in_menu:
                # Game logic updates
                self.direction = self.next_direction
                self.update_snake()
                self.handle_food_eaten()
                self.handle_bomb_hit()

                # Check level completion
                if self.check_level_complete(self.current_difficulty):
                    self.record_data(self.current_difficulty, self.current_level, True)
                    if self.current_level < 20:
                        self.current_level += 1
                        self.init_game_state()  # Proceed to next level
                    else:
                        self.in_menu = True
                        self.bg_music.stop()

                # Check game failure and play crash sound
                if self.check_collisions():
                    self.sounds.play_crash()  # Play death sound effect
                    self.record_data(self.current_difficulty, self.current_level, False)
                    self.in_menu = True
                    self.bg_music.stop()

            self.render()
            clock.tick(self.fps if not self.in_menu else 30)

    def get_system_info(self):
        """Get system information including computer and user name"""
        computer_name = platform.node()
        user_name = getpass.getuser()
        return computer_name, user_name

    def record_data(self, difficulty, level, success):
        """Record game data including timestamp, system info, level and status"""
        computer_name, user_name = self.get_system_info()
        timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        status = "Completed" if success else "Failed"
        filename = f"Fraction/Limited Challenges/{difficulty}.txt"
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"{timestamp} {computer_name} {user_name} Level {level} {status}\n")

    def check_level_complete(self, difficulty):
        """Check if current level is completed by comparing snake length with goal"""
        return self.snake_length >= self.level_goals[difficulty][self.current_level - 1]
