# -*- coding: utf-8 -*-
"""
Created on Fri May 10 19:29:38 2024

@author: leona
"""

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import random
import time


r_globale = 70
alpha = 20
B1x_globale = 120
B1y_globale = 120
B2x_globale = 280
B2y_globale = 120



# Fonction pour dessiner un rectangle sur un canvas donné
def draw_rectangle(canvas, color, x1, y1, x2, y2):
    canvas.create_rectangle(x1, y1, x2, y2, fill=color)

# Création de la fenêtre principale Tkinter
fenetre = tk.Tk()
fenetre.title("Exemple de plusieurs Canvas")

# Création du premier Canvas
canvas1 = tk.Canvas(fenetre, width=400, height=300, bg='white')
# Placement du Canvas à gauche avec un padding
canvas1.pack(side=tk.LEFT, padx=20, pady=20)
#création du squelette
canvas1.create_line(B1x_globale,B1y_globale,B2x_globale,B2y_globale)
canvas1.create_oval(B1x_globale-3,B1y_globale-3,B1x_globale+3,B1y_globale+3, fill="blue")
canvas1.create_oval(B2x_globale-3,B2y_globale-3,B2x_globale+3,B2y_globale+3, fill="red")





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









# Lancement de la boucle principale Tkinter
fenetre.mainloop()
