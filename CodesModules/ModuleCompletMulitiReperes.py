# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 23:29:04 2024

@author: leona
"""

import tkinter as tk
from tkinter import ttk
import numpy as np
from scipy.spatial.transform import Rotation as R


#calcule vecteur unitaire
def vecteur_unitaire(v):
    norme_v = np.linalg.norm(v)
    if norme_v != 0:
        return v / norme_v
    else:
        raise ValueError("La norme du vecteur est nulle, impossible de calculer le vecteur unitaire.")


#calcule matrice de rotation et angles d'Euler selon:(Y-X-Y)
def calcul_matrice_rotation(repere1, repere2):
    R1 = np.column_stack(repere1)
    R2 = np.column_stack(repere2)
    R_matrix = R2 @ np.linalg.inv(R1)
    r = R.from_matrix(R_matrix)
    angles_euler = r.as_euler('yxy', degrees=True)
    return R_matrix, angles_euler





#Calcul repères

def point_milieu(A, B):
    # Calculer la moyenne des coordonnées x, y, z des deux points
    M_x = (A[0] + B[0]) / 2
    M_y = (A[1] + B[1]) / 2
    M_z = (A[2] + B[2]) / 2
    
    return [M_x, M_y, M_z]


def calcul_vect_repeteTHORAX(IJ, C7, PX, T8):
    # Convertir les points en numpy arrays pour calculer facilement les vecteurs
    IJ = np.array(IJ)
    C7 = np.array(C7)
    PX = np.array(PX)
    T8 = np.array(T8)
    
    # Calcul des vecteurs
    M1 = point_milieu(IJ, C7)
    M2 = point_milieu(PX, T8)
    M1 = np.array(M1)
    M2 = np.array(M2)
    
    yt = M1-M2

    u = C7-IJ
    v = M2-IJ

    zt = np.cross(u, v)
    xt = np.cross(yt, zt) 
    
    return xt, yt, zt


def calcul_vect_repeteCLAVICULE(SC, AC , IJ, C7, PX, T8):
    # Convertir les points en numpy arrays pour calculer facilement les vecteurs
    SC = np.array(SC)
    AC = np.array(AC)
    IJ = np.array(IJ)
    C7 = np.array(C7)
    PX = np.array(PX)
    T8 = np.array(T8)

    zc = AC-SC
    
    #yt-----------------------------------
    M1 = point_milieu(IJ, C7)
    M2 = point_milieu(PX, T8)
    M1 = np.array(M1)
    M2 = np.array(M2)
    
    yt = M1-M2
    #-------------------------------------
    
    xc = np.cross(yt, zc)
    yc = np.cross(zc, xc)

    return xc, yc, zc


def calcul_vect_repeteSCAPULA(AA, TS, AI):
    # Convertir les points en numpy arrays pour calculer facilement les vecteurs
    AA = np.array(AA)
    TS = np.array(TS)
    AI = np.array(AI)
    
    
    zs = AA-TS
    
    u = AI-AA
    v = TS-AA

    xs = np.cross(u, v)
    ys = np.cross(zs, xs)
    
    return xs, ys, zs


def calcul_vect_repeteHUMERUS(GH, EL, EM):
    # Convertir les points en numpy arrays pour calculer facilement les vecteurs
    GH = np.array(GH)
    EL = np.array(EL)
    EM = np.array(EM)
    
    # Calcul des vecteurs
    M1 = point_milieu(EL, EM)
    M1 = np.array(M1)
    
    yh = GH-M1

    u = EL-GH
    v = EM-GH

    xh = np.cross(u, v)
    zh = np.cross(xh, yh)
    
    return xh, yh, zh


def calcul_vect_repeteAVANTBRAS(US, RS, EL, EM):
    # Convertir les points en numpy arrays pour calculer facilement les vecteurs
    US = np.array(US)
    RS = np.array(RS)
    EL = np.array(EL)
    EM = np.array(EM)
    
    
    M1 = point_milieu(EL, EM)
    M1 = np.array(M1)
    
    yf = M1-US
    
    u = M1-US
    v = RS-US
    
    xf = np.cross(u, v)
    zf = np.cross(xf, yf)
    
    return xf, yf, zf

#-------------------------------------------------------------------

#Récupération des points par la MOCAP

#thorax
IJ = [5, 10, 0]
C7 = [5, 10, -5]
PX = [5, 5, 0]
T8 = [5, 5, -5]

#clavicule
SC = [4, 10, 0]
AC = [0, 10, 0]

#scapula
AA = [0, 10, -3]
TS = [2, 10, -3]
AI = [2, 8, -3]

#humerus
GH = [0, 10, -2]
EL = [-3, 5, -2]
EM = [0, 5, -2]

#avant-bras
US = [0, 2, -2]
RS = [-3, 2, -2]


xt, yt, zt = calcul_vect_repeteTHORAX(IJ, C7, PX, T8)
xc, yc, zc = calcul_vect_repeteCLAVICULE(SC, AC , IJ, C7, PX, T8)
xs, ys, zs = calcul_vect_repeteSCAPULA(AA, TS, AI)
xh, yh, zh = calcul_vect_repeteHUMERUS(GH, EL, EM)
xf, yf, zf = calcul_vect_repeteAVANTBRAS(US, RS, EL, EM)



#repères
repere_T = [xt,yt,zt]

repere_C = [xc,yc,zc]

repere_S = [xs,ys,zs]

repere_H = [xh,yh,zh]

repere_AvB = [xf,yf,zf]

'''
repere_B = [
    np.array([3, 1, 2]),
    np.array([1, 3, 0]),
    np.array([0, 0, 4])
]

repere_C = [
    np.array([1, 2, 1]),
    np.array([2, 0, 3]),
    np.array([0, 3, 1])
]
'''


#calcul des vecteurs unitaires des repères
repere_T_unitaires = [vecteur_unitaire(v) for v in repere_T]
repere_C_unitaires = [vecteur_unitaire(v) for v in repere_C]
repere_S_unitaires = [vecteur_unitaire(v) for v in repere_S]
repere_H_unitaires = [vecteur_unitaire(v) for v in repere_H]
repere_AvB_unitaires = [vecteur_unitaire(v) for v in repere_AvB]

#dictionnaire pour lier les choix dans l'interface à leurs vecteurs unitaires
repere_dict = {
    "Repère Thorax": repere_T_unitaires,
    "Repère Clavicule": repere_C_unitaires,
    "Repère Scapula": repere_S_unitaires,
    "Repère Humerus": repere_H_unitaires,
    "Repère Forearm": repere_AvB_unitaires,
}



#fonction lancée dès validation
def btnValider():
    repere_depart = choix_depart.get()
    repere_Trrivee = choix_arrivee.get()
    
    if repere_depart != repere_Trrivee:
        R_matrix, angles_euler = calcul_matrice_rotation(repere_dict[repere_depart], repere_dict[repere_Trrivee])
        resultats_text.set(f"Matrice de rotation :\n{R_matrix}\n\nAngles d'Euler (Y-X-Y) :\n{angles_euler}")
    else:
        resultats_text.set("Veuillez sélectionner deux repères différents.")






#création de la fenêtre principale Tkinter
root = tk.Tk()
root.title("Calcul des angles d'Euler et matrice de rotation")

#label et menu déroulant pour choisir le repère de départ
ttk.Label(root, text="Choisissez le repère de départ :").grid(column=0, row=0, padx=10, pady=10)
choix_depart = ttk.Combobox(root, values=["Repère Thorax", "Repère Clavicule", "Repère Scapula", "Repère Humerus", "Repère Forearm"], state="readonly")
choix_depart.grid(column=1, row=0, padx=10, pady=10)

#label et menu déroulant pour choisir le repère d'arrivée
ttk.Label(root, text="Choisissez le repère d'arrivée :").grid(column=0, row=1, padx=10, pady=10)
choix_arrivee = ttk.Combobox(root, values=["Repère Thorax", "Repère Clavicule", "Repère Scapula", "Repère Humerus", "Repère Forearm"], state="readonly")
choix_arrivee.grid(column=1, row=1, padx=10, pady=10)

#bouton pour valider
valider_btn = ttk.Button(root, text="Valider", command=btnValider)
valider_btn.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

#zone de texte pour afficher les résultats
resultats_text = tk.StringVar()
resultats_label = ttk.Label(root, textvariable=resultats_text, justify="left")
resultats_label.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

#exécuter l'interface Tkinter
root.mainloop()
