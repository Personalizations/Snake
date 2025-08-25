import pygame
import sys
import math
from pygame import mixer

# Initialize audio system
mixer.init()

# Load menu sound effects and background music (ensure files exist or modify paths)
try:
    SELECT_SOUND = mixer.Sound("Assets/audio/home_menu/select.wav")
    CONFIRM_SOUND = mixer.Sound("Assets/audio/home_menu/confirm.wav")
    MENU_BG_MUSIC = "Assets/audio/home_menu/background_music.wav"
except:
    # Silent placeholder when sound loading fails
    class DummySound:
        def play(self):
            pass

    SELECT_SOUND = DummySound()
    CONFIRM_SOUND = DummySound()
    MENU_BG_MUSIC = None

class BackgroundMusicHandler:
    """Background music handling class"""
    def __init__(self, music_path):
        self.music_path = music_path
        self.volume = 0.3  # Menu background music volume (lower than game music)
        self.is_playing = False

    def start(self):
        """Start playing background music (looping)"""
        if self.music_path and not self.is_playing:
            try:
                mixer.music.load(self.music_path)
                mixer.music.set_volume(self.volume)
                mixer.music.play(-1)  # -1 indicates infinite loop
                self.is_playing = True
            except Exception as e:
                print(f"Menu background music playback failed: {e}")

    def stop(self):
        """Stop background music"""
        if self.is_playing:
            mixer.music.stop()
            self.is_playing = False

class MenuOption:
    """Class representing a single menu option"""
    def __init__(
            self,
            text,
            action=None,
            font=None,
            color=(255, 255, 255),
            hover_color=(0, 255, 0),
            y_pos=0,
    ):
        self.text = text
        self.action = action  # Function to execute when selected
        self.font = font or pygame.font.SysFont("Arial", 36)
        self.color = color
        self.hover_color = hover_color
        self.y_pos = y_pos
        self.is_selected = False
        self.text_surface = None
        self.rect = None
        self.animation_offset = 0  # For selection animation
        self.animation_speed = 0.5  # Animation speed

    def update(self):
        """Update option state and animation"""
        if self.is_selected:
            # Breathing effect when selected
            self.animation_offset = (self.animation_offset + self.animation_speed) % (
                    2 * math.pi
            )
        else:
            self.animation_offset = 0

    def render(self, screen, center_x):
        """Draw the option with selection effects"""
        color = self.hover_color if self.is_selected else self.color
        self.text_surface = self.font.render(self.text, True, color)

        # Add scaling effect when selected
        scale = (
            1.0 + (abs(math.sin(self.animation_offset)) * 0.1)
            if self.is_selected
            else 1.0
        )
        scaled_surface = pygame.transform.scale(
            self.text_surface,
            (
                int(self.text_surface.get_width() * scale),
                int(self.text_surface.get_height() * scale),
            ),
        )

        self.rect = scaled_surface.get_rect(center=(center_x, self.y_pos))
        screen.blit(scaled_surface, self.rect)

    def check_hover(self, pos):
        """Check if mouse is hovering over the option"""
        if self.rect and self.rect.collidepoint(pos):
            if not self.is_selected:
                self.is_selected = True
                SELECT_SOUND.play()
                return True
        return False


class MenuSystem:
    """Main menu system handling navigation and rendering"""
    def __init__(self, screen_width, screen_height, title, options_list):
        self.width = screen_width
        self.height = screen_height
        self.title = title
        self.options = []
        self.selected_index = 0
        self.title_font = pygame.font.SysFont("Arial", 48)
        self.title_color = (0, 255, 0)
        self.bg_color = (0, 0, 0)  # Background color (used if image fails to load)

        # Initialize background music handler
        self.bg_music = BackgroundMusicHandler(MENU_BG_MUSIC)
        self.bg_music.start()  # Start background music

        # Adjust background image to fit screen
        self.background = None
        try:
            # Ensure path is correct (adjust according to actual location)
            img = pygame.image.load("Assets/background/home_menu/menu_en.png").convert()
            self.background = pygame.transform.scale(img, (self.width, self.height))
        except Exception as e:
            print(f"Background image loading failed: {e}")
            self.background = None

        # Create menu options
        self._create_options(options_list)

    def _create_options(self, options_list):
        """Create menu options from the provided list"""
        start_y = self.height // 2.1
        spacing = 70

        for i, (text, action) in enumerate(options_list):
            y_pos = start_y + i * spacing
            option = MenuOption(text=text, action=action, y_pos=y_pos)
            self.options.append(option)

        # Select first option by default
        if self.options:
            self.options[0].is_selected = True

    def handle_events(self):
        """Handle user input events for menu navigation"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.bg_music.stop()  # Stop music when exiting
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self._navigate(-1)
                elif event.key == pygame.K_DOWN:
                    self._navigate(1)
                elif event.key == pygame.K_RETURN:
                    self._select_option()
                elif event.key == pygame.K_ESCAPE:
                    # Exit game or return to previous menu
                    if len(self.options) > 2 and self.options[-1].text == "Exit Game":
                        self.bg_music.stop()  # Stop music when exiting
                        self.options[-1].action()

            elif event.type == pygame.MOUSEMOTION:
                # Mouse hover navigation
                pos = pygame.mouse.get_pos()
                hovered = False
                for i, option in enumerate(self.options):
                    if option.check_hover(pos):
                        self._set_selected(i)
                        hovered = True
                if not hovered:
                    # Maintain current selection when mouse is outside all options
                    self._update_selection()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Mouse click selection
                pos = pygame.mouse.get_pos()
                for option in self.options:
                    if option.rect and option.rect.collidepoint(pos):
                        self._set_selected(self.options.index(option))
                        self._select_option()
                        break

    def _navigate(self, direction):
        """Navigate to previous/next option"""
        self.options[self.selected_index].is_selected = False
        self.selected_index = (self.selected_index + direction) % len(self.options)
        self.options[self.selected_index].is_selected = True
        SELECT_SOUND.play()

    def _set_selected(self, index):
        """Set the selected option by index"""
        if 0 <= index < len(self.options):
            self.options[self.selected_index].is_selected = False
            self.selected_index = index
            self.options[self.selected_index].is_selected = True

    def _update_selection(self):
        """Update selection state for all options"""
        for i, option in enumerate(self.options):
            option.is_selected = i == self.selected_index

    def _select_option(self):
        """Select current option and execute its action"""
        CONFIRM_SOUND.play()
        if self.options[self.selected_index].action:
            # Add visual feedback for selection confirmation
            self._draw_confirmation_feedback()
            pygame.display.flip()
            pygame.time.delay(200)  # Short delay for better feedback
            self.bg_music.stop()  # Stop menu music before entering submenu or game
            self.options[self.selected_index].action()
            self.bg_music.start()  # Restart music when returning from submenu

    def _draw_confirmation_feedback(self):
        """Draw visual feedback for selection confirmation"""
        option = self.options[self.selected_index]
        s = pygame.Surface(
            (option.rect.width + 40, option.rect.height + 20), pygame.SRCALPHA
        )
        pygame.draw.rect(s, (0, 255, 0, 50), s.get_rect(), border_radius=5)
        screen_pos = (
            option.rect.centerx - s.get_width() // 2,
            option.rect.centery - s.get_height() // 2,
        )
        pygame.display.get_surface().blit(s, screen_pos)

    def update(self):
        """Update all option states"""
        for option in self.options:
            option.update()

    def render(self, screen):
        """Draw the entire menu"""
        # Draw background image, use solid color if loading fails
        if self.background:
            screen.blit(self.background, (0, 0))
        else:
            screen.fill(self.bg_color)

        # Draw title
        title_surface = self.title_font.render(self.title, True, self.title_color)
        title_rect = title_surface.get_rect(center=(self.width // 2, 100))
        screen.blit(title_surface, title_rect)

        # Draw options
        for option in self.options:
            option.render(screen, self.width // 2)