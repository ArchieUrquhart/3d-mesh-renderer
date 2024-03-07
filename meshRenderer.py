import pygame
import numpy as np
import math

#SETUP
# import mesh from obj file 
def importObj(file):
  verts = []
  faces = []
  
  with open(file,"r") as readfile:
    line = readfile.readline().rstrip('\n')
    
    while line:
      items = line.split(" ")
      if items[0] = "v":
        verts.append((float(items[1]), float(items[2]) ,float(items[3])))
      elif items[0] = "f":
        faces.append((int(items[1]), int(items[2]) ,int(items[3])))

      line = readfile.readline().rstrip('\n')
      
  return verts, faces


# define rotation matricies
def rotmatX(angle):
  sin0 = math.sin(angle)
  cos0 = math.cos(angle)
  
  Rx = np.matrix([[1,      0,      0],
                  [0,    cos0, -sin0],
                  [0,    sin0,  cos0]])
  
  return Rx


def rotmatY(angle):
  sin0 = math.sin(angle)
  cos0 = math.cos(angle)
  
  Ry = np.matrix([[cos0,   0,   sin0],
                  [0,      1,      0],
                  [-sin0,  0,   cos0]])
  return Ry


def rotmatZ(angle):
  sin0 = math.sin(angle)
  cos0 = math.cos(angle)
  
  Rz = np.matrix([[cos0,  -sin0,   0],
                  [sin0,  cos0,    0],
                  [0,      0,      1]])

  return Rz
  



#   define projection matrix


#CALCULATIONS
#   rotate triangles
#       numpy matmul with each point againt rot mat

#   find normals
#       find edge vectors
#       numpy cross product

#   project valid triangles
#       numpy dot prod with vector to "camera"
#       if dot prod < 0 then comense
#       numpy matmul with each point againt proj mat

#   shade triangles
#       init light vector(s)
#       Shade triangles depending on normal light dot prod


#DRAW TRIANGLES


#OPTIMIZATIONS

