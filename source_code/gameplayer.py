# Game Player Class
class Player:

    def __init__(self, char, char_color, win_color):
        # The char represent the player's character 
        # on the board
        self.char = char

        self.char_color = char_color # Character's color
        self.win_color = win_color

    def get_char(self):
        # getter of player's character
        return self.char

    def get_charcolor(self):
        #getter of player's character-color
        return self.char_color
    
    def get_wincolor(self):
        return self.win_color
