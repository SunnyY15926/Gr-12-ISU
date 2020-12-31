import pygame
pygame.init()

class Textbox():
    def __init__(self,posX,posY,width,height, text = '', font = pygame.font.Font('freesansbold.ttf', 11), color = (150, 150, 150)):
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.color = color

    def __repr__(self):
        return self.text
    
    def __str__(self):
        return self.__repr__()

    def getRect(self):
        return [self.posX,self.posY,self.width, self.height]

    def draw(self, surface):
        pygame.draw.rect(surface,self.color,self.getRect())
        surface.blit(self.font.render(self.text, True, (0,0,0)) ,(self.posX + 20, self.posY + 10))

