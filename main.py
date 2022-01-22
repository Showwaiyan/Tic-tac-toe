import pygame, sys
import gameboard

board = gameboard.Board((640,640))

pygame.init()

screen = pygame.display.set_mode(board.screen_size, 0, 32)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255,255,255))

    pygame.display.update()
