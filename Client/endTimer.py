# Timer for winning game

from timer import *

class EndTimer(Timer):
    def __init__(self, x, y, image, totalTime):
        super(EndTimer, self).__init__(x, y, image, totalTime)
        self.startWidth = 756
        self.image = pygame.transform.scale(image, (self.startWidth, self.height))
    
    def update(self):
        self.elapsedTime = min(self.elapsedTime + 1, self.totalTime)
        newWidth = max(int(self.startWidth * ((self.totalTime - self.elapsedTime) / self.totalTime)), 0)
        self.image = pygame.transform.scale(self.image, (newWidth, self.height))
        self.updateRect()
    '''
    def update(self):
        self.elapsedTime = min(self.elapsedTime + 1, self.totalTime)
        newWidth = max(0, min(int(self.finalWidth * (1 - ((self.totalTime - self.elapsedTime) / self.totalTime))), self.finalWidth))
        print("newWidth = ", newWidth)
        self.image = pygame.transform.scale(self.image, (newWidth, self.height))
        print("Scaled the image")
        self.updateRect()
        print("updated the rect")
    '''



'''
elapsedTime = 0
def update(totalTime):
    elapsedTime = 0
    while elapsedTime <= totalTime:
        elapsedTime += 1
        print(elapsedTime)
        newWidth = min(int(756 * (1 - ((totalTime - elapsedTime) / totalTime))), 756)
        print(newWidth)

'''