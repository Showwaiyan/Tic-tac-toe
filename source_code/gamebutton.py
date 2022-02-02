# Class for button
class Button():

    def __init__(self,text, color, box=None ,font=None, surface=None,pos=None, size=None):
        self.text = text # Text that will appear on screen
        self.color = color # Text color
        self.box = box
        self.font = font
        self.surface = surface
        self.pos = pos   # Text-block position
        self.size = size # Text-block dimension
        

    def get_text(self):
        # Getter of text
        return self.text

    def get_color(self):
        # Getter of color
        return self.color

    def get_box(self):
        # Getter of color
        return self.box

    def get_font(self):
        # Getter of font
        return self.font

    def get_surface(self):
        # Getter of surface object
        return self.surface
    
    def get_pos(self):
        # Getter of text-block postionn
        return self.pos

    def get_size(self):
        # Getter of text-block dimension
        return self.size

    def set_box(self,box):
        # Setter of box
        self.box = box

    def set_font(self,font):
        # Setter of font
        self.font = font

    def set_surface(self,surface):
        # Setter of text surface object
        self.surface = surface

    def set_pos(self,pos):
        # Setter of text-block postion
        self.pos = pos

    def set_size(self,size):
        # Setter of text-block size
        self.size = size

    def click(self,mouse_pos):
        # Checking if mouse positon x and y are in text dimension
        if (mouse_pos[0] >= self.pos[0] and mouse_pos[0] <= self.pos[0]+self.surface.get_width()) and (mouse_pos[1] >= self.pos[1] and mouse_pos[1] <=  self.pos[1]+self.surface.get_height()):
            return True
        else:
            return False
        

