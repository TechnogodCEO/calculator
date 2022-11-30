import pygame, sys
from pygame.locals import QUIT
import FUNCTION 
# importing required library
import pygame


# create button class
class button:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def area(self):
        LT = [self.x, self.y]
        RT = [self.x + self.w, self.y]
        LB = [self.x, self.y + self.h]
        RB = [self.x + self.w, self.y + self.h]
        y1 = self.y
        y2 = self.y + self.h 
        x1 = self.x
        x2 = self.x + self.w
        return LT,RT,LB,RB,y1,y2,x1,x2

#create class objects
b1 = button(35, 305, 80, 50)
b2 = button(130, 305, 80, 50)
b3 = button(220, 305, 80, 50)
b4 = button(350, 305, 80, 50)
b5 = button(35, 380, 80, 50)
b6 = button(130, 380, 80, 50)
b7 = button(220, 380, 80, 50)
b8 = button(350, 380, 80, 50)
b9 = button(35, 455, 80, 50)
b10 = button(130, 455, 80, 50)
b11 = button(220, 455, 80, 50)
b12 = button(350, 455, 80, 50)
b13 = button(35, 530, 80, 50)
b14 = button(130, 530, 80, 50)
b15 = button(220, 530, 80, 50)
b16 = button(350, 530, 80, 50)
b17 = button(35, 605, 80, 50)
b18 = button(130, 605, 80, 50)
b19 = button(220, 605, 80, 50)
b20 = button(35, 680, 80, 50)
b21 = button(130, 680, 80, 50)
b22 = button(220, 680, 80, 50)
b23 = button(350, 605, 80, 130)

objects = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23]

# activate the pygame library .
pygame.init()
X = 466
Y = 807

# create the display surface object
# of specific dimension..e(X, Y).
scrn = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('TI-108 calculator')

# create a surface object, image is drawn on it.
imp = pygame.image.load("TI-108calc.jpg").convert()

# Using blit to copy content from one surface to other
scrn.blit(imp, (0, 0))

# paint screen one time
pygame.display.flip()
status = True
while (status):

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for i in objects:
              coi = i.area()
              #if ((coi[6] >=pos[0] and pos[0]<=coi[5]) and (coi[8] >=pos[1] and pos[1]<=coi[7])) :
                
    
    

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        elif event.type == pygame.QUIT:
            status = False
    pygame.draw.rect(scrn, (255,255,255), pygame.Rect(30, 30, 60, 60))   
    pygame.display.update()
# deactivates the pygame library
pygame.quit()
