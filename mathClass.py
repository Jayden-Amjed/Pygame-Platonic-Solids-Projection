import pygame
import numpy as np
from math import *

class mathUtil:
    ##Class variable to hold rotated points
    rotated_points = []
    i = 0
    
    ##Projection Matrix
    projection_matrix = np.array([
    [1, 0, 0],
    [0, 1, 0]
    ])
    
    ##Sets scale for how far apart points should be relative to screen
    scale = 150
    
    ##Makes an empty list as big as the list entered
    @staticmethod
    def fill_list(verteces_number):
        new_list = [[n, n] for n in range(len(verteces_number))]
        return new_list
    
    ##Takes 4 lists, 3 being the rotation matrices, 1 being the shape_list with its original vertices
    #Resets rotated_points everytime its called
    #For every (vertex(x,y,z)) in the shape_list, it applies a rotation about x,y,z, then multiplies it by projection matrix (Flattens Z axis)
    #Takes new vertex(x,y) and puts it a variable thats then appended to rotated_points
    
    def rotate_list_for_light(list_z,list_x,list_y,shape_list):
        mathUtil.rotated_points = []
        for items in shape_list:
            rotated_list = np.dot(list_z, items)
            rotated_list = np.dot(list_x, rotated_list)
            rotated_list = np.dot(list_y, rotated_list)
            mathUtil.rotated_points.append(rotated_list)
        return mathUtil.rotated_points
    
    ##Takes list of shape vertices and mutiplies it by each rotation matrix
    @staticmethod
    def rotate_list(list_z,list_x,list_y,shape_list):
        mathUtil.rotated_points = []
        for items in shape_list:
            rotated_list = np.dot(list_z, items.reshape((3, 1)))
            rotated_list = np.dot(list_x, rotated_list)
            rotated_list = np.dot(list_y, rotated_list)
            cord_2d = np.dot(mathUtil.projection_matrix,rotated_list)
            mathUtil.rotated_points.append(cord_2d)
        return mathUtil.rotated_points
    
    ##Takes a list =[x,y],[x,y],[0,1]
    #For every poin in list, assigns x as [0], assings y = [1]
    ##Uses pygame funciton to draw the points
    
    @staticmethod
    def draw_x_y_cords(list,x_y_points_list,screen,color):
        mathUtil.i = 0
        for points in list:
            x = int(points[0] * mathUtil.scale) + 600 #center
            y = int(points[1] * mathUtil.scale) + 500 #center
            
            x_y_points_list[mathUtil.i] = [x,y]
            pygame.draw.circle(screen,color,(x,y),5)
            mathUtil.i += 1
    
    #Takes a list= [x,y],two indexes
    #Uses index to get (x,y)1 and (x,y)2 then draws a line between them
    @staticmethod
    def connect_two_points(i,j,x_y_points_list,screen,color):
        pygame.draw.line(screen, color, (x_y_points_list[i][0], x_y_points_list[i][1]), (x_y_points_list[j][0], x_y_points_list[j][1]))
    
    
    @staticmethod
    def connect_dodecahedron_points(projected_points,screen,color):
        pentagon_indices = [
        ##Each set marks vertices for a pentagon
        [2, 16, 17, 3, 13],   
        [7, 11, 3, 13, 15],  
        [6, 15, 7, 19, 18],    
        [6, 10, 2, 13, 15],   
        [3, 17, 1, 9, 11], 

        [7, 11, 9, 5, 19], 
        [5, 19, 18, 4, 14],  
        [2, 16, 0, 8, 10],  
        [1, 12, 0, 16, 17], 
        [4, 8, 0, 12, 14],  
    ]
    # Draw each pentagon based on the defined indices
        for pentagon in pentagon_indices:
            for i in range(len(pentagon)):
                start_point = pentagon[i]
                end_point = pentagon[(i + 1) % len(pentagon)]  # Wrap around to the start
                mathUtil.connect_two_points(start_point, end_point, projected_points, screen, color)
    
    @staticmethod
    def connect_icosahedron_points(projected_points,screen,color):
        triangle_indices = [
        ##Each set marks vertices for a triangle
        [1, 11, 6,],
        [11, 6, 7,],
        [1, 6, 0,],
        [8, 4, 5,],
        [6, 7, 10,],
        [6, 0, 10,],
        [8, 2, 10,],
        [7, 3, 2,],
        [8, 10, 0,],
        [1, 11, 6,],
        [5, 2, 8,],
        [3, 7, 11,],
        [11, 3, 9,],
        [1, 11, 9,],
        [0, 4, 1,],
        [9, 3, 5,],
        [1, 4, 9,],                   
        
    ]
    # Draw each triangle based on the defined indices
        for triangle in triangle_indices:
            for i in range(len(triangle)):
                start_point = triangle[i]
                end_point = triangle[(i + 1) % len(triangle)]  # Wrap around to the start
                mathUtil.connect_two_points(start_point, end_point, projected_points, screen, color)
    
    
    @staticmethod
    def connect_octahedron_points(projected_points,screen,color):
        base_point_count_1 = len(projected_points) - 2 ## -2 point is top point
        base_point_count_2 = len(projected_points) - 1 ## -1 point is bottom point
        
        for i in range(base_point_count_1):
            next_index = (i + 1) % base_point_count_1  # Wrap around to create the closed base
            mathUtil.connect_two_points(i, next_index, projected_points, screen, color)
            mathUtil.connect_two_points(i,base_point_count_1,projected_points,screen,color) ##Connect points to top
            mathUtil.connect_two_points(i,base_point_count_2,projected_points,screen,color) ##Connect points to bottom

            
    
    
    @staticmethod
    def connect_tertrahedron_points(projected_points,screen,color):
        base_point_count = len(projected_points) - 1  # Assume last point is the top point
        for i in range(base_point_count):
            next_index = (i + 1) % base_point_count  # Wrap around to create the closed base
            mathUtil.connect_two_points(i, next_index, projected_points, screen, color)

        # Connect each base point to the top point
            mathUtil.connect_two_points(i, base_point_count, projected_points, screen, color)
    
    
    @staticmethod
    def connect_cube_points(vertex,projected_points,screen,color):
        for i in range(int(vertex/2)):
            mathUtil.connect_two_points(i, (i+1) % 4, projected_points,screen,color)
            mathUtil.connect_two_points(i+4, ((i+1) % 4) + 4, projected_points,screen,color)
            mathUtil.connect_two_points(i, (i+4), projected_points,screen,color)