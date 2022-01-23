class Board:
    board = [0,0,0,0,0,0,0,0,0]

    def __init__(self,screen_size):
        self.screen_size = screen_size
    
    def change_square(self,mouse_pos, char):
        # Checking mouse positio is in which square

        if mouse_pos[1] <= 200:
            if mouse_pos[0] <= 200:
                self.board[0] = char if self.board[0] == 0 else self.board[0]
            elif mouse_pos[0] <= 420:
                self.board[1] = char if self.board[1] == 0 else self.board[1]
            elif mouse_pos[0] <= 640:
                self.board[2] = char if self.board[2] == 0 else self.board[2]
        elif mouse_pos[1] <= 420:
            if mouse_pos[0] <= 200:
                self.board[3] = char if self.board[3] == 0 else self.board[3]
            elif mouse_pos[0] <= 420:
                self.board[4] = char if self.board[4] == 0 else self.board[4]
            elif mouse_pos[0] <= 640:
                self.board[5] = char if self.board[5] == 0 else self.board[5]
        elif mouse_pos[1] <= 640:
            if mouse_pos[0] <= 200:
                self.board[6] = char if self.board[6] == 0 else self.board[6]
            elif mouse_pos[0] <= 420:
                self.board[7] = char if self.board[7] == 0 else self.board[7]
            elif mouse_pos[0] <= 640:
                self.board[8] = char if self.board[8] == 0 else self.board[8]

    def give_pos(self,square,text_width,text_hight):
        if square == 0:
            return (100-text_width,100-text_hight)
