import sys, math
import pygame
import numpy as np
from pygame.locals import *
import subprocess
from multiprocessing import Process
import time
from datetime import datetime, timedelta


#websockify -D --web=/usr/share/novnc/ --cert=/etc/ssl/novnc.pem 6080 localhost:5901


p = subprocess.Popen([sys.executable, '/workspaces/3DPhysicsTest/physiscs.py'], 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.STDOUT)

width = 600
height = 300
screen_color = (49, 150, 100)
line_color = (255, 0, 0)

cubeA = [20,20,20,20,10,20,10,10,20,10,20,20,10,20,10,10,10,10,20,10,10,20,20,10]
cubeALines = [0,1,1,2,2,3,3,4,4,5,5,6,6,7,0,7,0,3,4,7,1,6,2,5]
cubeB = [20,20,20,20,10,20,10,10,20,10,20,20,10,20,10,10,10,10,20,10,10,20,20,10]
cubeBLines = [0,1,1,2,2,3,3,4,4,5,5,6,6,7,0,7,0,3,4,7,1,6,2,5,0,2,0,4,0,5,0,6,1,3,1,5,1,7,1,4,2,0,2,4,2,6,2,7,3,1,3,5,3,6,3,7,4,0,4,1,4,2,4,6,5,0,5,1,5,3,5,7,6,0,6,2,6,3,6,4,7,1,7,2,7,3,7,5]

# 0: 1, 7, 3, 2, 4, 5, 6
# 1: 0, 2, 6, 3, 4, 5, 7
# 2: 1, 3, 5, 0, 4, 6, 7
# 3: 0, 2, 4, 1, 5, 6, 7
# 4: 3, 7, 5, 0, 1, 2, 6
# 5: 4, 2, 6, 0, 1, 3, 7
# 6: 1, 5, 7, 0, 2, 3, 4
# 7: 0, 4, 6, 1, 2, 3, 5









PyraA = [20,20,20,20,20,10,20,10,10,20,10,20,28,15,15]
PyraALines = [0,1,2,3,3,0,2,1,0,4,1,4,2,4,3,4]
PyraB = [20,20,20,20,20,10,20,28,15,28,15,15]
PyraBLines = [0,1,1,2,2,0,0,3,1,3,2,3]

r = 15
zNear = 50
zFar = 100
FovAngle = 90
Aspect = height/width
ƒ = (1/math.tan((FovAngle/2)* math.pi / 180))

roMatX = [[1,0,0],[0,(math.cos(r* math.pi / 180)),(-1*(math.sin(r* math.pi / 180)))],[0,math.sin(r* math.pi / 180),math.cos(r* math.pi / 180)]]
roMatXNeg = [[1,0,0],[0,(math.cos((r*-1)* math.pi / 180)),(-1*(math.sin((r*-1)* math.pi / 180)))],[0,math.sin((r*-1)* math.pi / 180),math.cos((r*-1)* math.pi / 180)]]
roMatY = [[math.cos(r* math.pi / 180),0,math.sin(r * math.pi /180)],[0,1,0],[(-1* (math.sin(r * math.pi / 180))),0, math.cos(r * math.pi / 180)]]
roMatYNeg = [[math.cos((r*-1)* math.pi / 180),0,math.sin((r*-1) * math.pi /180)],[0,1,0],[(-1* (math.sin((r*-1) * math.pi / 180))),0, math.cos((r*-1) * math.pi / 180)]]
roMatZ = [[math.cos(r * math.pi/180),(-1*(math.sin(r * math.pi / 180))),0],[math.sin(r* math.pi / 180),math.cos(r* math.pi / 180),0],[0,0,1]]
roMatZNeg = [[math.cos((r * -1) * math.pi/180),(-1*(math.sin((r * -1) * math.pi / 180))),0],[math.sin((r * -1)* math.pi / 180),math.cos((r * -1)* math.pi / 180),0],[0,0,1]]

PerProjMat = [[Aspect*ƒ,0,0,0],[0,ƒ,0,0],[0,0,(zFar/(zFar-zNear)),(((-1*zFar)*zNear)/(zFar-zNear))],[0,0,1,0]]
RenderedPoints = []


pygame.init()



def main():
    loadP = cubeA
    loadPLines = cubeALines
    def rFrame(screen):
        screen.fill(screen_color)
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




    
    timeFired = 0

    def grav():
        print("GRAV")
        print(loadP)
        for i in range(1, (len(loadP)//3)+1):
            loadP[i*2] = loadP[i*2]-0.2
        rFrame(screen)
        return datetime.now() + timedelta(seconds=1)

    while True:
        if timeFired != 0:

            if datetime.now() > timeFired:
                # HEART BEAT 

                timeFired = grav()
        else:
            # HEART BEAT START
            timeFired = grav()

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
                    if event.key == pygame.K_d:
                        z = []
                        for i in range(len(loadP)//3):
                            p = i*3
                            point = [loadP[p],loadP[p+1],loadP[p+2]]
                            z = z + (np.dot(roMatYNeg,point).tolist())
                        loadP = z 
                        print(loadP)
                        rFrame(screen)
                    if event.key == pygame.K_q:
                        z = []
                        for i in range(len(loadP)//3):
                            p = i*3
                            point = [loadP[p],loadP[p+1],loadP[p+2]]
                            z = z + (np.dot(roMatZ,point).tolist())
                        loadP = z 
                        print(loadP)
                        rFrame(screen)
                    if event.key == pygame.K_e:
                        z = []
                        for i in range(len(loadP)//3):
                            p = i*3
                            point = [loadP[p],loadP[p+1],loadP[p+2]]
                            z = z + (np.dot(roMatZNeg,point).tolist())
                        loadP = z 
                        print(loadP)
                        rFrame(screen)
main()