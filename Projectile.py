from math import sin, cos, radians

class Projectile:
    
    def __init__(self, x0, y0, v0, angle):
        '''
        x0 and y0 are initial coordinates of the cannon
        v0 is the initial velocity
        angle is the angle of shooting in degrees
        '''
        #CONSTANTS
        self.time = 0 #s
        self.mass = 0.050 #kg
        
        # Friction factor
        self.friction = 0.5 # N/(m/s)
        
        # current x and y coordinates of the ball
        self.x    = x0
        self.y    = y0
        # current value of velocity components
        self.vx  = v0*cos(radians(angle))
        self.vy  = v0*sin(radians(angle))

        # acceleration by x and y axes
        self.ax   = 0
        self.ay   = -9.81 #m/s^2
        
        # these list will contain discrete set of ball coordinates
        self.xarr = [self.x]
        self.yarr = [self.y]
    
    '''
    v = u + at
    '''    
    def updateVx(self, dt):
        self.vx = self.vx + self.ax*dt
        return self.vx
    
    def updateVy(self, dt):
        self.vy = self.vy + self.ay*dt
        return self.vy
    
    '''
    s = 0.5(u + v)t
    '''
    def updateX(self, dt):
        self.x = self.x + 0.5*(self.vx + self.updateVx(dt))*dt
        return self.x
    
    def updateY(self, dt):
        self.y = self.y + 0.5*(self.vy + self.updateVy(dt))*dt
        return self.y
    
    def step(self, dt):
        # append the coordinates of the projitile at t = dt into lists
        self.xarr.append(self.updateX(dt))
        self.yarr.append(self.updateY(dt))
        self.time = self.time + dt
