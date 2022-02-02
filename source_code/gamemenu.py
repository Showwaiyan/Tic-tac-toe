# Module import start
import pygame, sys
import gamebutton
# Module import end


pygame.init()

def gameintro_menu(screen,screen_width,screen_height):
    MENU_BACKCOLOR = (64,135,132) # Menu background color
    TEXT_COLOR = (237,221,181)
    BOX_COLOR = (98,102,104)
    
    playbutton = gamebutton.Button("Play...!!", TEXT_COLOR)
    quitbutton = gamebutton.Button("Quit.....", TEXT_COLOR)

    playbutton.set_size(80)
    quitbutton.set_size(80)

    Title_font = pygame.font.SysFont("arial",95,True,True)
    Title_text = Title_font.render("TIC-TAC-TOE", True, TEXT_COLOR)
    Title_pos = ((screen_width//2)-Title_text.get_width()//2, 20)

    name_font = pygame.font.SysFont("arail",25)
    name_text = name_font.render("By Show WaiYan", False, (0,0,0))
    name_pos = (screen_width-150, Title_text.get_height()+40)

    playbutton.set_font(pygame.font.SysFont("arial",playbutton.get_size(),True))
    quitbutton.set_font(pygame.font.SysFont("arial",quitbutton.get_size(),True))
     
    playbutton.set_surface(playbutton.get_font().render(playbutton.get_text(), True, playbutton.get_color()))
    quitbutton.set_surface(quitbutton.get_font().render(quitbutton.get_text(), True, quitbutton.get_color()))

    playbutton.set_pos(((screen_width//2)-playbutton.get_surface().get_width()//2,(screen_height//2)-playbutton.get_surface().get_height()//2))
    quitbutton.set_pos(((screen_width//2)-quitbutton.get_surface().get_width()//2,(screen_height-120)-quitbutton.get_surface().get_height()//2))
    
    screen.fill(MENU_BACKCOLOR)
    playbutton.set_box(pygame.Rect((playbutton.get_pos()[0]-10,playbutton.get_pos()[1]-10),
                           (playbutton.get_surface().get_width()+20,
                            playbutton.get_surface().get_height()+20)))

    quitbutton.set_box(pygame.Rect((quitbutton.get_pos()[0]-10,quitbutton.get_pos()[1]-10),
                           (quitbutton.get_surface().get_width()+20,
                            quitbutton.get_surface().get_height()+20)))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playbutton.click(event.pos):
                   return True
                elif quitbutton.click(event.pos):
                   return False

        pygame.draw.rect(screen, BOX_COLOR, playbutton.get_box(),8)
        pygame.draw.rect(screen, BOX_COLOR, quitbutton.get_box(),8)
        screen.blit(Title_text, Title_pos) 
        screen.blit(name_text, name_pos)
        screen.blit(playbutton.get_surface(), playbutton.get_pos())
        screen.blit(quitbutton.get_surface(), quitbutton.get_pos())
        pygame.display.update()



def playerchose_menu(screen,screen_width,screen_height,playerstate):
    MENU_BACKCOLOR = (64,135,132) # Menu background color
    TEXT_COLOR = (0,0,0)
    TEXT_SIZE = 60
    Turn_font = pygame.font.SysFont("arial",TEXT_SIZE,False,True)
    if playerstate:
        Turn_message = "'o's turn to start"
    else:
        Turn_message = "'x's turn to start"

    Turn_text = Turn_font.render(Turn_message, True, TEXT_COLOR)
    pos = ((screen_width//2 - Turn_text.get_width()//2),(screen_height//2 - Turn_text.get_height()//2))

    screen.fill(MENU_BACKCOLOR)
    screen.blit(Turn_text,pos)

    pygame.display.update()
    
    pygame.time.wait(1000)

