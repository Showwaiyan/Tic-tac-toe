class Board:
    board = [[0,0,0]
            ,[0,0,0]
            ,[0,0,0]]

    def __init__(self,screen_size):
        self.screen_size = screen_size
    
    def change_square(self,mouse_pos, char):
        # Checking mouse positio is in which square

        colon = int(mouse_pos[0] // 220)
        row = int(mouse_pos[1] // 220)
        self.board[row][colon] = char if self.board[row][colon] == 0 else self.board[row][colon]

    def check_square(self,mouse_pos):
       colon = int(mouse_pos[0] // 220)
       row = int(mouse_pos[1] // 220)
       return (self.board[row][colon] != 0)
  
        
    

    def give_pos(self,row,colon,text_width,text_height):
       x = ((colon * 220) + 100) - text_width
       y = ((row * 220) + 100) - text_height
       return (x,y)
