import pygame
import numpy as np
from math import *


class Shape:
    
    phi = (1 +5 ** 0.5) /2
    ##Shapes are made of vertices
    def __init__(self,vertex):
        self.vertex = vertex
    
    ##Util method to get number of vertices
    def __getitem__(self,key):
        if key == 'vertex':
            return self.vertex
    
    ##Takes an empty list and fills it with shape vertices coressponding to much 'vertex' is
    def assign_vertices(self,list):
        
        ##Cube Vertices
        if self.vertex == 8:
            list.append(np.array([-1, -1, 1]))
            list.append(np.array([1, -1, 1]))
            list.append(np.array([1,  1, 1]))
            list.append(np.array([-1, 1, 1]))
            list.append(np.array([-1, -1, -1]))
            list.append(np.array([1, -1, -1]))
            list.append(np.array([1, 1, -1]))
            list.append(np.array([-1, 1, -1]))
        ##Tetrahedron Vertices
        elif self.vertex == 4:
            list.append(np.array([0,1,-1]))
            list.append(np.array([1,1,1]))
            list.append(np.array([-1,1,1]))
            list.append(np.array([0,-1,0]))
        ##Octahedron Vertices
        elif self.vertex == 6:
            list.append(np.array([1, 0, 0]))   # Front vertex
            list.append(np.array([0, 1, 0]))   # Right vertex
            list.append(np.array([-1, 0, 0]))  # Back vertex
            list.append(np.array([0, -1, 0]))  # Left vertex
            list.append(np.array([0, 0, 1]))   # Top vertex
            list.append(np.array([0, 0, -1]))  # Bottom vertex
        ##Dodecahedron Vertices
        elif self.vertex == 20:
            ##Square Vertices
            list.append(np.array([1, 1, 1]))
            list.append(np.array([1, 1, -1]))
            list.append(np.array([1, -1, 1]))
            list.append(np.array([1, -1, -1]))
            list.append(np.array([-1, 1, 1]))
            list.append(np.array([-1, 1, -1]))
            list.append(np.array([-1, -1, 1]))
            list.append(np.array([-1, -1, -1]))
            
            ##12 Pentagons Vertices
            list.append(np.array([0, 1 / Shape.phi, Shape.phi]))
            list.append(np.array([0, 1 / Shape.phi, -Shape.phi]))
            list.append(np.array([0, -1 / Shape.phi, Shape.phi]))
            list.append(np.array([0, -1 / Shape.phi, -Shape.phi]))

            list.append(np.array([1 / Shape.phi, Shape.phi, 0]))
            list.append(np.array([1 / Shape.phi, -Shape.phi, 0]))
            list.append(np.array([-1 / Shape.phi, Shape.phi, 0]))
            list.append(np.array([-1 / Shape.phi, -Shape.phi, 0]))

            list.append(np.array([Shape.phi, 0, 1 / Shape.phi]))
            list.append(np.array([Shape.phi, 0, -1 / Shape.phi]))
            list.append(np.array([-Shape.phi, 0, 1 / Shape.phi]))
            list.append(np.array([-Shape.phi, 0, -1 / Shape.phi]))
        elif self.vertex == 12:
            list.append(np.array([1, Shape.phi, 0]))
            list.append(np.array([-1, Shape.phi, 0]))
            list.append(np.array([1, -Shape.phi, 0]))
            list.append(np.array([-1, -Shape.phi, 0]))
            list.append(np.array([0, 1, Shape.phi]))
            list.append(np.array([0, -1, Shape.phi]))
            list.append(np.array([0, 1, -Shape.phi]))
            list.append(np.array([0, -1, -Shape.phi]))
            list.append(np.array([Shape.phi, 0, 1]))
            list.append(np.array([-Shape.phi, 0, 1]))
            list.append(np.array([Shape.phi, 0, -1]))
            list.append(np.array([-Shape.phi, 0, -1]))
            
            
    #Prints the vertices in a vertex list
    def get_vertices_list(self,list):
        for lists in list:
            print(lists)


##shape_1 = Shape(8)
##print(shape_1['vertex'])
##shape_1.assign_vertices(vertices_list)
##shape_1.get_vertices_list(vertices_list)

        



