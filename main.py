import pygame, sys
import gameboard, gameplayer

board = gameboard.Board((640,640))
player1 = gameplayer.Player("o")
player2 = gameplayer.Player("x")
playerstate = True

rect_color = (44,157,153)
background_color = (64,135,132)

pygame.init()

font = pygame.font.SysFont("arial",80)
screen = pygame.display.set_mode(board.screen_size, 0, 32)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.change_square(event.pos,playerstate)
            playerstate = not playerstate

    screen.fill(background_color)
    print(board.board)
    #Drawing nine square on the screen
    for y in range(0,board.screen_size[1],220):
        for x in range(0,board.screen_size[0],220):
            pygame.draw.rect(screen, rect_color, ((x,y),(200,200)))
                
    pygame.display.update()
