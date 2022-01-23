import pygame, sys
import gameboard, gameplayer

board = gameboard.Board((640,640))
player1 = gameplayer.Player("o")
player2 = gameplayer.Player("x")
playerstate = True

rect_color = (44,157,153)
background_color = (64,135,132)

pygame.init()

font = pygame.font.SysFont("arial",200)
screen = pygame.display.set_mode(board.screen_size, 0, 32)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if playerstate:
                board.change_square(event.pos, player1.give_char())
            else:
                board.change_square(event.pos, player2.give_char())
            playerstate = not playerstate

    screen.fill(background_color)

    #Drawing nine square on the screen
    for y in range(0,board.screen_size[1],220):
        for x in range(0,board.screen_size[0],220):
            pygame.draw.rect(screen, rect_color, ((x,y),(200,200)))

    for i in range(0,9):
        if board.board[i] == player1.give_char():
            character = font.render(player1.give_char(), True, (255,226,190))
            screen.blit(character, board.give_pos(i,character.get_width()//2,character.get_height()//2))
        elif board.board[i] == player2.give_char():
            character = font.render(player2.give_char(), True, (88,89,90))
            screen.blit(character, board.give_pos(i,character.get_width()//2,character.get_height()//2))
                
    pygame.display.update()
