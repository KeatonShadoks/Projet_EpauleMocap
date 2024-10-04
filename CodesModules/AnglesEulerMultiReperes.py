# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 13:22:46 2024

@author: leona
"""

import tkinter as tk
from tkinter import ttk
import numpy as np
from scipy.spatial.transform import Rotation as R


#calcule du vecteur unitaire
def vecteur_unitaire(v):
    norme_v = np.linalg.norm(v)
    if norme_v != 0:
        return v / norme_v
    else:
        raise ValueError("La norme du vecteur est nulle, impossible de calculer le vecteur unitaire.")

#calculer matrice de rotation et angles d'Euler selon:(Y-X-Y)
def calcul_matrice_rotation(repere1, repere2):
    R1 = np.column_stack(repere1)
    R2 = np.column_stack(repere2)
    R_matrix = R2 @ np.linalg.inv(R1)
    r = R.from_matrix(R_matrix)
    angles_euler = r.as_euler('yxy', degrees=True)
    return R_matrix, angles_euler

#repères
repere_A = [
    np.array([1, 0, 0]),
    np.array([0, 1, 0]),
    np.array([0, 0, 1])
]

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



#calcul des vecteurs unitaires des repères
repere_A_unitaires = [vecteur_unitaire(v) for v in repere_A]
repere_B_unitaires = [vecteur_unitaire(v) for v in repere_B]
repere_C_unitaires = [vecteur_unitaire(v) for v in repere_C]

#dictionnaire pour lier les choix dans l'interface à leurs vecteurs unitaires
repere_dict = {
    "Repère A": repere_A_unitaires,
    "Repère B": repere_B_unitaires,
    "Repère C": repere_C_unitaires
}




#fonction lancée dès validation
def btnValider():
    repere_depart = choix_depart.get()
    repere_arrivee = choix_arrivee.get()
    
    if repere_depart != repere_arrivee:
        R_matrix, angles_euler = calcul_matrice_rotation(repere_dict[repere_depart], repere_dict[repere_arrivee])
        resultats_text.set(f"Matrice de rotation :\n{R_matrix}\n\nAngles d'Euler (Y-X-Y) :\n{angles_euler}")
    else:
        resultats_text.set("Veuillez sélectionner deux repères différents.")





#création de la fenêtre principale Tkinter
root = tk.Tk()
root.title("Calcul des angles d'Euler et matrice de rotation")

#label et menu déroulant pour choisir le repère de départ
ttk.Label(root, text="Choisissez le repère de départ :").grid(column=0, row=0, padx=10, pady=10)
choix_depart = ttk.Combobox(root, values=["Repère A", "Repère B", "Repère C"], state="readonly")
choix_depart.grid(column=1, row=0, padx=10, pady=10)

#label et menu déroulant pour choisir le repère d'arrivée
ttk.Label(root, text="Choisissez le repère d'arrivée :").grid(column=0, row=1, padx=10, pady=10)
choix_arrivee = ttk.Combobox(root, values=["Repère A", "Repère B", "Repère C"], state="readonly")
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
