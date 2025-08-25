# Function/options.py
import pygame


def show_options():
    # Initialize pygame
    pygame.init()

    # Set up the window
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game Options")

    # Color definitions
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)

    # Font settings
    font = pygame.font.SysFont("SimHei", 36)
    small_font = pygame.font.SysFont("SimHei", 24)

    # Options content
    options = [
        "Difficulty Speed Settings",
        "Difficulty Settings",
        "Return to Main Menu",
    ]
    selected_option = 0

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(BLACK)

        # Title
        title = font.render("Game Options", True, GREEN)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

        # Draw options
        for i, option in enumerate(options):
            color = WHITE if i == selected_option else (100, 100, 100)
            text = small_font.render(option, True, color)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 200 + i * 50))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    # Handle option selection
                    if selected_option == 2:  # Return to main menu
                        running = False
                elif event.key == pygame.K_ESCAPE:  # Press the ESC key to exit to the main menu
                    running = False

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    show_options()
