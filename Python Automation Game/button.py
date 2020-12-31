from textbox import Textbox
import pygame
pygame.init()

class Button(Textbox):
    def __init__(self,posX,posY,width,height, text, page, 
    font = pygame.font.Font('freesansbold.ttf', 11), color = (150, 150, 150)):
        super().__init__(posX,posY,width, height,text,font)

        self.isUnlocked = True

        self.font = font
        self.page = page #destination of the button
        self.color =  color #button color is default grey unless otherwise specified


    def intersect(self,x,y):
        return self.posX < x and (self.posX + self.width) > x and self.posY < y and (self.posY + self.height) > y
        
    def onClick(self): #when button is clicked
        self.color = (100,100,100)
        return self.page
        

    def offClick(self):
        self.color = (150, 150, 150)

    def onHover(self): #when mouse hovers over the button
        pass
        
    def unlock(self):
        self.isUnlocked = True

    def draw(self, surface):
        if self.isUnlocked:
            pygame.draw.rect(surface,self.color,self.getRect())
            surface.blit(self.font.render(self.text, True, (0,0,0)) ,(self.posX + 20, self.posY + 10))