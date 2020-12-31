class Resource():
    def __init__(self):
        self.food = 0
        self.wood = 0
        
        self.resources = {'food': self.food, 'wood' : self.wood}

    def add(self, resourceType, resource):
        self.resources[resourceType] += resource

    def remove(self, resourceType, resource):
        self.resources[resourceType] -= resource