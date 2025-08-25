import pygame
import random
import sys
from pygame import mixer

# Initialize Pygame and audio system
pygame.init()
mixer.init()

# Game constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Color definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)  # Snake body
DARK_GREEN = (0, 200, 0)  # Snake head
RED = (255, 0, 0)  # Food

# Direction constants
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


# Background music setup
class BackgroundMusic:
    def __init__(self, music_path):
        self.music_path = music_path
        self.volume = 0.5  # Default volume (0.0-1.0)
        self.is_playing = False

    def load(self):
        """Load background music file"""
        try:
            mixer.music.load(self.music_path)
            return True
        except pygame.error as e:
            print(f"Failed to load background music: {e}")
            return False

    def play(self, loop=-1):
        """Play background music with optional loop count (-1 = infinite)"""
        if not self.is_playing and mixer.music.get_busy() == 0:
            mixer.music.set_volume(self.volume)
            mixer.music.play(loop)
            self.is_playing = True

    def stop(self):
        """Stop background music"""
        if self.is_playing:
            mixer.music.stop()
            self.is_playing = False

    def set_volume(self, volume):
        """Set music volume (0.0-1.0)"""
        self.volume = max(0.0, min(1.0, volume))  # Clamp between 0 and 1
        mixer.music.set_volume(self.volume)


# Initialize background music
bg_music = BackgroundMusic("Assets/audio/background/background_music.wav")
bg_music.load()


def generate_food(snake_positions):
    """Generate random food position not on snake"""
    while True:
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        food_position = (x, y)
        if food_position not in snake_positions:
            return food_position


def draw_snake(screen, snake):
    """Draw snake on screen"""
    # Draw head
    head_x, head_y = snake[0]
    pygame.draw.rect(
        screen,
        DARK_GREEN,
        (head_x * GRID_SIZE, head_y * GRID_SIZE, GRID_SIZE, GRID_SIZE),
    )

    # Draw body
    for segment in snake[1:]:
        x, y = segment
        pygame.draw.rect(
            screen, GREEN, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        )


def draw_food(screen, food):
    """Draw food on screen"""
    x, y = food
    pygame.draw.rect(screen, RED, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))


def draw_score(screen, score):
    """Draw current score on screen"""
    font = pygame.font.SysFont("Arial", 24)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))


def game_loop(screen):
    """Main game loop"""
    # Start playing background music
    bg_music.play()

    # Initialize game state
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    direction = RIGHT
    next_direction = direction
    food = generate_food(snake)
    score = 0
    FPS = 10
    clock = pygame.time.Clock()
    running = True

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bg_music.stop()  # Stop music on exit
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Handle direction changes
                if event.key == pygame.K_UP and direction != DOWN:
                    next_direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    next_direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    next_direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    next_direction = RIGHT
                elif event.key == pygame.K_ESCAPE:
                    bg_music.stop()  # Stop music when exiting to menu
                    return
                elif event.key == pygame.K_q:  # Press Q to exit the game
                    bg_music.stop()
                    pygame.quit()
                    sys.exit()

        # Update direction
        direction = next_direction

        # Move snake
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = ((head_x + dx) % GRID_WIDTH, (head_y + dy) % GRID_HEIGHT)

        # Check for self-collision
        if new_head in snake:
            bg_music.stop()  # Stop music on game over
            return

        # Add new head
        snake.insert(0, new_head)

        # Check food collision
        if new_head == food:
            score += 10
            food = generate_food(snake)
            FPS += 0.5  # Increase speed slightly
        else:
            # Remove tail if no food eaten
            snake.pop()

        # Drawing
        screen.fill(BLACK)
        draw_snake(screen, snake)
        draw_food(screen, food)
        draw_score(screen, score)
        pygame.display.flip()

        # Control game speed
        clock.tick(FPS)


def main():
    """Main function to initialize and run the game"""
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    # Start the game loop
    game_loop(screen)

    # Cleanup
    pygame.quit()


if __name__ == "__main__":
    main()
