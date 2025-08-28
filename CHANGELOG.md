### 2.1

- The last item's connector line was not correctly displayed as └──.
 Improvements:
 - A two-pass traversal strategy is now used, first collecting all directory information and then generating the directory tree.
 - Improved indentation logic to more accurately calculate connector lines at each level.
 - Correctly use the └── symbol for the last subdirectory and last file in each directory.
 - Fixed an issue with connector line display for deep directories.

- the generated directory tree will have the correct hierarchical relationships and connecting lines

 - improved hierarchy calculation to more accurately determine directory depth using relative paths
 - use the "└──" symbol for the last file/directory and "├──" for others, making the structure clearer
 - optimized indentation logic to ensure proper alignment of connecting lines
 - fix an issue with root directory display


### 2.0

- fix the issue that the Traditional Chinese version of the README document could not be redirected
- fix the multi-language translation issue of README document

### 1.9

- optimize the multi-language jump display of the project structure --- Simplified Chinese
- fix：optimize the multi-language jump display of the project structure --- Traditional Chinese
- optimize the multi-language jump display of the project structure --- Traditional Chinese
- optimize the multi-language jump display of the project structure --- Japanese
- optimize the display of project structure. previously, tree.py was added to generate the structure.
- generate a structure tree

### 1.8

- fix file code format
- add selection page and press ESC key to exit to the main menu
- repair Instructions Document Format
- add Press 'ESC' to exit the current page
- add one-key Q key detection Press Q to exit the game

### 1.7

- add background music to the start menu
- add start menu background music
- add music to the game background
- add background_music.wav for later

### 1.6

- fix the error in the project structure directory
- fix project structure directory comment error
- add the results of the project structure generation script
- add a script to generate the project structure

### 1.5

- restructured the project using the Project Tree Generator and added more comprehensive Japanese comments.
- restructured the project using the Project Tree Generator and added more comprehensive Traditional Chinese annotations.
- restructured the project using the Project Tree Generator and added more comprehensive Chinese comments.
- restructured the project using the Project Tree Generator and added more comprehensive English comments.

### 1.4

- after adding menu background, the button is not in the frame
- fix the issue where the background of menu en.png could not be displayed after moving
- move menu cn.png menu en.png menu jp.png menu zh tw.png from Assets/background to Assets/background/home_menu folder

### 1.3

- submit menu_jp.png to add more styles to the background
- submit menu_zh_tw.png to add more styles to the background
- submit menu_cn.png to add more styles to the background

### 1.2

- fix the issue that the start menu does not display the background image
- modify the loading of the background image to be delayed until the MenuSystem is initialized

### 1.1

- leave Snake Game in the Start Menu blank
- fix the start menu bar error issue
- add menu start background image
- import menu_en.png start menu background image
- prepare to add background images to the background later
- updated click version to 8.2.2

### 1.0

- add project structure for game_core.py
- refactor the game rendering function of main.py to only render the menu bar

### 0.9

- add the game_core.py file to prepare for the subsequent main.py slimming down
- fix the issue of no sound when selecting menu bar
- project structure with menu_controls.py added

### 0.8

- fix menu_controls.py error
- import menu_controls.py into main.py
- optimize the implementation of start menu option response and feedback function

### 0.7

- add confirmation sound effects and selection sound effects to the project structure directory of README.md in other languages
- add confirmation sound effects and selection sound effects to the project structure directory of README.md
- optimize the code formatting of Traditional Chinese CONTRIBUTING.md
- optimize the code formatting of Simplified Chinese CONTRIBUTING.md
- optimize the code formatting of Japanese CONTRIBUTING.md
- optimize the code formatting of CONTRIBUTING.md

### 0.6

- move the sound effects to the home_menu folder
- add menu bar confirmation sound effect
- add menu bar selection sound effect
- use black . command to format the file
- fix errors in contribution documentation

### 0.5

- project structure for adding functionality jp.md
- restructure the README jp.md project
- project structure for adding functionality zh_tw.md
- restructure the README zh_tw.md project

### 0.4

- project structure for adding functionality zh_cn.md
- restructure the README zh_cn.md project
- project structure for adding functionality
- restructure the README project

### 0.3

- add project structure
- optimized the path guidance of README.md and contribution documents
- add resource folder

### 0.2

- add support for library dependencies
- add documentation multi-language support
- add README.md multi-language support

### 0.1

- submit basic functions and some required files as a whole