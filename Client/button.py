import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(Button, self).__init__()
        self.x = x
        self.y = y
        self.image = image
        self.baseImage = image.copy()
        self.updateRect()
        
    # taken from Lucas Peraza's GameObject.py,
    # https://github.com/LBPeraza/Pygame-Asteroids
    def updateRect(self):
        # update the object's rect attribute with the new x,y coordinates
        w, h = self.image.get_size()
        self.width, self.height = w, h
        self.rect = pygame.Rect(self.x - w / 2, self.y - h / 2, w, h)
    
    def clicked(self):
        pass