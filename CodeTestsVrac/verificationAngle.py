# -*- coding: utf-8 -*-
"""
Created on Wed May 15 14:36:16 2024

@author: leona
"""
import math as mt
import matplotlib.pyplot as plt
import pandas as pd
import time
import tkinter as tk
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import random
from PIL import Image, ImageTk
from moviepy.editor import VideoFileClip


#calcul de l'angle grâce au produit scalaire
def angle_between_points(xA, yA, zA, xB, yB, zB, xC, yC, zC):
    ux, uy, uz = xB - xA, yB - yA, zB - zA
    vx, vy, vz = xC - xA, yC - yA, zC - zA

    prod_scalaire = ux * vx + uy * vy + uz * vz
    norm_u = mt.sqrt(ux**2 + uy**2 + uz**2)
    norm_v = mt.sqrt(vx**2 + vy**2 + vz**2)

    cos_theta = prod_scalaire / (norm_u * norm_v)
    angle_radians = mt.acos(cos_theta)
    angle_degrees = mt.degrees(angle_radians)
    
    return angle_degrees





#définition des coordonnées des trois points d'exemple
x1 = 3
y1 = 2
z1 = 3

x2 = 1
y2 = 2
z2 = 3

x3 = 3.3
y3 = 2
z3 = 2.92

x4 = 3.08
y4 = 2
z4 = 2.7

print( "\tPosition PtA : [%3.2f, %3.2f, %3.2f]"% (x1, y1, z1 ))
print( "\tPosition PtB : [%3.2f, %3.2f, %3.2f]"% (x2, y2, z2 ))
print( "\tPosition PtC : [%3.2f, %3.2f, %3.2f]"% (x3, y3, z3 ))

y1 = 0
y2 = 0
y3 = 0
y4 = 0

#print(z3)
alphaG = 180 - angle_between_points(x1, y1, z1, x2, y2, z2, x3, y3, z3)
print(f"alphaG : %3.2f degrés"%alphaG)
alphaD = angle_between_points(x1, y1, z1, x2, y2, z2, x4, y4, z4) - 90
print(f"alphaD : %3.2f degrés"%alphaD)


