# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:04:12 2024

@author: leona
"""

import tkinter as tk
from PIL import Image, ImageTk

def resize_image(image_path, width, height):
    # Charger l'image depuis le chemin spécifié
    original_image = Image.open(image_path)

    # Redimensionner l'image à la taille spécifiée avec interpolation BILINEAR
    resized_image = original_image.resize((width, height), Image.BILINEAR)

    return resized_image

def main():
    # Créer une fenêtre Tkinter
    root = tk.Tk()
    root.title("Image de fond redimensionnée")

    # Spécifier la taille du canevas
    canvas_width = 800
    canvas_height = 600

    # Redimensionner l'image de fond
    image_path = "AnimationAvatar/shema2.png"  # Chemin vers votre image de fond
    resized_image = resize_image(image_path, canvas_width, canvas_height)

    # Convertir l'image redimensionnée en PhotoImage
    photo = ImageTk.PhotoImage(resized_image)

    # Créer un canevas avec la taille spécifiée
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    # Afficher l'image redimensionnée sur le canevas
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)

    # Lancer la boucle principale Tkinter
    root.mainloop()

if __name__ == "__main__":
    main()
