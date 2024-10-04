# -*- coding: utf-8 -*-
"""
Created on Wed May 15 17:04:21 2024

@author: leona
"""

import tkinter as tk
from tkinter import *
import math as mt


def changeTriangles():
    angle_degrees = ALPHA.get()
    print(angle_degrees)
    
    # Convertir l'angle en radians
    angle_radians = mt.radians(angle_degrees)
    
    side_length = 100
    x = 250
    y = 50
    
    delta = side_length * mt.tan(angle_radians)

    # Calculer les coordonnées des sommets du triangle en fonction de l'angle donné
    x1 = x
    y1 = y
    x2 = x + side_length
    y2 = y - delta
    x3 = x + side_length
    y3 = y + delta
    
    
    x4 = x + delta
    y4 = y + side_length
    x5 = x - delta
    
    x6 = x-100
    x7 = x6 - side_length
    
    x9 = x6 - delta
    x10 = x6 + delta
    
    canvas.coords(trig1, x1, y1, x2, y2, x3, y3)
    canvas.coords(trig2, x1, y1, x4, y4, x5, y4)
    canvas.coords(trig3, x6, y, x7, y2, x7, y3)
    canvas.coords(trig4, x6, y, x9, y4, x10, y4)



# Fonction principale pour créer et afficher la fenêtre Tkinter avec le triangle 
#rempli en vert


# Créer une fenêtre Tkinter
root = tk.Tk()
root.title("Triangle rempli en vert avec un angle précis")
# Spécifier la taille du canevas
canvas_width = 400
canvas_height = 300
# Créer un canevas avec la taille spécifiée
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="grey")
canvas.pack()


#détermination de alpha
global ALPHA
ALPHA = IntVar()
entree = Entry(root, textvariable=ALPHA)
entree.pack()


boutonAlpha = Button(root, text="valider",command=changeTriangles)
boutonAlpha.pack()

trig1 = canvas.create_polygon(0, 0, 0, 0, 0, 0, fill="green", outline="black")
trig2 = canvas.create_polygon(0, 0, 0, 0, 0, 0, fill="green", outline="black")
trig3 = canvas.create_polygon(0, 0, 0, 0, 0, 0, fill="green", outline="black")
trig4 = canvas.create_polygon(0, 0, 0, 0, 0, 0, fill="green", outline="black")

# Coordonnées du point de départ du triangle
start_x = 250
start_y = 50

# Longueur du côté du triangle
#side_length = 100

# Angle du triangle en degrés
angle_degrees = 0

# Dessiner le triangle rempli en vert avec l'angle spécifié
#draw_triangle_with_angle(canvas, start_x, start_y, side_length, angle_degrees)


# Lancer la boucle principale Tkinter
root.mainloop()
