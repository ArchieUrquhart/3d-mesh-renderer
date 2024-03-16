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
  points = [(0.0, 0.0, 0.0),#0
            (1.0, 0.0, 0.0),#1
            (0.0, 1.0, 0.0),#2#
            (1.0, 1.0, 0.0),#3#
            (0.0, 0.0, 1.0),#4
            (1.0, 0.0, 1.0),#5
            (0.0, 1.0, 1.0),#6#
            (1.0, 1.0, 1.0)]#7#
  
  triangles = [(0,2,1),#0
               (3,1,2),#1
               (1,3,5),#2
               (7,5,3),#3
               (5,7,4),#4
               (6,4,7),#5
               (6,7,2),#6
               (3,2,7),#7
               (0,4,2),#8
               (6,2,4),#9
               (0,1,4),#10
               (5,4,1),]#11
  
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


# project any 3d point to 2d screen
def projectPoint(point):
  zdist = 2
  x = point[0]
  y = point[1]
  z = point[2] + zdist

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
  projy = projy * -scale + HIEGHT/2

  projPoint = (projx,projy)

  return projPoint



def normalize(vector):
  #calculates magnitude of vector then divides up components by said magnitute
  mag = math.sqrt(vector[0] **2 + vector[1] **2 + vector[2] **2)
  x = vector[0] / mag
  y = vector[1] / mag
  z = vector[2] / mag

  normalized = np.array([x,y,z])

  return normalized

# gets the vector between two given points
def getVector(a,b):
  x = b[0] - a[0]
  y = b[1] - a[1]
  z = b[2] - a[2]

  return [x, y, z]


def getNormal(triangle):
  #gets all verticies of the given triangle
  p0 = verts[triangle[0]]
  p1 = verts[triangle[1]]
  p2 = verts[triangle[2]]

  #calcutes the vectors from the corder of triangle to the other points
  v0 = np.array(getVector(p0,p1))
  v1 = np.array(getVector(p0,p2))

  normal = np.cross(v0, v1)
  #normal = normalize(normal)

  return normal


def checkTris():
  validtris = []
  validverts = []

  for triangle in tris:
    camvec = np.array([verts[triangle[0]][0],verts[triangle[0]][1],verts[triangle[0]][2]+2])
    normal = getNormal(triangle)
    dotprod = np.dot(camvec, normal)

    if dotprod < 0:
      validtris.append(triangle)
      for point in range(3):
        validverts.append(verts[triangle[point]])

  return validtris, validverts


verts, tris = genGube()
points = [None]*len(verts)


while True:
#INPUT DETECTION
  for event in pygame.event.get():
      #close window
      if event.type == pygame.QUIT:
          sys.exit()
      
  screen.fill(black)

  
  for i in range(len(verts)):
    verts[i] = rotmatX(verts[i], math.pi/200)
    verts[i] = rotmatY(verts[i], math.pi/150)
    verts[i] = rotmatZ(verts[i], math.pi/300)

  validtris, validverts = checkTris()

  for i in range(len(verts)):
    if verts[i] in validverts:
      points[i] = projectPoint(verts[i])
      pygame.draw.circle(screen,white,points[i],3)


  for triangle in tris:
    if triangle in validtris:
      verticies = [points[triangle[0]], points[triangle[1]], points[triangle[2]]]
      pygame.draw.polygon(screen, white, verticies, 3)


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

