import pygame


class Text:
    
    ##Attributes
    def __init__(self,font,text,font_size,text_surface,text_rect):
        self.font = font
        self.text = text
        self.font_size = font_size
        self.text_surface = text_surface
        self.text_rect = text_rect
        
    ##Takes position of mouse cursor and checks if its in boundaries of button
    def check_for_hover(self,position):
        if position[0] in range(self.text_rect.left,self.text_rect.right) and position[1] in range(self.text_rect.top,self.text_rect.bottom):
            return True
        return False
    
    
    def create_text(self,color,x_cord,y_cord):
        self.font = pygame.font.Font(None,self.font_size) ##Makes font 
        self.text_surface = self.font.render(self.text,True,color) ##Renders text
        self.text_rect = self.text_surface.get_rect() #Gets size of text_surface
        self.text_rect.center = (x_cord,y_cord) #Where the center of the square is?

    
    ##Creates padding between text and rectangle
    def create_padding(self,padding,box_rect_var,):
        box_rect_var = pygame.Rect(
        self.text_rect.left - padding,
        self.text_rect.top - padding,
        self.text_rect.width + 2 * padding,
        self.text_rect.height + 2 * padding,
        )
        return box_rect_var

    ##Draws text on screen
    def draw_text(self,screen,color,box_rect):
        pygame.draw.rect(screen,color,box_rect, border_radius = 5)    
        screen.blit(self.text_surface,self.text_rect)

    
    ##Draws the number index of each vertex given a shape
    @staticmethod
    def draw_vertex_number(projected_points,font_size,color_text,color_background,screen):
        i = 0
        for points in projected_points:
            text_index = Text(None,str(i),font_size,None,None)
            text_index.create_text(color_text,points[0],points[1]+20)
            box_rect_text_index = []
            box_rect_text_index = text_index.create_padding(10,box_rect_text_index)
            text_index.draw_text(screen,color_background,box_rect_text_index)
            i += 1
    