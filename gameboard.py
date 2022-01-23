class Board:
    board = [0,0,0,0,0,0,0,0,0]
  
    def __init__(self,screen_size):
        self.screen_size = screen_size
    
    def check_square(self,mouse_pos):
        # Checking mouse positio is in which square

        if mouse_pos[1] <= 200:
            if mouse_pos[0] <= 200:
                self.board[0] = 1
            elif mouse_pos[0] <= 420:
                self.board[1] = 1
            elif mouse_pos[0] <= 640:
                self.board[2] = 1
        elif mouse_pos[1] <= 420:
            if mouse_pos[0] <= 200:
                self.board[3] = 1
            elif mouse_pos[0] <= 420:
                self.board[4] = 1
            elif mouse_pos[0] <= 640:
                self.board[5] = 1
        elif mouse_pos[1] <= 640:
            if mouse_pos[0] <= 200:
                self.board[6] = 1
            elif mouse_pos[0] <= 420:
                self.board[7] = 1
            elif mouse_pos[0] <= 640:
                self.board[8] = 1

            
