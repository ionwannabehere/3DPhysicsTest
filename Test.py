import sys, pygame, math
import numpy as np
from pygame.locals import*


width = 480
height = 360
screen_color = (49, 150, 100)
line_color = (255, 0, 0)

cubeA = [20,20,20,20,10,20,10,10,20,10,20,20,10,20,10,10,10,10,20,10,10,20,20,10]
cubeB = [20,20,20,20,20,0,20,0,0,20,0,20,0,20,20,0,20,0,0,0,0,0,0,20,]
zNear = 50
zFar = 100
FovAngle = 100
Aspect = height/width
ƒ = (1/math.tan((FovAngle/2)* math.pi / 180))

PerProjMat = [[Aspect*ƒ,0,0,0],[0,ƒ,0,0],[0,0,(zFar/(zFar-zNear)),(((-1*zFar)*zNear)/(zFar-zNear))],[0,0,1,0]]

for i in range(8):
    p = i*3
    point = [cubeB[p],cubeB[p+1],cubeB[p+2],1]
    mult = np.dot(PerProjMat, point)
    print(str(mult) +  " : " + str(i+1))


def main():
    screen=pygame.display.set_mode((width,height))
    screen.fill(screen_color)

    pygame.draw.line(screen,line_color, (60, 80), (130, 100))
    pygame.draw.line(screen,line_color, (50, 50), (850, 400))
    pygame.display.flip()
    while True:
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)
main()