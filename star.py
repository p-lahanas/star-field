import random
import pygame

WHITE = (255,255,255)

class Star:
    """
    A class to represent the stars in the star field.
    Parameters:
        win_width(int) = the pygame window width
        win_height(int) = the pygame window height
    """

    def __init__(self, win_width, win_height):

        self.width = win_width
        self.height = win_height
        self.reset()

    def reset(self):
        #randomly select x, y and z coordinates -> negative used to centre the movement in the middle of the screen
        self.x = random.randint(-self.width//2, self.width//2)
        self.y = random.randint(-self.height//2,self.height//2)
        self.z = random.randint(1,self.width//2)
        self.orig_z = self.z
        self.sx0 = round((self.x/self.orig_z)*self.width//2) + self.width//2
        self.sy0 = round((self.y/self.orig_z)*self.height//2) + self.height//2

    def update(self):
        self.z -= 1

        if self.z < 1:
            self.reset()
            
        self.radius = round((self.orig_z-self.z)/self.orig_z*4)
        
        self.sx = round((self.x/self.z)*self.width//2) + self.width//2
        self.sy = round((self.y/self.z)*self.height//2) + self.height//2

        

    def draw(self, display):
        pygame.draw.circle(display, WHITE, (self.sx, self.sy), self.radius)