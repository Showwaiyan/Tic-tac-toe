# Module import start
import random
# Module import end

# The Whole Game Board Class
class Board:
    board = [[0,0,0]   # Multidimension List for 
            ,[0,0,0]   # accessing data as a 
            ,[0,0,0]]  # Command line preference
    BOARD_ROW = 3
    BOARD_COLON = 3
    winning_linepos = [[0,0],[0,0]] # To draw line position on GUI screen
    winning_linewidth = 0 # To draw line width on GUI screen

    # Player's state if Ture, it will represent one of the player
    # and otherwise false, it will represent another player
    playerstate = None


    def __init__(self,screen_size):
        #size of the game baord screen
        self.screen_size = screen_size
    

    def get_width(self):
        # Getter of screen size width
        return self.screen_size[0]

    def get_height(self):
        # Getter of screen size height
        return self.screen_size[1]

    def get_winningline_pos(self):
        # Getter of winning line position
        return self.winning_linepos

    def get_linewidth(self):
        # Getter of winning line width
        return self.winning_linewidth

    
    def restart_gameboard(self):
        # Restart the game
        self.board = [[0,0,0]
                     ,[0,0,0]
                     ,[0,0,0]]
        self.winning_linepos = [[0,0],[0,0]]        
        self.winning_linewidth = 0


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
       # Checking the square on screen is drew or not

       # If the user click the square that has already value with character
       # this function return the positon of x and y's square has been draw
       # and not to count this as a drawing character step
       colon = int(mouse_pos[0] // 220)
       row = int(mouse_pos[1] // 220)
       return (self.board[row][colon] != 0)
  
        
    def get_pos(self,row,colon,text_width,text_height):
       # Giving the which? sqaure's center base on the mouse position of x and y
       # to draw the character

       x = ((colon * 220) + 100) - text_width
       y = ((row * 220) + 100) - text_height
       return (x,y)


    def horizontal_test(self,player):
        #Cheking horizontal row if the player win or not
        win_state = 0
       
        for y in range(self.BOARD_ROW):
           for x in range(self.BOARD_COLON):
               if self.board[y][x] == player:
                   win_state += 1
           if win_state == 3:
               self.winning_linepos = [
                        (40,y*220 +110),
                        (self.get_width()-40,y*220 +110)]
               self.winning_linewidth = 13
               return True
           else:
               win_state = 0
        return False

    def vertical_test(self,player):
        #Checkingg vertical colon if player win or not
        win_state = 0

        for y in range(self.BOARD_COLON):
            for x in range(self.BOARD_ROW):
                if self.board[x][y] == player:
                    win_state += 1
            if win_state == 3:
                self.winning_linepos = [
                        (y*220 +100,40),
                        (y*220 +100,self.get_height()-20)]
                self.winning_linewidth = 13
                return True
            else:
                win_state = 0
        return False
    
    def des_cross_test(self,player):
        # Checking descending cross section if player is win or not
        win_state = 0

        for i in range(self.BOARD_ROW): # We can use both board row and colon
            if self.board[i][i] == player:
                win_state += 1
        if win_state == 3:
            self.winning_linepos = [
                    (40,50),
                    (self.get_width()-40, self.get_height()-30)]
            self.winning_linewidth = 20
            return True
        else:
            return False

    def asc_cross_test(self,player):
        # Checking asceding cross section if player is win or not
        win_state = 0

        for i in range(self.BOARD_COLON): # We can use both board row and colon
            if self.board[i][2-i] == player:
                win_state += 1
        if win_state == 3:
            self.winning_linepos = [
                    (40,self.get_height()-30),
                    (self.get_width() - 30,40)]
            self.winning_linewidth = 20
            return True
        else:
            return False


    def test_winning(self,player):
       # Checking every position of square if player win or not

       if self.horizontal_test(player):
           return True
       elif self.vertical_test(player):
           return True
       elif self.asc_cross_test(player):
           return True
       elif self.des_cross_test(player):
           return True
       else:
           return False

    def check_gameboard(self):
       # Checking the gameboard is fully filled with character or not
       for x in range(self.BOARD_COLON):
           for y in range(self.BOARD_ROW):
               if self.board[x][y] == 0:
                   return False
       return True


    def first_playerchoose(self):
        # Choosing which player start to play
        if random.randint(0,1) == 0:
            self.playerstate = False
        else:
            self.playerstate = True

    def get_playerstate(self):
        # Getter of player state
        return self.playerstate

    def set_playerstate(self, flag):
        # Setter of plaer state
        self.playerstate = flag


