# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:15:12 2024

@author: leona
"""

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Fonction pour mettre à jour le graphique
x_data = []
y_data = []

def update_graph():
    # Ajouter de nouvelles données au graphique
    x_new = len(x_data) + 1
    y_new = random.randint(0, 100)  # Remplacez ceci par vos propres données

    x_data.append(x_new)
    y_data.append(y_new)

    # Limiter l'historique des données affichées
    max_len = 50
    if len(x_data) > max_len:
        x_data.pop(0)
        y_data.pop(0)

    # Mettre à jour les données du graphique
    line.set_data(x_data, y_data)

    # Redessiner le graphique
    ax.relim()
    ax.autoscale_view()
    canvas.draw()

# Initialise la fenêtre principale tkinter
root = tk.Tk()
root.title("Graphique en temps réel")

# Crée une figure matplotlib vide
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_ylim(0, 100)  # Définir les limites de l'axe y

# Ajoute la figure à un canevas tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def animate():
    update_graph()
    root.after(1000, animate)  # Appel récursif après 1000 millisecondes (1 seconde)

# Lancer la première mise à jour du graphique
animate()

# Démarrer la boucle principale tkinter
root.mainloop()
