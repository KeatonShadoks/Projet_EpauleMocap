# -*- coding: utf-8 -*-
"""
Created on Sun May  5 19:53:25 2024

@author: leona
"""

import tkinter as tk
import math

# Fonction pour dessiner les deux droites et l'angle entre elles
def dessiner_angle(angle):
    # Effacer le dessin précédent
    canvas.delete("all")

    # Taille du canevas
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    # Coordonnées des points pour les droites
    x1, y1 = width * 0.2, height * 0.5
    x2, y2 = width * 0.8, height * 0.5

    # Dessiner la première droite
    canvas.create_line(x1, y1, x2, y2, fill='blue', width=2)

    # Calculer les coordonnées pour la deuxième droite en fonction de l'angle
    angle_radians = math.radians(angle)
    x3 = x1 + math.cos(angle_radians) * (x2 - x1)
    y3 = y1 - math.sin(angle_radians) * (y1 - y2)

    # Dessiner la deuxième droite
    canvas.create_line(x1, y1, x3, y3, fill='red', width=2)

    # Calculer les coordonnées pour l'arc représentant l'angle
    start_angle = math.degrees(math.atan2(y1 - y3, x3 - x1))
    extent_angle = -angle  # Négatif car tkinter tourne dans le sens contraire des aiguilles d'une montre

    # Dessiner l'arc représentant l'angle
    canvas.create_arc(x1-30, y1-30, x1+30, y1+30, start=start_angle, extent=extent_angle, style='arc', outline='green', width=2)

# Fonction appelée lorsqu'on appuie sur le bouton
def update_angle():
    try:
        angle = float(angle_entry.get())
        dessiner_angle(angle)
    except ValueError:
        print("Veuillez entrer un nombre valide pour l'angle.")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Visualisation de l'angle entre deux droites")

# Créer un canevas pour dessiner les droites et l'angle
canvas = tk.Canvas(root, width=400, height=300, bg='white')
canvas.pack(padx=20, pady=20)

# Entrée pour saisir l'angle
angle_label = tk.Label(root, text="Angle (degrés) :")
angle_label.pack()
angle_entry = tk.Entry(root)
angle_entry.pack()

# Bouton pour mettre à jour l'angle
update_button = tk.Button(root, text="Mettre à jour", command=update_angle)
update_button.pack(pady=10)

# Exemple initial avec un angle de 45 degrés
dessiner_angle(45)

# Lancer la boucle principale
root.mainloop()
