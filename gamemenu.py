# Module import start
import pygame, sys
import gamebutton
# Module import end


pygame.init()

def gameintro_menu(screen,screen_width,screen_height):
    MENU_BACKCOLOR = (64,135,132) # Menu background color
    
    playbutton = gamebutton.Button("Play...!!", (0,0,0))
    quitbutton = gamebutton.Button("Quit.....", (0,0,0))

    playbutton.set_size(80)
    quitbutton.set_size(80)

    font = pygame.font.SysFont("arial",playbutton.get_size(),True)
     
    playbutton.set_surface(font.render(playbutton.get_text(), True, playbutton.get_color()))
    quitbutton.set_surface(font.render(quitbutton.get_text(), True, quitbutton.get_color()))

    playbutton.set_pos(((screen_width//2)-playbutton.get_surface().get_width()//2,(screen_height//2)-playbutton.get_surface().get_height()//2))
    quitbutton.set_pos(((screen_width//2)-quitbutton.get_surface().get_width()//2,(screen_height-120)-quitbutton.get_surface().get_height()//2))
    
    screen.fill(MENU_BACKCOLOR)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playbutton.click(event.pos):
                   return True
                elif quitbutton.click(event.pos):
                   return False
                
        screen.blit(playbutton.get_surface(), playbutton.get_pos())
        screen.blit(quitbutton.get_surface(), quitbutton.get_pos())
        pygame.display.update()
        
