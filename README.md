[简体中文](./Document/README/zh_cn.md)
[繁体中文](./Document/README/zh_tw.md)
[日本語](./Document/README/jp.md)

# Snake Game in Python

A classic Snake game implementation using Python and Pygame library. Control the snake to eat food, grow longer, and avoid collisions with the walls or itself.

## Features

- Classic Snake gameplay mechanics
- Score tracking system
- Increasing difficulty as the snake grows
- Game over detection
- Simple and intuitive controls
- Colorful graphics

## Requirements

- Python 3.6 or higher
- Pygame library

## Installation

See [CONTRIBUTING.md](./CONTRIBUTING.md) for more details.

## How to Play

1. Run the game:
   ```
   python main.py
   ```

2. Use arrow keys to control the snake's direction:
   - Up Arrow: Move up
   - Down Arrow: Move down
   - Left Arrow: Move left
   - Right Arrow: Move right

3. Eat the red food to grow longer and increase your score
4. Avoid hitting the walls or the snake's own body
5. Press 'Q' to quit the game at any time
6. Press 'R' to restart after game over

## Game Mechanics

- The snake moves continuously in the direction it's facing
- Each time the snake eats food, it grows longer by one segment
- The score increases by 10 points for each food eaten
- The game speed increases gradually as the snake grows
- The game ends if the snake hits the wall or its own body

## Project Structure

```
Snakes/                     # Project root directory, overall a Snake game project
├── CHANGELOG.md            # Project change log, records feature changes and fixes for each version
├── CONTRIBUTING.md         # Contribution guidelines, instructing developers on how to contribute to the project
├── LICENSE                 # Project license file, specifying usage rights and restrictions
├── README.md               # Main project documentation, including project introduction, installation and usage instructions
├── main.py                 # Main program entry file, responsible for launching the game and coordinating modules
├── requirements.txt        # Project dependency list, recording required Python libraries and versions
├── tree.py                 # Likely used for tree structure data processing in the game (e.g., snake body structure or level design)
├── .idea/                  # PyCharm IDE project configuration directory
│   ├── Snake.iml           # Project module configuration file
│   ├── jsLibraryMappings.xml # JavaScript library mapping configuration
│   ├── misc.xml            # Miscellaneous configuration
│   ├── modules.xml         # Module structure configuration
│   ├── vcs.xml             # Version control system configuration
│   ├── workspace.xml       # Workspace configuration, records IDE window layout etc.
│   ├── inspectionProfiles/ # Code inspection configuration directory
│   │   ├── Project_Default.xml # Default project inspection configuration
│   │   ├── profiles_settings.xml # Inspection profile settings
├── Assets/                 # Game resources directory, storing various materials
│   ├── index.html          # Likely a web page description or accompanying web interface for the game
│   ├── audio/              # Audio resources directory
│   │   ├── home_menu/      # Main menu related sound effects
│   │   │   ├── confirm.wav # Confirmation action sound effect
│   │   │   ├── select.wav  # Selection action sound effect
│   ├── background/         # Background images directory
│   │   ├── home_menu/      # Main menu background images
│   │   │   ├── menu_cn.png # Chinese menu background
│   │   │   ├── menu_en.png # English menu background
│   │   │   ├── menu_jp.png # Japanese menu background
│   │   │   ├── menu_zh_tw.png # Traditional Chinese menu background
│   ├── icon/               # Icon resources directory
│   │   ├── test.txt        # Icon resource test file (may record icon-related information)
├── Document/               # Project documentation directory, containing multi-language documents
│   ├── CONTRIBUTING/       # Multi-language contribution guidelines
│   │   ├── jp.md           # Japanese contribution guidelines
│   │   ├── zh_cn.md        # Chinese (Simplified) contribution guidelines
│   │   ├── zh_tw.md        # Chinese (Traditional) contribution guidelines
│   ├── README/             # Multi-language documentation
│   │   ├── jp.md           # Japanese documentation
│   │   ├── zh_cn.md        # Chinese (Simplified) documentation
│   │   ├── zh_tw.md        # Chinese (Traditional) documentation
├── Function/               # Game function modules directory
│   ├── game/               # Game core functions directory
│   │   ├── game_core.py    # Implementation of core game logic (e.g., snake movement, collision detection)
│   ├── home_menu/          # Main menu functions directory
│   │   ├── exit_game.py    # Implementation of exit game functionality
│   │   ├── menu_controls.py # Menu control logic (e.g., navigation, selection)
│   │   ├── options.py      # Game options settings functionality (e.g., sound effects, language)
│   │   ├── start_game.py   # Implementation of game launch functionality, responsible for transitioning from menu to game
```

## Contributing

Contributions are welcome! If you have any ideas for improvements or bug fixes, please:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

GPL-3.0 License. See [License here](./LICENSE) for details.

## Acknowledgments

- Pygame community for the excellent game development library
- Classic Snake game creators for the original concept
- All contributors who help improve this project