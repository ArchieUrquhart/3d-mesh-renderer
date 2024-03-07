import pygame
import numpy as np
import math

#SETUP
#   import mesh from obj file 
#   init points array
#   init triangles array

#   init triangles

#   define rotation matricies

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

