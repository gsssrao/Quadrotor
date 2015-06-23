import numpy as np
from plot import plot_trajectory
from math import sin, cos

class UserCode:
    def __init__(self):
        self.position = np.array([[0], [0]])
        
    def measurement_callback(self, t, dt, navdata):
        '''
        :param t: time since simulation start
        :param dt: time since last call to measurement_callback
        :param navdata: measurements of the quadrotor
        '''
        
        # update self.position by integrating measurements contained in navdata
        theta = navdata.rotZ
        self.position[0] = self.position[0]+navdata.vx*dt*cos(theta)-navdata.vy*dt*sin(theta)
        self.position[1] = self.position[1]+navdata.vx*dt*sin(theta)+navdata.vy*dt*cos(theta)
        # print str(navdata.rotZ)
        plot_trajectory("odometry", self.position)
