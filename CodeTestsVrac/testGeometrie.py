# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:31:02 2024

@author: leona
"""

import tkinter as tk
from tkinter import *
import math as mt

fenetre = Tk()

fenetre.geometry('400x400')
fenetre.title('Titre Youpiiii')
fenetre['bg']='white'
fenetre.resizable(height=True,width=True)

alpha = 10

def changeAlpha():
    alpha = ALPHA.get()
    print(alpha)
    deltaX1 = mt.cos(mt.radians(alpha))*r
    deltaY1 = mt.sin(mt.radians(alpha))*r
    BGx = B1x-deltaX1
    BGy = B1y+deltaY1
    canvas.coords(brasGauche, B1x,B1y,BGx,BGy)




canvas = Canvas(fenetre, width="400",height="300",bg="grey")


#détermination de alpha
ALPHA = IntVar()
entree = Entry(fenetre, textvariable=ALPHA)
entree.pack()


boutonAlpha = Button(fenetre, text="valider",command=changeAlpha)
boutonAlpha.pack()


#création du squelette
#alpha = 20
r = 70
B1x = 120
B1y = 120
B2x = 280
B2y = 120
canvas.create_line(B1x,B1y,B2x,B2y)
canvas.create_oval(B1x-3,B1y-3,B1x+3,B1y+3, fill="blue")
canvas.create_oval(B2x-3,B2y-3,B2x+3,B2y+3, fill="red")
deltaX1 = mt.cos(mt.radians(alpha))*r
deltaY1 = mt.sin(mt.radians(alpha))*r
BGx = B1x-deltaX1
BGy = B1y+deltaY1
brasGauche = canvas.create_line(B1x,B1y,BGx,BGy)

#zones vertes
#arcG_front = canvas.create_arc()



canvas.pack()

fenetre.mainloop()