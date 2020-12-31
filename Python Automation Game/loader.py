from button import Button
import pygame
pygame.init()

class Loader(Button):
    def __init__(self,posX,posY,width, height, text, page, resourceType, reward, timer,resource, isUnlocked):
        super().__init__(posX,posY,width, height,text, page)
        self.resourceType = resourceType
        self.reward = reward
        self.timer = timer
        self.resource = resource #resource object storing all resource counts
        
        self.progress = 0
        self.isUnlocked = isUnlocked
        self.running = False

    def tick(self):
        if self.running:
            if self.progress >= 1:
                self.progress = 0
                self.running = False
                self.resource.add(self.resourceType, self.reward)
            else:
                self.progress += 1 / self.timer

    def onClick(self): #when button is clicked
        self.color = (100,100,100)
        self.running = True

    def draw(self, surface):
        if self.isUnlocked:
            pygame.draw.rect(surface,self.color,self.getRect())
            pygame.draw.rect(surface,(50,50,50),[self.posX + 1, self.posY + 1, 
            (self.width - 2) * self.progress, self.height -2]) #progress bar
            surface.blit(self.font.render(self.text, True, (0,0,0)) ,(self.posX + 20, self.posY + 10))

    
    