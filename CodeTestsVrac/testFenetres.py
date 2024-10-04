# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:25:30 2024

@author: leona
"""

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

#création de la fenêtre en définissant ses paramètres
fenetre = Tk()
fenetre.geometry('1000x600')
fenetre.title('Fenêtre Test')
fenetre['bg']='white'
fenetre.resizable(height=True,width=True)

#création d'un canvas bleu placé à gauche
canvasBleu = Canvas(fenetre, width="600",height="500",bg="blue")
canvasBleu.pack(side=tk.LEFT, padx=0, pady=0)

#création d'un canvas gris placé à gauche placé par rapport au premier canvas
canvasGris = Canvas(canvasBleu, width="600",height="300",bg="grey")
canvasGris.place(x='0',y='0') #placement par rapport au canva maitre

#création d'un canvas rouge placé à gauche placé par rapport au premier canvas
canvasRouge = Canvas(canvasBleu, width="400",height="300",bg="red")
canvasRouge.place(x='100',y='400')

#lancement de la boucle
fenetre.mainloop()




