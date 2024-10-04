# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:04:52 2024

@author: leona
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 10 14:41:17 2024

@author: leona
"""

import math as mt
import matplotlib.pyplot as plt
import pandas as pd
import time
import tkinter as tk
from tkinter import *



    
fenetre = Tk()
fenetre.geometry('400x400')
fenetre.title('Titre Youpiiii')
fenetre['bg']='white'
fenetre.resizable(height=True,width=True)

canvas = Canvas(fenetre, width="400",height="300",bg="grey")



#variables globales
r_globale = 70
alpha = 20
B1x_globale = 120
B1y_globale = 120
B2x_globale = 280
B2y_globale = 120
deltaX1 = mt.cos(mt.radians(alpha))*r_globale
deltaY1 = mt.sin(mt.radians(alpha))*r_globale
BGx = B1x_globale-deltaX1
BGy = B1y_globale+deltaY1
brasGauche_globale = canvas.create_line(B1x_globale,B1y_globale,BGx,BGy)
i = 0

'''
def changeAlpha():
    alpha = ALPHA.get()
    print(alpha)
    deltaX1 = mt.cos(mt.radians(alpha))*r
    deltaY1 = mt.sin(mt.radians(alpha))*r
    BGx = B1x-deltaX1
    BGy = B1y+deltaY1
    canvas.coords(brasGauche, B1x,B1y,BGx,BGy)
'''


#calcul de l'angle grâce au produit scalaire
def angle_between_points(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    ux, uy, uz = x2 - x1, y2 - y1, z2 - z1
    vx, vy, vz = x3 - x1, y3 - y1, z3 - z1

    dot_product = ux * vx + uy * vy + uz * vz
    norm_u = mt.sqrt(ux**2 + uy**2 + uz**2)
    norm_v = mt.sqrt(vx**2 + vy**2 + vz**2)

    cos_theta = dot_product / (norm_u * norm_v)
    angle_radians = mt.acos(cos_theta)
    angle_degrees = mt.degrees(angle_radians)
    
    return angle_degrees



def get_values():
    # Chemin vers votre fichier Excel
    excel_file_path = 'test.xlsx'

    # Charger le fichier Excel
    df = pd.read_excel(excel_file_path)

    # Obtenir le nombre total de lignes dans le DataFrame
    total_rows = len(df)
    
    
    
    # Itérer à travers les lignes et récupérer les valeurs chaque seconde
    for i in range(total_rows):
        # Récupérer les valeurs de la ligne actuelle
        #row_values = df.iloc[i].values
        # Récupérer les chiffres de la deuxième ligne
        chiffres_ligne = df.iloc[i, 0].split(',') if pd.notnull(df.iloc[1, 0]) else []
        # Convertir les chiffres en entiers
        chiffres_ligne = [int(chiffre) for chiffre in chiffres_ligne]
    
    
        # Afficher les valeurs de la ligne
        #print(f"Valeurs de la ligne {i+1}: {chiffres_ligne}")
        
    
        #définition des coordonnées des trois points
        x1 = chiffres_ligne[0]
        y1 = chiffres_ligne[1]
        z1 = chiffres_ligne[2]
        
        x2 = chiffres_ligne[3]
        y2 = chiffres_ligne[4]
        z2 = chiffres_ligne[5]
        
        x3 = chiffres_ligne[6]
        y3 = chiffres_ligne[7]
        z3 = chiffres_ligne[8]
        
    
        #print(z3)
        alpha = angle_between_points(x1, y1, z1, x2, y2, z2, x3, y3, z3)
        print(alpha)
        
        
        #afficher alpha
        deltaX1 = mt.cos(mt.radians(alpha))*r_globale
        deltaY1 = mt.sin(mt.radians(alpha))*r_globale
        BGx = B1x_globale-deltaX1
        BGy = B1y_globale+deltaY1
        #brasGauche = canvas.create_line(B1x_globale,B1y_globale,BGx,BGy)
        canvas.coords(brasGauche_globale,B1x_globale,B1y_globale,BGx,BGy)
        '''
        #affichage des points en 3d
        ax = plt.axes(projection="3d")
        ax.scatter(x1,y1,z1)
        ax.scatter(x2,y2,z2)
        ax.scatter(x3,y3,z3)
        plt.show
        '''
        # Attendre une seconde avant de passer à la ligne suivante
        #time.sleep(1)
        






def main():
    
    
    
    #détermination de alpha
    ALPHA = IntVar()
    entree = Entry(fenetre, textvariable=ALPHA)
    entree.pack()
    
    
    boutonAlpha = Button(fenetre, text="Get Values",command=get_values)
    boutonAlpha.pack()
    
    
    #création du squelette

    
    canvas.create_line(B1x_globale,B1y_globale,B2x_globale,B2y_globale)
    canvas.create_oval(B1x_globale-3,B1y_globale-3,B1x_globale+3,B1y_globale+3, fill="blue")
    canvas.create_oval(B2x_globale-3,B2y_globale-3,B2x_globale+3,B2y_globale+3, fill="red")
    
    
    canvas.pack()
    fenetre.mainloop()
    
    time.sleep(0.2)






if __name__ == "__main__":
    main()








