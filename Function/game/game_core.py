import pygame
import random
from Function.home_menu.exit_game import exit_game

# Game constants (migrated from main.py)
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


def draw_snake(screen, snake):
    """Draw the snake"""
    # Draw snake head
    head_x, head_y = snake[0]
    pygame.draw.rect(
        screen,
        DARK_GREEN,
        (head_x * GRID_SIZE, head_y * GRID_SIZE, GRID_SIZE, GRID_SIZE),
    )

    # Draw snake body
    for segment in snake[1:]:
        x, y = segment
        pygame.draw.rect(
            screen,
            GREEN,
            (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        )


def draw_food(screen, food):
    """Draw the food"""
    x, y = food
    pygame.draw.rect(
        screen,
        RED,
        (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    )


def generate_food(snake):
    """Generate food, ensuring it doesn't appear on the snake"""
    while True:
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        food = (x, y)
        if food not in snake:
            return food


def show_message(screen, message, color, size, y_offset=0):
    """Display game messages"""
    font = pygame.font.SysFont("SimHei", size)
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(text, text_rect)


def game_loop(screen):
    """Main game loop"""
    FPS = 10  # Initial speed

    # Initialize snake position and direction
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    direction = RIGHT
    next_direction = direction

    # Generate initial food
    food = generate_food(snake)

    # Score
    score = 0

    # Game state
    running = True
    game_over = False

    clock = pygame.time.Clock()

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # Press Q to exit game
                    return

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

            # Check for self-collision
            if new_head in snake:
                game_over = True

            # Add new head to snake
            snake.insert(0, new_head)

            # Check if food is eaten
            if new_head == food:
                score += 1
                food = generate_food(snake)
                # Increase speed every 5 points
                if score % 5 == 0:
                    FPS += 1
            else:
                # Remove tail if no food eaten (maintain length)
                snake.pop()

        # Drawing
        screen.fill(BLACK)
        draw_snake(screen, snake)
        draw_food(screen, food)

        # Display score
        font = pygame.font.SysFont("SimHei", 24)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Display game over messages
        if game_over:
            show_message(screen, "Game Over!", RED, 48)
            show_message(screen, f"Final Score: {score}", WHITE, 36, 50)
            show_message(screen, "Press any key to restart", WHITE, 24, 100)
            show_message(screen, "Press Q to return to menu", WHITE, 24, 150)

        # Update display
        pygame.display.flip()

        # Control game speed
        clock.tick(FPS)
