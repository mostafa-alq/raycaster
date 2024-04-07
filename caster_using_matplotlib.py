# This was the first test of a raycaster, using a very inefficient algorithm
# I used matplotlib and manipulated the way that it drew lines in order to feign a raycaster.
# However, this was extremely slow and was difficult to scale so I will not work on this further.
# My next raycaster will use either a digital differential analyser or bresenham's line algorithm.



import numpy as np
from matplotlib import pyplot as plt
import keyboard

mapa = [
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,1,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]]

# initial pos
posx, posy = 1,1

# exit
exitx, exity = 3,3

# what angle is the player looking at relative to origin
rot = np.pi/4
while True:
    for i in range(60):
        rot_i = rot + np.deg2rad(i-30)
        x, y = posx, posy
        sin, cos = 0.02*np.sin(rot_i), 0.02*np.cos(rot_i)
        n = 0
        
        while True:
            x, y, n = x + cos, y + sin, n +1
            if mapa[int(x)][int(y)]:
                h = 1/(0.02*n)
                break
            
        plt.vlines(i, -h, h, lw = 8)
        
    plt.axis('off');plt.tight_layout();plt.axis([0,60,-1,1])
    plt.draw(); plt.pause(0.0001);plt.clf()
    
    key = keyboard.read_key()
    x, y = (posx, posy)

    if key == 'up':
        x, y = (x + 0.3*np.cos(rot), y + 0.3*np.sin(rot))
    elif key == 'down':
        x, y = (x - 0.3*np.cos(rot), y - 0.3*np.sin(rot))
    elif key == 'left':
        rot = rot - np.pi/8
    elif key == 'right':
        rot = rot + np.pi/8
    elif key == 'esc':
        break

    # player is only allowed to move if they are not about to walk into a wall
    if mapa[int(x)][int(y)] == 0:
        # checks if they are in the exit
        if int(posx) == exitx and int(posy) == exity:
            break
        posx, posy = (x, y)
    


plt.close()
