# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:47:29 2024

@author: leona
"""

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import random
import time



# Création de la fenêtre principale Tkinter
fenetre = tk.Tk()
fenetre.title("Graphique avec ajout de valeur chaque seconde")


# Initialisation du graphique dans Tkinter
fig = Figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)
line, = ax.plot([], [], 'b-')
ax.set_xlabel('Temps (s)')
ax.set_ylabel('Valeur')
ax.set_title('Évolution de la valeur au fil du temps')
ax.grid(True)

graph = FigureCanvasTkAgg(fig, master=fenetre)
graph_widget = graph.get_tk_widget()
graph_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

def update(frame):
    new_value = random.randint(0, 100)  # Générer une nouvelle valeur aléatoire
    xdata.append(frame)
    ydata.append(new_value)
    line.set_data(xdata, ydata)
    ax.relim()
    ax.autoscale_view()
    return line,

# Données initiales
xdata, ydata = [], []

# Création de l'animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=1000, blit=True)

# Lancement de la boucle principale Tkinter
fenetre.mainloop()

