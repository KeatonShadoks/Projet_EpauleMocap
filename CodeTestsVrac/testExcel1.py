# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:09:32 2024

@author: leona
"""

import pandas as pd


# Chemin vers votre fichier Excel
excel_file_path = 'TroisPts1_1colloneModif.xlsx'

# Charger le fichier Excel
df = pd.read_excel(excel_file_path)

# Obtenir le nombre total de lignes dans le DataFrame
total_rows = len(df)

#print(frame)
# Données initiales
# Exemple de données
x = []
y = []
    



# Supposons que df est votre DataFrame pandas

# Parcourir les lignes du DataFrame
for i in range(len(df)):
    # Accéder à la cellule à la ligne i, colonne 0
    cell_value = df.iloc[i, 0]
    
    # Vérifier si la valeur de la cellule n'est pas nulle (non-NaN)
    if pd.notnull(cell_value):
        # Diviser la chaîne de nombres à virgule en une liste
        chiffres_ligne = cell_value.split(',')
        
        # Convertir les éléments de la liste en float
        chiffres_ligne_float = [float(num) for num in chiffres_ligne]
        
        # Afficher les chiffres séparés en tant que liste de nombres flottants
        print(f"Chiffres ligne {i+1} : {chiffres_ligne_float}")
    else:
        # Si la cellule est vide, afficher une liste vide
        chiffres_ligne_float = []
        print(f"Chiffres ligne {i+1} : {chiffres_ligne_float}")
