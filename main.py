import pygame, sys
import gameboard

board = gameboard.Board((640,640))
rect_color = (44,157,153)
background_color = (64,135,132)

pygame.init()

screen = pygame.display.set_mode(board.screen_size, 0, 32)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.check_square(event.pos)

    screen.fill(background_color)

    #Drawing nine square on the screen
    for y in range(0,board.screen_size[1],220):
        for x in range(0,board.screen_size[0],220):
            pygame.draw.rect(screen, rect_color, ((x,y),(200,200)))
                
    pygame.display.update()
