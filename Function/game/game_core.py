import pygame
import random
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
BLUE = (0, 0, 255)  # Bomb

# Direction constants
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class BackgroundMusic:
    """Background music management class"""
    def __init__(self, music_path):
        self.music_path = music_path
        self.volume = 0.5  # Default volume
        self.is_playing = False

    def load(self):
        """Load music file"""
        try:
            mixer.music.load(self.music_path)
            return True
        except pygame.error as e:
            print(f"Failed to load background music: {e}")
            return False

    def play(self, loop=-1):
        """Play music (-1 for infinite loop)"""
        if not self.is_playing and not mixer.music.get_busy():
            mixer.music.set_volume(self.volume)
            mixer.music.play(loop)
            self.is_playing = True

    def stop(self):
        """Stop music"""
        if self.is_playing:
            mixer.music.stop()
            self.is_playing = False

    def set_volume(self, volume):
        """Set volume (0.0-1.0)"""
        self.volume = max(0.0, min(1.0, volume))
        mixer.music.set_volume(self.volume)


def generate_food(snake_positions):
    """Generate food position not on snake body"""
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
        screen, DARK_GREEN,
        (head_x * GRID_SIZE, head_y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    )
    # Draw body
    for segment in snake[1:]:
        x, y = segment
        pygame.draw.rect(
            screen, GREEN,
            (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        )


def draw_food(screen, food):
    """Draw food on screen"""
    x, y = food
    pygame.draw.rect(
        screen, RED,
        (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    )


def draw_score(screen, score):
    """Draw score on screen"""
    font = pygame.font.SysFont("Arial", 24)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))


# New: Game sound effects class (supplement audio support)
class GameSounds:
    def __init__(self):
        self.eat_sound = self.load_sound("Assets/audio/effects/eat.wav")
        self.crash_sound = self.load_sound("Assets/audio/effects/crash.wav")

    def load_sound(self, path):
        try:
            return mixer.Sound(path)
        except pygame.error as e:
            print(f"Failed to load sound effect: {e}")
            return None

    def play_eat(self):
        if self.eat_sound:
            self.eat_sound.play()

    def play_crash(self):
        if self.crash_sound:
            self.crash_sound.play()
