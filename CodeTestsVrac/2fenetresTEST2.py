# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:39:35 2024

@author: leona
"""

import tkinter as tk
import math
from PIL import Image, ImageTk

def update_graphics(*args):
    angle = float(angle_var.get())
    
    # Calculer les nouvelles coordonnées en fonction de l'angle
    radius = 50
    center_x, center_y = 150, 100
    x = center_x + radius * math.cos(math.radians(angle))
    y = center_y + radius * math.sin(math.radians(angle))
    
    # Mettre à jour le texte et le point dans la fenêtre principale
    label_angle.config(text=f"Angle : {angle}°")
    main_canvas.coords(point_id_main, x - 5, y - 5, x + 5, y + 5)

    # Mettre à jour la nouvelle fenêtre si elle existe
    if new_window and new_window.winfo_exists():
        new_window.label_angle.config(text=f"Angle : {angle}°")
        new_window.canvas.coords(new_window.point_id, x - 5, y - 5, x + 5, y + 5)

def open_new_window():
    global new_window
    if new_window and new_window.winfo_exists():
        new_window.deiconify()
        return
    
    new_window = tk.Toplevel(root)
    new_window.title("Fenêtre Patient")
    new_window.geometry("700x600")
    
    image_path = "AnimationAvatar/shema5.png"
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    new_window.canvas = tk.Canvas(new_window, width=image.width, height=image.height)
    new_window.canvas.pack()
    new_window.canvas.create_image(0, 0, image=photo, anchor=tk.NW)
    
    angle = float(angle_var.get())
    radius = 50
    center_x, center_y = image.width // 2, image.height // 2
    x = center_x + radius * math.cos(math.radians(angle))
    y = center_y + radius * math.sin(math.radians(angle))
    
    new_window.point_id = new_window.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red")
    new_window.image = photo
    new_window.label_angle = tk.Label(new_window, text=f"Angle : {angle}°")
    new_window.label_angle.pack()

def calculate_angle():
    # Effectuez ici votre calcul complexe pour déterminer l'angle
    angle = (angle_var.get() + 45) % 360  # Juste un exemple de calcul
    angle_var.set(angle)  # Met à jour la variable avec le nouvel angle

root = tk.Tk()
root.title("Fenêtre Principale")

# Variable pour l'angle
angle_var = tk.DoubleVar(value=0)

# Ajouter un bouton pour ouvrir la nouvelle fenêtre
open_button = tk.Button(root, text="Ouvrir Fenêtre Patient", command=open_new_window)
open_button.pack()

# Ajouter un label pour afficher l'angle actuel
label_angle = tk.Label(root, text=f"Angle : {angle_var.get()}°")
label_angle.pack()

# Ajouter un bouton pour recalculer l'angle
calc_button = tk.Button(root, text="Calculer Angle", command=calculate_angle)
calc_button.pack()

# Créer un canevas dans la fenêtre principale
main_canvas = tk.Canvas(root, width=300, height=200)
main_canvas.pack()

# Initialiser le point sur le canevas principal
center_x, center_y = 150, 100
initial_angle = angle_var.get()
x = center_x + 50 * math.cos(math.radians(initial_angle))
y = center_y + 50 * math.sin(math.radians(initial_angle))
point_id_main = main_canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red")

# Associer la fonction de mise à jour à la variable d'angle
angle_var.trace("w", update_graphics)

new_window = None

root.mainloop()
