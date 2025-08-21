import pygame
from Function.home_menu.start_game import start_game
from Function.home_menu.options import show_options
from Function.home_menu.exit_game import exit_game
from Function.home_menu.menu_controls import MenuSystem

# Initialize Pygame
pygame.init()

# Window constants
WIDTH, HEIGHT = 800, 600  # Game window dimensions

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


def main_menu():
    """Main menu function - uses menu system from menu_controls.py"""
    # Define menu items (text and corresponding actions)
    menu_options = [
        ("Start Game", start_game),
        ("Options", show_options),
        ("Exit Game", exit_game)
    ]

    # Create menu system instance
    menu = MenuSystem(
        screen_width=WIDTH,
        screen_height=HEIGHT,
        title="Snake Game",
        options_list=menu_options
    )

    clock = pygame.time.Clock()
    running = True

    while running:
        # Handle events
        menu.handle_events()

        # Update menu state
        menu.update()

        # Render menu
        menu.render(screen)

        # Update display
        pygame.display.flip()
        clock.tick(60)

    exit_game()


if __name__ == "__main__":
    main_menu()  # Program entry point is main menu
