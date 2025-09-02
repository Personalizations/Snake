import pygame
from Function.game.challenge_selector import ChallengeSelector


def start_game():
    screen = pygame.display.get_surface()
    selector = ChallengeSelector(screen)
    selector.run()
