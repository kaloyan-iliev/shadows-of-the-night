
# coding: utf-8

# In[ ]:


import sys
import math


# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
start = [x0,y0]
w1=w
h1=h
y1=0
x1=0
counter = 0
prev_dir = ""
step_x = 0
step_y = 0

# game loop

while True:
    change_dir_x = False
    change_dir_y = False
    
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    #ADD LOGIC FOR CHANGING DIRECTIONS
    if counter > 0:
        if prev_dir in ["U","UR","UL"] and bomb_dir in ["D","DR","DL"]:
            change_dir_y = True
        if prev_dir in ["L","UL","DL"] and bomb_dir in ["R","DR","UR"]:
            change_dir_x = True
        if bomb_dir in ["U","UR","UL"] and prev_dir in ["D","DR","DL"]:
            change_dir_y = True
        if bomb_dir in ["L","UL","DL"] and prev_dir in ["R","DR","UR"]:
            change_dir_x = True
    

    
    print("Prev dir, cur dir",prev_dir ,bomb_dir,change_dir_y,change_dir_x, file=sys.stderr)
    print("x0     ",x0, "y0         ",y0, file=sys.stderr)
    print("x1     ",x1, "y1         ",y1, file=sys.stderr)    
    prev_dir = bomb_dir


    if bomb_dir in ["U","UR","UL","DR","DL","D"]:
        if bomb_dir[0] == "U":
            if counter == 0:
                step_y = round(y0/2)
            else:
                step_y = round((step_y/2)+0.1)
            print("step_y over 2     ",step_y,step_y/2, round(step_y/2,0), int(step_y/2), file=sys.stderr)  
            if step_y ==0:
                step_y +=1
            y0 -= step_y
                
        if bomb_dir[0] == "D":
            if counter == 0:
                step_y = round((h-y0)/2)
            else: 
                step_y = round(step_y/2)
            if step_y ==0:
                step_y +=1
            print("step_y over 2     ",step_y,step_y/2, round(step_y/2,0), int(step_y/2), file=sys.stderr)  
            
            y0 += step_y
            
            
    if bomb_dir in ["L","UR","UL","DR","DL","R"]:
        if bomb_dir[-1] == "R":
            if counter == 0:
                step_x = int((w-x0)/2)
            else:
                step_x = round(step_x/2+0.0)
            if step_x ==0:
                step_x +=1    
            x0 += step_x
                
        if bomb_dir[-1] == "L":
            if counter == 0:
                step_x = round((x0)/2)
            else: step_x = round(step_x/2)
            if step_x ==0:
                step_x +=1
            x0 -= step_x
#    print("width     ",w, "height         ",h, file=sys.stderr)  
    print("step_x     ",step_x, "step_y         ",step_y, file=sys.stderr)         
    counter+=1                


    if x0 > w:
        x0=w
    if y0 > h:
        y0=h
    print(x0,y0)

