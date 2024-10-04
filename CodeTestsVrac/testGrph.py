# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:16:41 2024

@author: leona
"""

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Exemple de données
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 6]

# Créer une fenêtre tkinter
root = tk.Tk()
root.title("Graphique de points")

# Créer le scatter plot
fig, ax = plt.subplots()
ax.scatter(x, y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Graphique de points')

# Intégrer le graphique dans tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Lancer la boucle principale tkinter
tk.mainloop()
