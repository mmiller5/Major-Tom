from button import *

class Button1(Button):
    def __init__(self, x, y, image, isSolution):
        super(Button1, self).__init__(x, y, image)
        self.isSolution = isSolution
    
    def clicked(self, mx, my):
        pass