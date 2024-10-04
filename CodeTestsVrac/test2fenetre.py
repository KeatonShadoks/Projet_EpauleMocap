# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 22:13:32 2024

@author: leona
"""

import tkinter as tk
from PIL import Image, ImageTk

# Fonction pour redimensionner l'image
def resize_image(image_path, width, height):
    image = Image.open(image_path)
    return image.resize((width, height), Image.ANTIALIAS)

# Fonction pour ouvrir une nouvelle fenêtre avec l'image
def open_new_window():
    # Créer une nouvelle fenêtre Toplevel
    new_window = tk.Toplevel(root)
    new_window.title("Fenêtre Patient")

    # Définir les dimensions de la nouvelle fenêtre
    new_window.geometry("700x600")
    
    # Spécifier la taille du canevas
    canvas_width = 300
    canvas_height = 200

    # Redimensionner l'image de fond
    image_path = "AnimationAvatar/shema5.png"  # Chemin vers votre image de fond
    resized_image = resize_image(image_path, canvas_width, canvas_height)

    # Convertir l'image redimensionnée en PhotoImage
    photo = ImageTk.PhotoImage(resized_image)

    # Créer un canevas avec la taille spécifiée
    avatar = tk.Canvas(new_window, width=canvas_width, height=canvas_height)
    avatar.pack()

    # Afficher l'image redimensionnée sur le canevas
    avatar.create_image(0, 0, image=photo, anchor=tk.NW)

    # Stocker la référence de l'image dans un attribut de la fenêtre pour éviter le garbage collection
    new_window.image = photo

# Création de la fenêtre principale
root = tk.Tk()
root.title("Fenêtre Principale")

# Ajouter un bouton pour ouvrir la nouvelle fenêtre
open_button = tk.Button(root, text="Ouvrir Fenêtre Patient", command=open_new_window)
open_button.pack()

# Lancer la boucle principale de tkinter
root.mainloop()
