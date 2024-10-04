# -*- coding: utf-8 -*-
"""
Created on Fri May 17 23:28:34 2024

@author: leona
"""

import tkinter as tk

def open_new_window():
    # Créer une nouvelle fenêtre Toplevel
    new_window = tk.Toplevel(root)
    new_window.title("Nouvelle Fenêtre")

    # Définir les dimensions de la nouvelle fenêtre
    new_window.geometry("300x200")

    # Ajouter un label dans la nouvelle fenêtre
    label = tk.Label(new_window, text="Ceci est une nouvelle fenêtre.")
    label.pack(pady=20)

    # Ajouter un bouton de fermeture
    close_button = tk.Button(new_window, text="Fermer", command=new_window.destroy)
    close_button.pack(pady=10)

# Créer la fenêtre principale
root = tk.Tk()
root.title("Fenêtre Principale")
root.geometry("400x300")

# Ajouter un bouton qui ouvre une nouvelle fenêtre
open_button = tk.Button(root, text="Ouvrir Nouvelle Fenêtre", command=open_new_window)
open_button.pack(pady=20)

# Lancer la boucle principale Tkinter
root.mainloop()
