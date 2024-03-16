import sys
import pygame
import math
import numpy as np

pygame.init()

#colous
white = (255, 255, 255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (250,230,50)
cyan = (0,220,220)
magenta = (255,0,255)

#initialize window 
WIDTH = 1000
HIEGHT = 1000

screen = pygame.display.set_mode((WIDTH, HIEGHT))
title = "Mesh Renderer"
pygame.display.set_caption(title)

clock = pygame.time.Clock()

frameRate = 60

#SETUP
# import mesh from obj file 
def importObj(file):
  verts = []
  faces = []
  
  with open(file,"r") as readfile:
    line = readfile.readline().rstrip('\n')
    
    while line:
      items = line.split(" ")
      if items[0] == "v":
        verts.append((float(items[1]), float(items[2]) ,float(items[3])))
      elif items[0] == "f":
        faces.append((int(items[1]), int(items[2]) ,int(items[3])))

      line = readfile.readline().rstrip('\n')
      
  return verts, faces


def genGube():
  points = [(0.0, 0.0, 0.0),
            (1.0, 0.0, 0.0),
            (0.0, 1.0, 0.0),
            (1.0, 1.0, 0.0),
            (0.0, 0.0, 1.0),
            (1.0, 0.0, 1.0),
            (0.0, 1.0, 1.0),
            (1.0, 1.0, 1.0)]
  
  triangles = [(0,2,1),
               (3,1,2),
               (1,3,5),
               (7,5,3),
               (5,7,4),
               (6,4,7),
               (6,2,7),
               (3,7,2),
               (0,4,2),
               (6,2,4),
               (0,1,4),
               (5,4,1),]
  
  return points, triangles


# define rotation matricies
def rotmatX(vert,angle):
  sin0 = math.sin(angle)
  cos0 = math.cos(angle)
  
  rotMat = np.array([[1,      0,      0],
                  [0,    cos0, -sin0],
                  [0,    sin0,  cos0]])
  
  v = np.array([vert[0],vert[1],vert[2]])

  point = np.matmul(rotMat, v)

  x = point[0]
  y = point[1]
  z = point[2]

  return (x,y,z)


def rotmatY(vert,angle):
  sin0 = math.sin(angle)
  cos0 = math.cos(angle)
  
  rotMat = np.array([[cos0,   0,   sin0],
                     [0,      1,      0],
                     [-sin0,  0,   cos0]])
  
  v = np.array([vert[0],vert[1],vert[2]])

  point = np.matmul(rotMat, v)

  x = point[0]
  y = point[1]
  z = point[2]

  return (x,y,z)


def rotmatZ(vert,angle):
  sin0 = math.sin(angle)
  cos0 = math.cos(angle)
  
  rotMat = np.array([[cos0,  -sin0,   0],
                     [sin0,  cos0,    0],
                     [0,      0,      1]])

  v = np.array([vert[0],vert[1],vert[2]])

  point = np.matmul(rotMat, v)

  x = point[0]
  y = point[1]
  z = point[2]

  return (x,y,z)


# project point
def projectPoint(point):
  x = point[0]
  y = point[1]
  z = point[2] + 2

  #get aspect ratio
  asp = WIDTH / HIEGHT

  #define fov angle
  fov = math.pi / 2

  #define scaling factor for points
  scale = HIEGHT / 3 #(-1 - 1 takes up 1/3 of screen)

  inTan = 1/math.tan(fov/2)

  #find ratio of half width of frustrum intersection at z coordinate to x/y distance from 0,0 line 
  # this is done in order to calculate portion of screen space
  if z:
    projx = x  / (inTan * z)
    projy = y / (inTan * z)
  else:
    projx = x  / (inTan)
    projy = y / (inTan)
    
  #find screen co-ords of projected points with 0,0 as screen centre 
  projx = projx * asp * scale + WIDTH/2
  projy = projy * scale + HIEGHT/2

  projPoint = (projx,projy)

  return projPoint




verts, tris = genGube()

while True:
#INPUT DETECTION
  for event in pygame.event.get():
      #close window
      if event.type == pygame.QUIT:
          sys.exit()
      
  screen.fill(black)


  for vert in verts:
    point = projectPoint(vert)
    pygame.draw.circle(screen,white,point,5)


  for i in range(len(verts)):
    verts[i] = rotmatX(verts[i], math.pi/300)
    #verts[i] = rotmatY(verts[i], math.pi/150)
    verts[i] = rotmatZ(verts[i], math.pi/200)

  clock.tick(frameRate)
  pygame.display.update()



#CALCULATIONS
                    #   rotate triangles
                    #       numpy matmul with each point againt rot mat

#   find normals
#       find edge vectors
#       numpy cross product

#   project valid triangles
#       numpy dot prod with vector to "camera"
#       if dot prod < 0 then comense
                    #       project points to screen space

#   shade triangles
#       init light vector(s)
#       Shade triangles depending on normal light dot prod


#DRAW TRIANGLES


#OPTIMIZATIONS

