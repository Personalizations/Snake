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
   python snake_game.py
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
snake/
├── snake_game.py       # Main game file
├── assets/             # Game assets (images, sounds)
├── Document/           # Documentation directory
│  ├── README/          # Multi-language README documents
│  │  ├── zh_cn.md      # Simplified Chinese README
│  │  ├── zh_tw.md      # Traditional Chinese README
│  │  └── jp.md         # Japanese README
│  └── CONTRIBUTING/    # MultiMulti-language contribution guidelines
│     ├── zh_cn.md      # Simplified Chinese contribution guidelines
│     ├── zh_tw.md      # Traditional Chinese contribution guidelines
│     └── jp.md         # Japanese contribution guidelines
├── LICENSE             # GPL-3.0 License
├── README.md           # Main README file (English)
├── CONTRIBUTING.md     # Main contribution guidelines file (English)
├── requirements.txt    # Project dependencies
└── .idea/              # IDE configuration files
    ├── vcs.xml         # Version control configuration
    ├── modules.xml     # Module configuration
    ├── .gitignore      # IDE-specific ignore file
    ├── jsLibraryMappings.xml  # JavaScript library mappings
    ├── inspectionProfiles/    # Inspection configuration files
    │  └── Project_Default.xml # Default project inspection configuration
    └── misc.xml        # Other miscellaneous configurations
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