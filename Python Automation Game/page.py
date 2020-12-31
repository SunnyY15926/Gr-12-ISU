class Page():
    def __init__(self, buttons = [], text = [], loaders = [], other = []):
        self.buttons = buttons
        self.loaders = loaders
        self.text = text
        self.other = other
    
    def mouseClick(self,x, y):
        for i in self.buttons:
            if i.intersect(x,y):
                i.onClick()
                return i.page
        for i in self.loaders:
            if i.intersect(x,y):
                i.onClick()
                return i.page
    
    def offClick(self):
        for i in self.buttons:
            i.offClick()
        for i in self.loaders:
            i.offClick()
                
    def draw(self,surface):
        for button in self.buttons:
            button.draw(surface)
        for i in self.text:
            i.draw(surface)
        for i in self.loaders:
            i.draw(surface)
    
    def tick(self):
        for i in self.loaders:
            i.tick()