import pygame
import numpy as np
import math

#SETUP
#   import mesh from mesh file that contains vertex face and normal data
#       file format:
#         v point1
#         v point2
#         v point3
#            ...
#         f pointA pointB pointC
#         f pointA pointB pointC
#         f pointA pointB pointC
#            ...
#         n x y z
#         n x y z
#         n x y z
#            ...
#
#         eg.
#         v 1.0, 0.0, 1.0 (x, y, z position)
#         v 3.0, 1.0, 1.0
#            ...
#         f 1, 2, 3 (each element is a corresponding vertex index)
#            ...
#         v 3, 1, 1

# POINTS ARE LABELED CLOCKWISE (when facing from exterior)

#   initialize triangles
#   define rotation matricies
#   define projection matrix


#CALCULATIONS
#   rotate triangles
#       numpy matmul with each point againt rot mat

#   find normals if not included
#       numpy cross product

#   project valid triangles
#       numpy dot prod with vector to 
#       if dot prod < 0 then comense
#       numpy matmul with each point againt proj mat

#DRAW TRIANGLES


#OPTIMIZATIONS

