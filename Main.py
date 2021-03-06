from math import sin, cos, radians
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

from Projectile import Projectile

# checks wheater a var is a number
def checkNum(varname):
    try:
        float(varname)
        return True
    except ValueError:
        return False


def f(x):
    return ax**2 + b**x + c

#Returns a tuple with sequential pairs of x and y coordinates
def makeShoot(x0, y0, velocity, angle):
    ball = Projectile(x0, y0, velocity, angle)
    dt = 0.05 # time step
    t = 0 # initial time
    ball.step(dt)
    
    while ball.y >= 0:
        ball.step(dt)
        t = t + dt

    return (ball.xarr, ball.yarr)

def main():
    
    #######Bunch of CONSTANTs########
    # Number of springs in parallel
    Np = 2
    
    # Spring constant
    k = Np*1000 # N/m
    ################################
    
        
    #######Taking inputs########
    '''
    targetDistance = input("Target liner distance: ")
    while checkNum(targetDistance) == False :
        targetDistance = input("Pls input a valid number: ")
    
    bearingOfTarget = input('Bearing of target from laucher: ')
    while checkNum(bearingOfTarget) == False :
        bearingOfTarget = input('Pls input a valid number: ')
    '''
    ################################
    
    x0 = 0
    y0 = 0
    velocity = 10 #m/s
    x, y = makeShoot(x0, y0, velocity, 45)
    plt.plot(x,y)
    plt.xlabel('X coordinate (m)')
    plt.ylabel('Y coordinate (m)')
    plt.show()
    
if __name__ == '__main__':
    main()
