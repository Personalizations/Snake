import pygame
import sys
from Function.game.level_challenge import LevelChallenge
from Function.game.infinite_challenge import InfiniteChallenge


class ChallengeSelector:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.font = pygame.font.SysFont("SimHei", 36)
        self.small_font = pygame.font.SysFont("SimHei", 24)
        self.options = ["Level Challenge", "Infinite Challenge", "Return to Main Menu"]
        self.selected_option = 0
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(
                        self.options
                    )
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(
                        self.options
                    )
                elif event.key == pygame.K_RETURN:
                    self.select_option()
                elif event.key == pygame.K_ESCAPE:
                    self.running = False

    def select_option(self):
        if self.selected_option == 0:
            # Level Challenge
            level_challenge = LevelChallenge(self.screen)
            level_challenge.run()
        elif self.selected_option == 1:
            # Infinite Challenge
            infinite_challenge = InfiniteChallenge(self.screen)
            infinite_challenge.run()
        elif self.selected_option == 2:
            # Return to Main Menu
            self.running = False

    def render(self):
        self.screen.fill((0, 0, 0))
        title = self.font.render("Select Challenge Mode", True, (0, 255, 0))
        self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 100))

        for i, option in enumerate(self.options):
            color = (255, 255, 255) if i == self.selected_option else (100, 100, 100)
            text = self.small_font.render(option, True, color)
            self.screen.blit(
                text, (self.width // 2 - text.get_width() // 2, 200 + i * 50)
            )

        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            self.handle_events()
            self.render()
            clock.tick(30)
