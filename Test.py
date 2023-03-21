import sys, pygame, math
import numpy as np
from pygame.locals import*


width = 600
height = 300
screen_color = (49, 150, 100)
line_color = (255, 0, 0)

cubeA = [20,20,20,20,10,20,10,10,20,10,20,20,10,20,10,10,10,10,20,10,10,20,20,10]
cubeALines = [0,1,1,2,2,3,3,4,4,5,5,6,6,7,0,7,0,3,4,7,1,6,2,5]
cubeB = [20,20,20,20,20,0,20,0,0,20,0,20,0,20,20,0,20,0,0,0,0,0,0,20,]
cubeBLines = [0,1,1,2,2,3,3,4,4,5,5,6,6,7]

r = 15
zNear = 50
zFar = 100
FovAngle = 100
Aspect = height/width
ƒ = (1/math.tan((FovAngle/2)* math.pi / 180))

roMatX = [[1,0,0],[0,(math.cos(r* math.pi / 180)),(-1*(math.sin(r* math.pi / 180)))],[0,math.sin(r* math.pi / 180),math.cos(r* math.pi / 180)]]
roMatXNeg = [[1,0,0],[0,(math.cos((r*-1)* math.pi / 180)),(-1*(math.sin((r*-1)* math.pi / 180)))],[0,math.sin((r*-1)* math.pi / 180),math.cos((r*-1)* math.pi / 180)]]
roMatY = [[math.cos(r* math.pi / 180),0,math.sin(r * math.pi /180)],[0,1,0],[(-1* (math.sin(r * math.pi / 180))),0, math.cos(r * math.pi / 180)]]

PerProjMat = [[Aspect*ƒ,0,0,0],[0,ƒ,0,0],[0,0,(zFar/(zFar-zNear)),(((-1*zFar)*zNear)/(zFar-zNear))],[0,0,1,0]]
RenderedPoints = []


def main():
    loadP = cubeA
    loadPLines = cubeALines
    def rFrame(screen):
        RenderedPoints = []
        for i in range(len(loadP)//3):
            p = i*3
            point = [loadP[p],loadP[p+1],loadP[p+2],1]
            mult = np.dot(PerProjMat, point)
            mult[1] = mult[1]/2
            l=[]
            for i in range(3):
                l.append(((mult[i])/(mult[2])) * -1000 + 50)
                print(l)
            RenderedPoints.append(l)

        for i in range(len(loadPLines)//2):
            q = i*2
            pygame.draw.line(screen,line_color, (int(RenderedPoints[loadPLines[q]][0]), int(RenderedPoints[loadPLines[q]][1])), (int(RenderedPoints[loadPLines[q+1]][0]), int(RenderedPoints[loadPLines[q+1]][1])))
        pygame.display.flip()


    screen=pygame.display.set_mode((width,height))
    screen.fill(screen_color)
    rFrame(screen)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        z = []
                        for i in range(len(loadP)//3):
                            p = i*3
                            point = [loadP[p],loadP[p+1],loadP[p+2]]
                            z = z + (np.dot(roMatX,point).tolist())
                        loadP = z 
                        print(loadP)
                        rFrame(screen)
                    if event.key == pygame.K_s:
                        z = []
                        for i in range(len(loadP)//3):
                            p = i*3
                            point = [loadP[p],loadP[p+1],loadP[p+2]]
                            z = z + (np.dot(roMatXNeg,point).tolist())
                        loadP = z 
                        print(loadP)
                        rFrame(screen)
                    if event.key == pygame.K_a:
                        z = []
                        for i in range(len(loadP)//3):
                            p = i*3
                            point = [loadP[p],loadP[p+1],loadP[p+2]]
                            z = z + (np.dot(roMatY,point).tolist())
                        loadP = z 
                        print(loadP)
                        rFrame(screen)
main()