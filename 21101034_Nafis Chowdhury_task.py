from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math
import random
import time

dy=0
dx=0

d=0

NE=0
E=0
red=0
green=0
blue=0
c_x1=0
c_x2=0

c_y1=0
c_y2=0
x_0=random.randint(0,400)
arr=[]
arr2=[]
zone=0
y_0=500
x_move=0
y_move=0
game_over=False
pause=False
x_middle=0
y_middle=0
score=0
speed=1
m_x=0
m_y=0

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    glutPostRedisplay()


    
def specialKeyListener(key, x, y):
    global x_move, game_over,GL_PASS_THROUGH_TOKEN

    if key==GLUT_KEY_LEFT and game_over==False and pause==False:
        x_move-=2
        if x_move<0:
            x_move=0
    if key==GLUT_KEY_RIGHT and game_over==False and pause==False:
        
        x_move+=2
        if x_move>400:
            x_move=400
    glutPostRedisplay()


    
        

def art_icons():
    global pause   
    glColor3f(1, 0, 0)        #
    find_zone(20,460,80,460)
    find_zone(20,460,55,490)
    find_zone(20,460,55,430)

    if pause==True:
        glColor3f(0, 1, 0)
        find_zone(230,490,230,430) 
        find_zone(230,430,280,460)
        find_zone(230,490,280,460)
    else:
        glColor3f(0, 1, 0)
        find_zone(240,490,240,430) 
        find_zone(270,490,270,430)
    glColor3f(0, 0, 1)
    find_zone(445,490,495,430) 
    find_zone(495,490,445,430)
    

def find_zone(x_1,y_1,x_2,y_2):
    arr=[]
    global dx,dy,d,E,NE,c_x1, c_x2, c_y1, c_y2,zone
    dy=y_2-y_1
    dx=x_2-x_1
    if abs(dx)>abs(dy):
        if dx>0 and dy>0:
            c_x1=x_1
            c_y1=y_1
            c_x2=x_2
            c_y2=y_2
            zone=0
        elif dx<0 and dy>0:
            c_x1=-x_1
            c_y1=y_1
            c_x2=-x_2
            c_y2=y_2
            zone=3
        elif dx<0 and dy<0:
            c_x1=-x_1
            c_y1=-y_1
            c_x2=-x_2
            c_y2=-y_2
            zone=4
        elif dx>0 and dy<0:
            c_x1=x_1
            c_y1=-y_1
            c_x2=x_2
            c_y2=-y_2
            zone=7
        if dx>0 and dy==0:
            c_x1=x_1
            c_y1=y_1
            c_x2=x_2
            c_y2=y_2
            zone=0
        elif dx<0 and dy==0:
            c_x1=-x_1
            c_y1=y_1
            c_x2=-x_2
            c_y2=y_2
            zone=3
    else:
        if dx>0 and dy>0:
            c_x1=y_1
            c_y1=x_1
            c_x2=y_2
            c_y2=x_2
            zone=1
        elif dx<0 and dy>0:
            c_x1=y_1
            c_y1=-x_1
            c_x2=y_2
            c_y2=-x_2
            zone=2
        elif dx<0 and dy<0:
            c_x1=-y_1
            c_y1=-x_1
            c_x2=-y_2
            c_y2=-x_2
            zone=5
        elif dx>0 and dy<0:
            c_x1=-y_1
            c_y1=x_1
            c_x2=-y_2
            c_y2=x_2
            zone=6
        elif dx==0 and dy>0:
            c_x1=y_1
            c_y1=x_1
            c_x2=y_2
            c_y2=x_2
            zone=1
        elif dx==0 and dy<0:
            c_x1=-y_1
            c_y1=x_1
            c_x2=-y_2
            c_y2=x_2
            zone=6
    dy=c_y2-c_y1
    dx=c_x2-c_x1
    d=2*dy-dx
    E=2*dy
    NE=2*dy-2*dx
    while c_x1<c_x2:
        if d>0:
            d=d+NE
            c_x1+=1
            c_y1+=1
        else:
            d=d+E
            c_x1+=1 
        if zone==0:
            arr.append((c_x1,c_y1))
        elif zone==1:
            arr.append((c_y1,c_x1))
        elif zone==2:
            arr.append((-c_y1,c_x1))
        elif zone==3:
            arr.append((-c_x1,c_y1))
        elif zone==4:
            arr.append((-c_x1,-c_y1))
        elif zone==5:
            arr.append((-c_y1,-c_x1))
        elif zone==6:
            arr.append((c_y1,-c_x1))
        elif zone==7:
            arr.append((c_x1,-c_y1))
    for x,y in arr:
        glPointSize(1) 
        glBegin(GL_POINTS)
        glVertex2f(x,y)
        glEnd()
    
def showScreen():
    global game_over,score,pause
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0)
    glLoadIdentity()
    iterate()
    art_icons()
    draw_bar()
    if game_over==False:
        draw_diamond()

    glutSwapBuffers()

def draw_bar():
    global x_move,game_over
    x0=x_move
    x1=x_move+100
    if game_over==True:
        glColor3f(1, 0, 0)
    else:
        glColor3f(1, 1, 1)
    find_zone(x0,25,x1,25)
    find_zone(x0+10,3,x1-10,3)
    find_zone(x0,25,x0+10,3)
    find_zone(x1,25,x1-10,3)

def mouseListener(button, state, x, y):	
    global m_x,m_y,pause,y_move,x_0,game_over,score,speed
    if button == GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):
  
            m_x=x
            m_y=500-y
            if m_x>=445 and m_x<=495 and m_y>=430 and m_y<=490:
                print("Goodbye")
                glutLeaveMainLoop()
                
            if pause==False and m_x>=240 and m_x<=270 and m_y>=430 and m_y<=490:
            
                pause=True
            elif pause==True and m_x>=230 and m_x<=280 and m_y>=430 and m_y<=490:
                pause=False
            if m_x>=20 and m_x<=80 and m_y>=460 and m_y<=490:
                y_move=0
                x_0=random.randint(0,400)
                game_over=False
                score=0
                speed=0.5
                print("Starting over!")
            
                
            

def draw_diamond():
    global y_move,x_middle,y_middle,x_0,x_move,game_over,red,green,blue,score,speed,pause



    x_middle=(x_0+x_0+50)//2
    y_middle=(y_0+y_0+50)//2
    if y_move==0:
        red=round(random.random(),2)
        green=round(random.random(),2)
        blue=round(random.random(),2)
    glColor3f(red, green, blue)
    if pause==False:
        find_zone(x_middle,y_0-y_move,x_0,y_middle-y_move)
        find_zone(x_0,y_middle-y_move,x_middle,y_0+50-y_move)
        find_zone(x_middle,y_0+50-y_move,x_0+50,y_middle-y_move)
        find_zone(x_0+50,y_middle-y_move,x_middle,y_0-y_move)
        y_move=y_move+speed
    else:
        find_zone(x_middle,y_0-y_move,x_0,y_middle-y_move)
        find_zone(x_0,y_middle-y_move,x_middle,y_0+50-y_move)
        find_zone(x_middle,y_0+50-y_move,x_0+50,y_middle-y_move)
        find_zone(x_0+50,y_middle-y_move,x_middle,y_0-y_move)
    if x_0+50>x_move and x_0+50<(x_move+100) and y_move>475:
        x_0=random.randint(0,400)
        y_move=0
        score+=1
        speed+=0.3
        print("score:",score)
    if x_0>x_move and x_0<(x_move+100) and y_move>475:
        x_0=random.randint(0,400)
        y_move=0
        score+=1
        speed+=0.3
        print("score:",score)
    elif x_middle>x_move and x_middle<(x_move+100) and y_move>475:
        x_0=random.randint(0,400)
        y_move=0
        score+=1
        speed+=0.3
        
        print("score:",score)
    elif y_move>497:
        game_over=True
        print("Game Over! Score:",score)

    
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) 
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") 
glutDisplayFunc(showScreen)


glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()