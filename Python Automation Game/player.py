class Player():
    def __init__(self, posX, posY, speed = 1):
        self.posX = posX
        self.posY = posY
        self.speed = speed

    def getX(self):
        return self.posX
    
    def getY(self):
        return self.posY

    def getSpeed(self):
        return self.speed

    def move(self,x,y):
        self.posX += x
        self.posY += y
        
