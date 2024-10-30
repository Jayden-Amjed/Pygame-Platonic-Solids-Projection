import pygame
from shapeClass import Shape
import numpy as np
from math import *
from mathClass import mathUtil
from rotationClass import Rotation
from textMakerClass import Text

pygame.init()

##GLOBAL VARIABLES
WIDTH, HEIGHT = 1200, 1000 #Sets width and height for game display
WHITE = (255, 255, 255) #Global white color
RED = (255, 0, 0) #Global red color
BLACK = (0, 0, 0) #Global Black color
BLUE = (0,0,255) #Global Blue color
GREEN = (0,128,0) #Global Green color
SKY_BLUE = (135,206,235)

#TEXT STUFF
text_message = Text(None,'Start by clicking on a shape!',38,None,None)
text_message.create_text(WHITE,WIDTH/2,100)
box_rect_text_message = []
box_rect_text_message = text_message.create_padding(10,box_rect_text_message)

##Cube Button
text_cube = Text(None,'Cube',32,None,None)
text_cube.create_text(WHITE,1100,150)
box_rect_text_cube = []
box_rect_text_cube = text_cube.create_padding(10,box_rect_text_cube)

##Tetrahedron Button
text_tetrahedron = Text(None,'Tetrahedron',32,None,None)
text_tetrahedron.create_text(WHITE,1100,100)
box_rect_text_tetrahedron = []
box_rect_text_tetrahedron = text_tetrahedron.create_padding(10,box_rect_text_tetrahedron)

##Octahedron Button
text_octahedron = Text(None, 'Octahedron' , 32, None, None)
text_octahedron.create_text(WHITE,1100,200)
box_rect_text_octahedron = []
box_rect_text_octahedron = text_octahedron.create_padding(10,box_rect_text_octahedron)

##Dodecahedron Button
text_dodecahedron = Text(None, 'Dodecahedron' , 32, None, None)
text_dodecahedron.create_text(WHITE,1100,300)
box_rect_text_dodecahedron = []
box_rect_text_dodecahedron = text_dodecahedron.create_padding(10,box_rect_text_dodecahedron)

##Icosahedron Button
text_icosahedron = Text(None, 'Icosahedron' , 32, None, None)
text_icosahedron.create_text(WHITE,1100,250)
box_rect_text_icosahedron = []
box_rect_text_icosahedron = text_icosahedron.create_padding(10,box_rect_text_icosahedron)



##List where vertices of the selected shape are held
vertices_list_square = [] 
vertices_list_tetrahedron = []
vertices_list_octahedron = []
vertices_list_dodecahedron = []
vertices_list_icosahedron = []
##Creates rotation object to access Rotation() methods
rotation_object = Rotation()

pygame.display.set_caption("2D Projection of Platonic Solids") ##Sets the title of the window
screen = pygame.display.set_mode((WIDTH, HEIGHT)) ## Making screen

##Makes a clock using pygame clock libary
clock = pygame.time.Clock()




##Creates Shapes
tetrahedron = Shape(4)
tetrahedron.assign_vertices(vertices_list_tetrahedron)
tetrahedron.get_vertices_list(vertices_list_tetrahedron)
projected_points_tetrahedron = mathUtil.fill_list(vertices_list_tetrahedron)

square = Shape(8)
square.assign_vertices(vertices_list_square)
square.get_vertices_list(vertices_list_square)
projected_points_square = mathUtil.fill_list(vertices_list_square)

octahedron = Shape(6)
octahedron.assign_vertices(vertices_list_octahedron)
projected_points_octahedron = mathUtil.fill_list(vertices_list_octahedron)

dodecahedron = Shape(20)
dodecahedron.assign_vertices(vertices_list_dodecahedron)
projected_points_dodecahedron = mathUtil.fill_list(vertices_list_dodecahedron)

icosahedron = Shape(12)
icosahedron.assign_vertices(vertices_list_icosahedron)
projected_points_icosahedron = mathUtil.fill_list(vertices_list_icosahedron)

icosahedron_handler = False
dodecahedron_handler = False
octahedron_handler = False
pause = False
tetrahedron_handler = False
cube_handler = False

while True:

    
    clock.tick(60) # sets the game to 60 fps
    
    #If you press escape or exit button, games closes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_poistion = pygame.mouse.get_pos()
            if text_cube.check_for_hover(mouse_poistion):
                print('Cube Button Clicked: Rendering Cube')
                cube_handler = not cube_handler   
            if text_tetrahedron.check_for_hover(mouse_poistion):
                print('tetrahedron Button Clicked')
                tetrahedron_handler = not tetrahedron_handler
            if text_octahedron.check_for_hover(mouse_poistion):
                print('Octahedron Button Clicked')
                octahedron_handler = not octahedron_handler
            if text_dodecahedron.check_for_hover(mouse_poistion):
                print('Dodecahedron Button Clicked')
                dodecahedron_handler = not dodecahedron_handler
            if text_icosahedron.check_for_hover(mouse_poistion):
                print('Icosahedron Button Clicked')
                icosahedron_handler = not icosahedron_handler
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
        
    #Makes background white
    screen.fill(BLACK)    
    
    ##DRAWS TEXT
    text_message.draw_text(screen,BLACK,box_rect_text_message)
    text_cube.draw_text(screen,RED,box_rect_text_cube)
    text_tetrahedron.draw_text(screen,RED,box_rect_text_tetrahedron)
    text_octahedron.draw_text(screen,RED,box_rect_text_octahedron)
    text_dodecahedron.draw_text(screen,RED,box_rect_text_dodecahedron)
    text_icosahedron.draw_text(screen,RED,box_rect_text_icosahedron)
    
    ##Creates Rotation Matrices
    rotation_z = rotation_object.rotation_z()
    rotation_y = rotation_object.rotation_y()
    rotation_x = rotation_object.rotation_z()
    
    if pause == False:
        rotation_object.angle_incremenation() ##Increments angle by 0.01 after every frame
    
    if cube_handler == True:
        text_cube.draw_text(screen,GREEN,box_rect_text_cube)
        #Sets rotated_cube_points to new angle increments,draws new points,connects new points
        rotated_cube_points = mathUtil.rotate_list(rotation_z,rotation_x,rotation_y,vertices_list_square)
        mathUtil.draw_x_y_cords(rotated_cube_points,projected_points_square,screen,RED) ## Draws the points using rotated_list
        mathUtil.connect_cube_points(square["vertex"],projected_points_square,screen,WHITE)
    
    if tetrahedron_handler == True:
        text_tetrahedron.draw_text(screen,GREEN,box_rect_text_tetrahedron)
        #Sets rotated_prism_points to new angle increments,draws new points,connects new points
        rotated_tetrahedron_points = mathUtil.rotate_list(rotation_z,rotation_x,rotation_y,vertices_list_tetrahedron)
        rotated_tetrahedron_points_light = mathUtil.rotate_list_for_light(rotation_z,rotation_x,rotation_y,vertices_list_tetrahedron)
        mathUtil.draw_x_y_cords(rotated_tetrahedron_points,projected_points_tetrahedron,screen,RED)
        mathUtil.connect_tertrahedron_points(projected_points_tetrahedron,screen,WHITE)
        Text.draw_vertex_number(projected_points_tetrahedron,20,BLACK,WHITE,screen)
              
    if octahedron_handler == True:
        text_octahedron.draw_text(screen,GREEN,box_rect_text_octahedron)
        rotated_octahedron_points = mathUtil.rotate_list(rotation_z,rotation_x,rotation_y,vertices_list_octahedron)
        mathUtil.draw_x_y_cords(rotated_octahedron_points,projected_points_octahedron,screen,RED)
        mathUtil.connect_octahedron_points(projected_points_octahedron,screen,WHITE)
    
    if dodecahedron_handler == True:
        text_dodecahedron.draw_text(screen,GREEN,box_rect_text_dodecahedron)
        rotated_dodecahedron_points = mathUtil.rotate_list(rotation_z,rotation_x,rotation_y,vertices_list_dodecahedron)
        mathUtil.draw_x_y_cords(rotated_dodecahedron_points,projected_points_dodecahedron,screen,RED)
        mathUtil.connect_dodecahedron_points(projected_points_dodecahedron,screen,WHITE)
    
    if icosahedron_handler == True:
        text_icosahedron.draw_text(screen,GREEN,box_rect_text_icosahedron)
        rotated_icosahedron_points = mathUtil.rotate_list(rotation_z,rotation_x,rotation_y,vertices_list_icosahedron)
        mathUtil.draw_x_y_cords(rotated_icosahedron_points,projected_points_icosahedron,screen,RED)
        mathUtil.connect_icosahedron_points(projected_points_icosahedron,screen,WHITE)     

    
    #Updates game 60 times a second
    pygame.display.update()