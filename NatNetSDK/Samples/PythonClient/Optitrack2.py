import NatNetLib
from NatNetLib import *

def callback_frame_of_data(skeleton):
    # Cette fonction est appelée chaque fois qu'un nouveau frame de données est reçu
    # 'skeleton' contient les données de position des capteurs

    # Parcourir tous les marqueurs capturés
    for marker in skeleton.markers:
        print(f"ID: {marker.ID}, Position: ({marker.x}, {marker.y}, {marker.z})")




def main():
    # Initialiser le client NatNet 
    client = NatNetClient() #NatNetClient(): Crée une instance du client NatNet.

    # Configurer le callback pour recevoir les données de frame
    client.newFrameListener = callback_frame_of_data

    # Connexion au serveur NatNet (Motive) sur le port par défaut (1510)
    success, response = client.connect()

    if success:
        print("Connecté à NatNet")
        # Démarrer l'écoute des frames
        client.run()
    else:
        print(f"Erreur de connexion: {response}")
        return

if __name__ == "__main__":
    main()




