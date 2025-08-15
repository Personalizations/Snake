import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 800, 600  # Game window size
GRID_SIZE = 20  # Grid size (each unit represents 1cm)
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Color definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)  # Snake body
RED = (255, 0, 0)    # Food
DARK_GREEN = (0, 200, 0)  # Snake head

# Direction constants
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock to control game speed
clock = pygame.time.Clock()
FPS = 10  # Initial speed


def draw_snake(snake):
    """Draw the snake"""
    # Draw snake head
    head_x, head_y = snake[0]
    pygame.draw.rect(screen, DARK_GREEN,
                     (head_x * GRID_SIZE, head_y * GRID_SIZE,
                      GRID_SIZE, GRID_SIZE))

    # Draw snake body
    for segment in snake[1:]:
        x, y = segment
        pygame.draw.rect(screen, GREEN,
                         (x * GRID_SIZE, y * GRID_SIZE,
                          GRID_SIZE, GRID_SIZE))


def draw_food(food):
    """Draw the food"""
    x, y = food
    pygame.draw.rect(screen, RED,
                     (x * GRID_SIZE, y * GRID_SIZE,
                      GRID_SIZE, GRID_SIZE))


def generate_food(snake):
    """Generate food, ensuring it doesn't appear on the snake"""
    while True:
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        food = (x, y)
        if food not in snake:
            return food


def show_message(message, color, size, y_offset=0):
    """Display game messages"""
    font = pygame.font.SysFont("SimHei", size)
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(text, text_rect)


def main():
    """Main game function"""
    global FPS  # Declare FPS as global to modify within function
    # Initialize snake position and direction
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    direction = RIGHT
    next_direction = direction

    # Generate initial food
    food = generate_food(snake)

    # Score
    score = 0

    # Main game loop
    running = True
    game_over = False

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if game_over:
                    # Press any key to restart after game over
                    game_over = False
                    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
                    direction = RIGHT
                    next_direction = direction
                    food = generate_food(snake)
                    score = 0
                    FPS = 10  # Reset speed
                    continue

                # Handle direction keys
                if event.key == pygame.K_UP and direction != DOWN:
                    next_direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    next_direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    next_direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    next_direction = RIGHT

        if not game_over:
            # Update direction
            direction = next_direction

            # Calculate new head position
            head_x, head_y = snake[0]
            dx, dy = direction
            new_head = ((head_x + dx) % GRID_WIDTH, (head_y + dy) % GRID_HEIGHT)

            # Check if snake hits itself
            if new_head in snake:
                game_over = True

            # Add new head to snake body
            snake.insert(0, new_head)

            # Check if food is eaten
            if new_head == food:
                score += 1
                food = generate_food(snake)
                # Increase speed every 5 points
                if score % 5 == 0:
                    FPS += 1
            else:
                # If no food eaten, remove tail (maintain length)
                snake.pop()

        # Drawing
        screen.fill(BLACK)
        draw_snake(snake)
        draw_food(food)

        # Display score
        font = pygame.font.SysFont("SimHei", 24)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Display game over message
        if game_over:
            show_message("Game Over!", RED, 48)
            show_message(f"Final Score: {score}", WHITE, 36, 50)
            show_message("Press any key to restart", WHITE, 24, 100)

        # Update display
        pygame.display.flip()

        # Control game speed
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()