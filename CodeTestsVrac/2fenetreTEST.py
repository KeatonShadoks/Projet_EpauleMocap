# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:16:20 2024

@author: leona
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 23:03:50 2024

@author: leona
"""

import tkinter as tk
from PIL import Image, ImageTk

# Fonction pour mettre à jour les coordonnées du point dans les deux fenêtres
def update_coordinates(*args):
    x = int(coord_x.get())
    y = int(coord_y.get())
    
    # Mettre à jour le texte et le point dans la fenêtre principale
    label_coords.config(text=f"Coordonnées : ({x}, {y})")
    main_canvas.coords(point_id_main, x - 5, y - 5, x + 5, y + 5)

    # Mettre à jour la nouvelle fenêtre si elle existe
    if new_window and new_window.winfo_exists():
        new_window.label_coords.config(text=f"Coordonnées : ({x}, {y})")
        new_window.canvas.coords(new_window.point_id, x - 5, y - 5, x + 5, y + 5)

# Fonction pour ouvrir une nouvelle fenêtre
def open_new_window():
    global new_window
    if new_window and new_window.winfo_exists():
        new_window.deiconify()  # Réafficher la fenêtre si elle est déjà ouverte et minimisée
        return
    
    new_window = tk.Toplevel(root)
    new_window.title("Fenêtre Patient")
    new_window.geometry("700x600")
    
    # Charger l'image
    image_path = "AnimationAvatar/shema5.png"
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    # Créer un canevas dans la nouvelle fenêtre
    new_window.canvas = tk.Canvas(new_window, width=image.width, height=image.height)
    new_window.canvas.pack()
    new_window.canvas.create_image(0, 0, image=photo, anchor=tk.NW)
    
    # Ajouter le point dans la nouvelle fenêtre
    x, y = int(coord_x.get()), int(coord_y.get())
    new_window.point_id = new_window.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red")
    
    # Stocker la référence de l'image pour éviter le garbage collection
    new_window.image = photo

    # Ajouter un label pour afficher les coordonnées dans la nouvelle fenêtre
    new_window.label_coords = tk.Label(new_window, text=f"Coordonnées : ({x}, {y})")
    new_window.label_coords.pack()



# Création de la fenêtre principale
root = tk.Tk()
root.title("Fenêtre Principale")

# Variables pour les coordonnées
coord_x = tk.IntVar(value = 100)
coord_y = tk.IntVar(value = 100)


print(coord_x)

# Ajouter des entrées pour modifier les coordonnées
#entry_x = tk.Entry(root, textvariable=coord_x)
#entry_y = tk.Entry(root, textvariable=coord_y)
#entry_x.pack()
#entry_y.pack()

# Ajouter un label pour afficher les coordonnées actuelles
label_coords = tk.Label(root, text=f"Coordonnées : ({coord_x}, {coord_y})")
label_coords.pack()

# Ajouter un bouton pour ouvrir la nouvelle fenêtre
open_button = tk.Button(root, text="Ouvrir Fenêtre Patient", command=open_new_window)
open_button.pack()

# Créer un canevas dans la fenêtre principale
main_canvas = tk.Canvas(root, width=300, height=200)
main_canvas.pack()

# Ajouter un point dans le canevas principal
point_id_main = main_canvas.create_oval(coord_x - 5, coord_y - 5,
                                        coord_x + 5, coord_y + 5,
                                        fill="red")

# Associer les callbacks aux variables pour mettre à jour les coordonnées
coord_x.trace("w", update_coordinates)
coord_y.trace("w", update_coordinates)



# Variable pour la nouvelle fenêtre
new_window = None

# Lancer la boucle principale de tkinter
root.mainloop()
