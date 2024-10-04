# -*- coding: utf-8 -*-
"""
Created on Sun May  5 19:48:09 2024

@author: leona
"""

import tkinter as tk
import math

# Fonction pour dessiner le triangle avec l'angle spécifié
def dessiner_triangle(angle):
    # Effacer le dessin précédent
    canvas.delete("all")

    # Calculer les coordonnées des points du triangle
    x1, y1 = 150, 50  # Sommet supérieur
    x2, y2 = 50, 250   # Coin inférieur gauche
    x3, y3 = 250, 250  # Coin inférieur droit

    # Décaler le coin inférieur gauche pour faire varier l'angle
    x2 = x1 - int(math.tan(math.radians(angle)) * (y2 - y1))
    
    # Dessiner le triangle
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill='lightblue', outline='black', width=2)

# Fonction appelée lorsqu'on appuie sur le bouton
def update_triangle():
    try:
        angle = float(angle_entry.get())
        if 0 <= angle <= 180:
            dessiner_triangle(angle)
        else:
            raise ValueError("L'angle doit être entre 0 et 180 degrés.")
    except ValueError as e:
        print("Erreur :", e)

# Créer la fenêtre principale
root = tk.Tk()
root.title("Dessiner un triangle avec un angle")

# Créer un canevas pour dessiner le triangle
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Entrée pour saisir l'angle
angle_label = tk.Label(root, text="Angle (degrés) :")
angle_label.pack(pady=10)
angle_entry = tk.Entry(root)
angle_entry.pack(pady=5)

# Bouton pour mettre à jour le triangle
update_button = tk.Button(root, text="Mettre à jour", command=update_triangle)
update_button.pack(pady=10)

# Exemple initial avec un angle de 60 degrés
dessiner_triangle(60)

# Lancer la boucle principale
root.mainloop()
