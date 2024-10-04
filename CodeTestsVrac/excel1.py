# -*- coding: utf-8 -*-
"""
Created on Fri May 10 13:27:02 2024

@author: leona
"""

import pandas as pd
import time

# Chemin vers votre fichier Excel
excel_file_path = 'test.xlsx'

# Charger le fichier Excel
df = pd.read_excel(excel_file_path)

# Obtenir le nombre total de lignes dans le DataFrame
total_rows = len(df)

# Itérer à travers les lignes et récupérer les valeurs chaque seconde
for i in range(total_rows):
    # Récupérer les valeurs de la ligne actuelle
    row_values = df.iloc[i].values

    # Afficher les valeurs de la ligne
    print(f"Valeurs de la ligne {i+1}: {row_values}")
    
    
    x1 = row_values[0]
    print(x1)
    
    

    # Attendre une seconde avant de passer à la ligne suivante
    time.sleep(1)
    
print(type(['0,0,0,2,0,0,0,3,16']))