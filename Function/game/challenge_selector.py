import pygame
import sys
import math
from pygame import mixer
from Function.game.level_challenge import LevelChallenge
from Function.game.infinite_challenge import InfiniteChallenge


def init_background_music():
    try:
        music_path = "Assets/audio/home_menu/background_music.wav"
        mixer.music.load(music_path)
        mixer.music.set_volume(0.3)
        mixer.music.play(-1)
        return True
    except Exception as e:
        print(f"Music loading failed on the challenge selection interface: {e}")
        return False


class ChallengeSelector:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.font = pygame.font.SysFont("SimHei", 36)
        self.small_font = pygame.font.SysFont("SimHei", 24)
        self.options = ["Level Challenge", "Infinite Challenge", "Return to Main Menu"]
        self.selected_option = 0
        self.running = True
        self.bg_music = init_background_music()

        try:
            self.select_sound = mixer.Sound("Assets/audio/home_menu/select.wav")
        except:
            class DummySound:
                def play(self): pass

            self.select_sound = DummySound()

    def handle_events(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_hovered = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                    self.select_sound.play()
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                    self.select_sound.play()
                elif event.key == pygame.K_RETURN:
                    mixer.music.stop()
                    self.select_option()
                elif event.key == pygame.K_ESCAPE:
                    mixer.music.stop()
                    self.running = False
            elif event.type == pygame.MOUSEMOTION:
                for i in range(len(self.options)):
                    option_rect = self.get_option_rect(i)
                    if option_rect.collidepoint(mouse_pos):
                        if self.selected_option != i:
                            self.selected_option = i
                            self.select_sound.play()
                        mouse_hovered = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i in range(len(self.options)):
                    if self.get_option_rect(i).collidepoint(mouse_pos):
                        self.selected_option = i
                        mixer.music.stop()
                        self.select_option()
                        break

    def get_option_rect(self, index):
        text = self.small_font.render(self.options[index], True, (255, 255, 255))
        x = self.width // 2 - text.get_width() // 2
        y = 200 + index * 50
        return pygame.Rect(x, y, text.get_width(), text.get_height())

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
            if i == self.selected_option:
                scale = 1.0 + (abs(math.sin(pygame.time.get_ticks() / 300)) * 0.1)
                text = self.small_font.render(option, True, (255, 255, 255))
                scaled_text = pygame.transform.scale(
                    text,
                    (int(text.get_width() * scale), int(text.get_height() * scale))
                )
                x = self.width // 2 - scaled_text.get_width() // 2
                y = 200 + i * 50
                self.screen.blit(scaled_text, (x, y))
            else:
                color = (100, 100, 100)
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
        mixer.music.stop()