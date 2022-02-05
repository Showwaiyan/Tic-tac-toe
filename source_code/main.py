# Module import Start
import pygame, sys, os
import gameboard, gameplayer, gamemenu
# Module import End

# Creating object for board and players
board = gameboard.Board((640,640))
player1 = gameplayer.Humanplayer("o", (237,221,181), (255,233,179))
player2 = gameplayer.Humanplayer("x", (98,102,104), (74,74,74))

board.first_playerchoose() # Choosing which player to start

#Set Constant Color
RECT_COLOR = (44,157,153)
BACKGROUND_COLOR = (64,135,132)

# Assign the position of screen on the center of the monitor(window)
x = (1920//2)-(board.get_width()//2)
y = (1080//2)-(board.get_height()//2)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

pygame.init() # pygame package initlize

char_font = pygame.font.SysFont("arial",200) # Font for character represent
pygame.display.set_caption("Tic-Tac-Toe")
screen = pygame.display.set_mode((board.get_width(),board.get_height()), 0, 32) 


# Calling game intro surface
if not gamemenu.gameintro_menu(screen, board.get_width(), board.get_height()):
    sys.exit() # If user click quit button

# Showing which player start to play first
gamemenu.playerchose_menu(screen,board.get_width(),board.get_height(),board.get_playerstate())

screen.fill(BACKGROUND_COLOR)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN: 
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.mod & pygame.KMOD_LCTRL: # If press ctrl+c to quit
                if event.key == pygame.K_c:
                    sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not board.get_gameover():
            if board.check_square(event.pos): # Checking the square's value is with a character 
                continue

            # Changing the player's character on CLI array board
            if board.get_playerstate(): 
                board.change_square(event.pos, player1.get_char()) 
                board.set_playerstate(False)# Changing state to another player
            else:
                board.change_square(event.pos, player2.get_char()) 
                board.set_playerstate(True) # Changing state to another player
            
            # Checking which player win
            if board.test_winning(player1.get_char()):
                board.set_gameover(True)
            elif board.test_winning(player2.get_char()):
                board.set_gameover(True)

            # Checking the board is completely filled or not
            if board.check_gameboard():
                board.set_gameover(True)

        # Restarting the game
        elif event.type == pygame.KEYDOWN and board.get_gameover():
            if event.key == pygame.K_SPACE:
                board.set_gameover(False)
                board.restart_gameboard()
                # Every time restart the game - showing which player start to play first
                gamemenu.playerchose_menu(screen,board.get_width(),board.get_height(),board.get_playerstate())
                screen.fill(BACKGROUND_COLOR)
            

    #Drawing nine square on the screen
    for y in range(0,board.screen_size[1],220):
        for x in range(0,board.screen_size[0],220):
            pygame.draw.rect(screen, RECT_COLOR, ((x,y),(200,200)))

    # Filling Player's character on GUI screen
    for row in range(0,3):
        for colon in range(0,3):
            if board.board[row][colon] == player1.get_char():
                character = char_font.render(player1.get_char(), True, player1.get_charcolor())
                screen.blit(character, board.get_pos(row,colon,character.get_width()//2,character.get_height()//2))
            elif board.board[row][colon] == player2.get_char():
                character = char_font.render(player2.get_char(), True, player2.get_charcolor())
                screen.blit(character, board.get_pos(row,colon,character.get_width()//2,character.get_height()//2))


    # Drawing winnig line on GUI
    if board.get_gameover():
        if not board.get_playerstate():
            pygame.draw.lines(screen, player1.get_wincolor(), False, board.get_winningline_pos(), board.get_linewidth())
        elif board.get_playerstate():
            pygame.draw.lines(screen, player2.get_wincolor(), False, board.get_winningline_pos(), board.get_linewidth())
                        
    pygame.display.update()
