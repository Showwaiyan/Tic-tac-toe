# Game Player Class
class Player:

    def __init__(self, char, color):
        # The char represent the player's character 
        # on the board
        self.char = char

        self.color = color # Character's color

    def give_char(self):
        # getter of player's character
        return self.char

    def give_color(self):
        #getter of player's character-color
        return self.color
