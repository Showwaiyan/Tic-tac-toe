import pygame, sys
import gameboard, gameplayer

board = gameboard.Board((640,640))
player1 = gameplayer.Player("o")
player2 = gameplayer.Player("x")
playerstate = True

RECT_COLOR = (44,157,153)
BACKGROUND_COLOR = (64,135,132)

pygame.init()

font = pygame.font.SysFont("arial",200)
screen = pygame.display.set_mode(board.screen_size, 0, 32)


screen.fill(BACKGROUND_COLOR)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if board.check_square(event.pos):
                continue
            if playerstate:
                board.change_square(event.pos, player1.give_char())
                playerstate = False
            else:
                board.change_square(event.pos, player2.give_char())
                playerstate = True


    #Drawing nine square on the screen
    for y in range(0,board.screen_size[1],220):
        for x in range(0,board.screen_size[0],220):
            pygame.draw.rect(screen, RECT_COLOR, ((x,y),(200,200)))

    for row in range(0,3):
        for colon in range(0,3):
            if board.board[row][colon] == player1.give_char():
                character = font.render(player1.give_char(), True, (98,102,104))
                screen.blit(character, board.give_pos(row,colon,character.get_width()//2,character.get_height()//2))
            elif board.board[row][colon] == player2.give_char():
                character = font.render(player2.give_char(), True, (237,221,181))
                screen.blit(character, board.give_pos(row,colon,character.get_width()//2,character.get_height()//2))

    pygame.display.update()
