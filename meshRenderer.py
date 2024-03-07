import pygame
import numpy as np
import math

#SETUP
#   import mesh from obj file 
#   init points array
#   init triangles array

#   init triangles

#   define rotation matricies
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

