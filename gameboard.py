# The Whole Game Board Class
class Board:
    board = [[0,0,0]   # Multidimension List for 
            ,[0,0,0]   # accessing data as a 
            ,[0,0,0]]  # Command line preference
    BOARD_ROW = 3
    BOARD_COLON = 3

    def __init__(self,screen_size):
        #size of the game baord screen
        self.screen_size = screen_size
    

    def get_width(self):
        # Getter of screen size width
        return self.screen_size[0]

    def get_height(self):
        # Getter of screen size height
        return self.screen_size[1]


    def change_square(self,mouse_pos, char):
        # Determine the square from the position of mouse
        
        # Due to the 200x200 square
        # divided the mouse position x and y by 220,
        # which is the unit of square and line width
        # and get the round floor interger which is represent as a
        # multidimensino array indexs
        colon = int(mouse_pos[0] // 220)
        row = int(mouse_pos[1] // 220)

        # Checking the array is fill or not
        # if the array already has a value
        # Skip the step of assign
        self.board[row][colon] = char if self.board[row][colon] == 0 else self.board[row][colon]

    def check_square(self,mouse_pos):
       # Checking the square on screen is drew or ot

       # If the user click the square that has already value with character
       # this function return the positon of x and y's square has been draw
       # and not to count this as a drawing character step
       colon = int(mouse_pos[0] // 220)
       row = int(mouse_pos[1] // 220)
       return (self.board[row][colon] != 0)
  
        
    def give_pos(self,row,colon,text_width,text_height):
       # Giving the which? sqaure's center base on the mouse position of x and y
       # to draw the character

       x = ((colon * 220) + 100) - text_width
       y = ((row * 220) + 100) - text_height
       return (x,y)

    def test_winning(self,player):
       win_state = 0 # State value if value get 3, the player win

       # Horizontal row test start
       for y in range(self.BOARD_ROW):
           for x in range(self.BOARD_COLON):
               if self.board[x][y] == player:
                   win_state += 1
                   continue
           if win_state == 3:
               return True
           else:
               win_state = 0
        # Horizontal row test end

        # Vertical colon test start
       for x in range(self.BOARD_COLON):
           for y in range(self.BOARD_ROW):
               if self.board[x][y] == player:
                    win_state += 1
                    continue
           if win_state == 3:
               return True
           else:
               win_state = 0
        # Vertical colon test end

        # Acending cross test start
       for i in range(self.BOARD_ROW): # We can use both board row or colon
           if self.board[i][i] == player:
               win_state += 1
               continue
            
           if win_state == 3:
               return True
           else:
               break
        # Acending cross test end

        # Desending cross test start
       for i in range(self.BOARD_COLON): # We can use both board row or colon
           if self.board[i][2-i] == player:
               win_state += 1
               continue

           if win_state == 3:
               return True
           else:
               break
        # Desending cross test end
                   
       return False 
