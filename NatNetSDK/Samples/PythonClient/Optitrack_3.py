# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:00:02 2024

@author: leona
"""

import pynatnet
import time

def on_frame(frame):
    for rigid_body in frame.rigid_bodies:
        print(f"Rigid Body ID: {rigid_body.id}")
        print(f"Position: ({rigid_body.position[0]:.2f}, {rigid_body.position[1]:.2f}, {rigid_body.position[2]:.2f})")
        print(f"Orientation: ({rigid_body.orientation[0]:.2f}, {rigid_body.orientation[1]:.2f}, {rigid_body.orientation[2]:.2f}, {rigid_body.orientation[3]:.2f})")

def main():
    # Adresse IP de l'hôte Motive (la machine exécutant Motive)
    server_address = '127.0.0.1'

    # Créer un client NatNet
    client = pynatnet.NatNetClient(server_address)

    # Définir le callback pour traiter les données de frame
    client.new_frame_listener = on_frame

    # Démarrer le client NatNet
    client.run()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        client.shutdown()

if __name__ == "__main__":
    main()
