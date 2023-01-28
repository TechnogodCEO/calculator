#import functions
import pygame, sys
from pygame.locals import QUIT
import FUNCTION as f
import pygame

#initilize pygame
pygame.init()

#placeholder varible for text blit
x = ""
val1 = ""
val2 = ""
clrontype = False 
curop = ""
#initilize font
Font = pygame.font.SysFont(None, 100)


# create button class
class button:

    def __init__(self, name, x, y, w, h, value=None, op=None, mop=None):
        self.name = name
        self.value = value
        self.op = op
        self.mop = mop
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.button = pygame.Rect(self.x, self.y, self.w, self.h)
        self.LT = [self.x, self.y]
        self.RT = [self.x + self.w, self.y]
        self.LB = [self.x, self.y + self.h]
        self.RB = [self.x + self.w, self.y + self.h]
        self.y1 = self.y
        self.y2 = self.y + self.h
        self.x1 = self.x
        self.x2 = self.x + self.w

    def clicked(self, pos):  
        if i.button.collidepoint(pos):
            print("you pressed button " + self.name + " and the value is: " +
                  str(self.value))
            global x    
            global val1
            global clrontype
            global curop 
            if i.value != None:
                if (x == "" or len(x) <= 8):
                    x += str(i.value)
                if clrontype:
                    x = str(i.value)
                    clrontype = False
            elif i.name == "b20": 
                x = ""
                val1 = ""
            elif i.name == "b23":
                if val1 != "" and x != "" and curop != "":
                  x = str(curop(float(val1),float(x)))[:8]
                  
            elif i.op != None and x:
                x = str(i.op(float(x)))[:8]
                print(x)
            elif i.mop !=None and x:
                
            
                if not val1 or curop != i.mop:
                    val1 = x
                    clrontype = True
                    curop = i.mop
                else:
                    x = str(i.mop(float(val1), float(x)))
                    print(x) 
                    val1 = ""
                    clrontype = True
                    
                    
                # allow for new y value to be entered 
                # store y value
                # wait for equal

#create class objects
b1 = button("b1", 35, 305, 80, 50, op=f.B1)
b2 = button("b2", 130, 305, 80, 50, op=f.B2)
b3 = button("b3", 220, 305, 80, 50, op=f.B3) #todo fix lots of decimals 
b4 = button("b4", 350, 305, 80, 50, mop=f.B4)
b5 = button("b5", 35, 380, 80, 50)
b6 = button("b6", 130, 380, 80, 50)
b7 = button("b7", 220, 380, 80, 50)
b8 = button("b8", 350, 380, 80, 50, mop=f.B8)
b9 = button("b9", 35, 455, 80, 50, 7)
b10 = button("b10", 130, 455, 80, 50, 8)
b11 = button("b11", 220, 455, 80, 50, 9)
b12 = button("b12", 350, 455, 80, 50, mop=f.B12)
b13 = button("b13", 35, 530, 80, 50, 4)
b14 = button("b14", 130, 530, 80, 50, 5)
b15 = button("b15", 220, 530, 80, 50, 6)
b16 = button("b16", 350, 530, 80, 50, mop=f.B16)
b17 = button("b17", 35, 605, 80, 50, 1)
b18 = button("b18", 130, 605, 80, 50, 2)
b19 = button("b19", 220, 605, 80, 50, 3)
b20 = button("b20", 35, 680, 80, 50, op=f.clear)
b21 = button("b21", 130, 680, 80, 50, 0)
b22 = button("b22", 220, 680, 80, 50)
b23 = button("b23", 350, 605, 80, 130)

objects = [
    b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17,
    b18, b19, b20, b21, b22, b23
]

# activate the pygame library .

WIDTH = 466
HEIGHT = 807

# create the display surface object
# of specific dimension..e(X, Y).
scrn = pygame.display.set_mode((WIDTH, HEIGHT))

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for i in objects:
                i.clicked(pos)
                #if ((coi[6] >=pos[0] and pos[0]<=coi[5]) and (coi[8] >=pos[1] and pos[1]<=coi[7])) :

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        elif event.type == pygame.QUIT:
            status = False

    #draw output backround
    pygame.draw.rect(scrn, (200, 200, 200), pygame.Rect(55, 45, 355, 80))

    # render text for screen output
    label = Font.render(str(x), 1, (0, 0, 0))
    scrn.blit(label, (60, 50))
    pygame.display.flip()
# deactivates the pygame library
pygame.quit()
