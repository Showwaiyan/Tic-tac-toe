# Module import Start
import pygame, sys, os
import gameboard, gameplayer
# Module import End

# Creating object for board and players
board = gameboard.Board((640,640))
player1 = gameplayer.Player("o",(98,102,104))
player2 = gameplayer.Player("x", (237,221,181))

# Player's state if Ture, it will represent one of the player
# and otherwise false, it will represent another player
playerstate = True

# variable to check if someone win or nor
game_over = False

#Set Constant Color
RECT_COLOR = (44,157,153)
BACKGROUND_COLOR = (64,135,132)


x = (1920//2)-(board.get_width()//2)
y = (1080//2)-(board.get_height()//2)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

pygame.init() # pygame package initlize

char_font = pygame.font.SysFont("arial",200) # Font for character represent
screen = pygame.display.set_mode((board.get_width(),board.get_height()), 0, 32) 


screen.fill(BACKGROUND_COLOR)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if board.check_square(event.pos): # Checking the square's value is with a character 
                continue

            # Changing the player's character on CLI array board
            if playerstate: 
                board.change_square(event.pos, player1.give_char()) 
                playerstate = False # Changing state for another player
            else:
                board.change_square(event.pos, player2.give_char()) 
                playerstate = True # Changing state for another player

            if board.test_winning(player1.give_char()):
                print("Player1 win")
                game_over = True
            elif board.test_winning(player2.give_char()):
                print("Player2 win")
                game_over = True


    #Drawing nine square on the screen
    for y in range(0,board.screen_size[1],220):
        for x in range(0,board.screen_size[0],220):
            pygame.draw.rect(screen, RECT_COLOR, ((x,y),(200,200)))

    # Filling Player's character on GUI screen
    for row in range(0,3):
        for colon in range(0,3):
            if board.board[row][colon] == player1.give_char():
                character = char_font.render(player1.give_char(), True, player1.give_color())
                screen.blit(character, board.give_pos(row,colon,character.get_width()//2,character.get_height()//2))
            elif board.board[row][colon] == player2.give_char():
                character = char_font.render(player2.give_char(), True, player2.give_color())
                screen.blit(character, board.give_pos(row,colon,character.get_width()//2,character.get_height()//2))

    pygame.display.update()
