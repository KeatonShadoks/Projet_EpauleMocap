# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:42:11 2024

@author: leona
"""

import math
import matplotlib.pyplot as plt

#calcul de l'angle grâce au produit scalaire
def angle_between_points(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    ux, uy, uz = x2 - x1, y2 - y1, z2 - z1
    vx, vy, vz = x3 - x1, y3 - y1, z3 - z1

    dot_product = ux * vx + uy * vy + uz * vz
    norm_u = math.sqrt(ux**2 + uy**2 + uz**2)
    norm_v = math.sqrt(vx**2 + vy**2 + vz**2)

    cos_theta = dot_product / (norm_u * norm_v)
    angle_radians = math.acos(cos_theta)
    angle_degrees = math.degrees(angle_radians)
    
    return angle_degrees


#définition des coordonnées des trois points
x1 = 0
y1 = 0
z1 = 0

x2 = 0
y2 = 3
z2 = 0

x3 = 2
y3 = 0
z3 = 0

print(angle_between_points(x1, y1, z1, x2, y2, z2, x3, y3, z3))



#affichage des points en 3d
ax = plt.axes(projection="3d")
ax.scatter(x1,y1,z1)
ax.scatter(x2,y2,z2)
ax.scatter(x3,y3,z3)
plt.show





