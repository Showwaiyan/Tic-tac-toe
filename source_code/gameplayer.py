# Module import start
import random # for bot class usage
# Module import end

# Game Player Class
class Player:

    def __init__(self, char, char_color, win_color):
        # The char represent the player's character 
        # on the board
        self.char = char

        self.char_color = char_color # Character's color
        self.win_color = win_color # Drawing line color

    def get_char(self):
        # getter of player's character
        return self.char

    def get_charcolor(self):
        #getter of player's character-color
        return self.char_color
    
    def get_wincolor(self):
        return self.win_color


class Humanplayer(Player):

    gamemode = "HUMAN" # Mode assign variable

    def __init__(self,char, char_color, win_color):
        super().__init__(char,char_color,win_color)

    def get_gamemode(self):
        # Getter of gamemode
        return self.gamemode


class Botplayer(Player):
    gamemode = "BOT" # Mode assign variable

    def __init__(self,char, char_color, win_color):
        super().__init__(char,char_color,win_color)

    def get_gamemode(self):
        # Getter of gamemode
        return self.gamemode

    def get_pos(self):
        # Give the positon of x and y to the game board
        return [random.randint(0,2),random.randint(0,2)]

class AIplayer(Player):
    pass
