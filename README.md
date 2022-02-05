# Tic-tac-toe
Tic-tac-toe Game written with python and pygame-library. Two player mode, bot mode and AI mode would be available.

We've played this game since our very young age. In this tiny project, it will have 2vs2-mode, Bot-mode and AI-mode.

## Content
* [Installation](https://github.com/Showwaiyan/Tic-tac-toe/edit/main/README.md#installation)
* [How to run the game](https://github.com/Showwaiyan/Tic-tac-toe/edit/main/README.md#how-to-run-the-game)
* [Game Architecture](https://github.com/Showwaiyan/Tic-tac-toe/edit/main/README.md#game-architecture)

## Installation
This project is written in *python* with *pygame*. 

*If you want to try??* Please download __Python Intepreter__ and __Pygame Module__ first.

You can download *Python* from [Python offical Website](https://www.python.org/downloads/) and *Pygame* from [Pygame offical Website](https://www.pygame.org/download.shtml).

>__NOTE__: Be sure to downlad the *Python3* version and the lasted version of *Pygame*(need version higher than 1.9.5) for your specific operating system. They all support every operating system: Windows, Mac, all Linux distribution.

## How to run the game
### For running 2vs2 mode from Command Line
1. First, clone this repo to your local mechine with __git__ command.
* `git clone https://github.com/Showwaiyan/Tic-tac-toe.git`
2. Go to the __Tic-tac-toe/source_code directory__.
3. Run `main.py` with python3 interpreter.
* `python3 main.py`

### For running Bot mode from Command Line
*coming soon*

### For running AI mode from Command Line
*coming soon*
__
## Game Architecture
![Tic-tac-toeArchicture](https://github.com/Showwaiyan/Tic-tac-toe/blob/main/image/Tic-tac-toe%3CGameArchi%3E.jpeg)

### Main game loop *(main.py)*
The main gameloop code base which is main.py file is composed with `gameboard obj` and `player obj`. It also uses functionality from __Game intro menu__ to display user buttons and Friendly UI to start to play the game. The source of `pygame display code base` and `pygame event handling` in this code base mainly orginze the game. The control structures such as- game start, game over and some feactures are maily managed in this code base.

### Game board class *(gameboard.py)*
Game board class store data and control the all of the process of __Tic-tac-toe__ grid and chose which player to start and checking1 game state base on the board.

### Player class *(gameplayer.py)*
#### Human player class
Child class of Player class and this class is deticated for 2vs2 mode. The class store information such as sign of player, color, etc and process for representing as a human player.
#### Bot player class
Child class of Player class and this class is deticated for Human vs bot mode. The class stroe information about bot(not intelligence properties) and process to pick up a random grid from borad.
#### AI player class
Child class of Player class and this class is deticated for Human vs Ai mode. The class store informatin for __Decision making sstate__ and process to be unbeatable AI player.

### Game intro menu *(gamemenu.py)*
Give the functionalities to __Game main code base__ *(main.py)* to process button properties and text for friendly UI.

### Button class *(gamebutton.py)*
For the purpose of buttons to use in __Game menu__ *(gamemenu.pu)*, button class stroe button position and process that the users click the buttons and others fecture.
