# Define a Button class that will be used to create clickable buttons on the screen.
import pygame

#Set Color for button for now 
FONT_COLOR = 'WHITE'
BOADER_COLOR = '#008080' #mint green 

class Button:
    # The constructor (__init__) method is called when a Button is created.
    # It sets up the button's text, the rectangle that defines its shape and position, and a callback function that's called when the button is clicked.
    def __init__(self, text, rect, changeState):
        self.text = text
        self.rect = pygame.Rect(rect)
        self.changeState = changeState

    # The draw method is called to draw the button on the screen.
    # It draws the button rectangle and then the button text centered within the rectangle.
    def draw(self, surface):
        pygame.draw.rect(surface, BOADER_COLOR, self.rect)
        font = pygame.font.SysFont(None, 36)
        
        text_surf = font.render(self.text, True, FONT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)

        #draws the text onto the surface
        surface.blit(text_surf, text_rect)

    # The handle_event method checks if the button has been clicked.
    # If so, it calls the callback function that was assigned during construction.
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.changeState()
