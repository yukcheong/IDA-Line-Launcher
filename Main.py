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

def makeShoot(x0, y0, velocity, angle):
    """
    Returns a tuple with sequential pairs of x and y coordinates
    """
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
    
    # Spring constant
    k = 1000/Ns*Np # N/m
    
    ################################
    '''
    targetDistance = input("Target liner distance: ")
    while checkNum(targetDistance) == False :
        targetDistance = input("Pls input a valid number: ")
    
    bearingOfTarget = input('Bearing of target from laucher: ')
    while checkNum(bearingOfTarget) == False :
        bearingOfTarget = input('Pls input a valid number: ')
    '''
    
    
    
    
    x0 = 0
    y0 = 0
    velocity = 10
    print makeShoot(x0, y0, velocity, 45)
    x45, y45 = makeShoot(x0, y0, velocity, 45)
    x30, y30 = makeShoot(x0, y0, velocity, 30)
    x60, y60 = makeShoot(x0, y0, velocity, 60)
    plt.plot(x45, y45, 'bo-', x30, y30, 'ro-', x60, y60, 'ko-',
        [0, 12], [0, 0], 'k-' # ground
        )
    plt.legend(['45 deg shoot', '30 deg shoot', '60 deg shoot'])
    plt.xlabel('X coordinate (m)')
    plt.ylabel('Y coordinate (m)')
    plt.show()
    
if __name__ == '__main__':
    main()