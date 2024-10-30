import numpy as np
from math import sin, cos

class Rotation:
    

    def __init__(self,angle=0,angle_inc=0.01):
        self.angle = angle
        self.angle_inc = angle_inc
    
    
    ##Method to increment 'angle'
    def angle_incremenation(self):
        self.angle += self.angle_inc
    
    #Method Makes a matrix that rotates on the z axis    
    def rotation_z(self):
        angle = self.angle
        return np.array([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1],
    ])
    
    #Method Makes a matrix that rotates on the y axis    
    def rotation_y(self):
        angle = self.angle
        return np.array([
            [cos(angle), 0, sin(angle)],
            [0, 1, 0],
            [-sin(angle), 0, cos(angle)]
        ])
    
    #Method Makes a matrix that rotates on the x axis    
    def rotation_x(self):
        angle = self.angle
        return  np.array([
            [1, 0, 0],
            [0, cos(angle), -sin(angle)],
            [0, sin(angle), cos(angle)]
        ])