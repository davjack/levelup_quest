import json
from ..characters import Personnage, Stats, PERSONNAGES, Capacite
from ..combat import Combat
from ..story import Histoire
import os

class CyberQuestGame:
    def __init__(self):
        self.joueur = None
        self.histoire = None
        self.position_histoire = "debut"
        
    def nettoyer_ecran(self):
        # Pour Windows
        if os.name == 'nt':
            os.system('cls')
        # Pour Linux/Mac
        else:
            os.system('clear')
    
    def nouveau_jeu(self):
        self.afficher_intro()
        self.selection_personnage()
        self.histoire = Histoire(self.joueur)
    
    def afficher_intro(self):
        self.nettoyer_ecran()
        print("""
        ██████╗██╗   ██╗██████╗ ███████╗██████╗  ██████╗ ██╗   ██╗███████╗███████╗████████╗
        ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝
        ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝██║   ██║██║   ██║█████╗  ███████╗   ██║   
        ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   
        ╚██████╗   ██║   ██████╔╝███████╗██║  ██║╚██████╔╝╚██████╔╝███████╗███████║   ██║   
         ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   
        ════════════════════════════════════════════════════════════════════════════════════
                                    2  1  4  2
        ════════════════════════════════════════════════════════════════════════════════════
                            La Guilde du LevelUp présente
        ════════════════════════════════════════════════════════════════════════════════════

        Dans un monde où la technologie règne en maître, où les mégacorporations 
        contrôlent l'information et où les IAs sont devenues conscientes...

        Vous êtes un membre de la mystérieuse Guilde du LevelUp, une organisation 
        secrète qui lutte pour maintenir l'équilibre dans ce monde cyberpunk.

        Votre mission : Infiltrer NeuroCorp et découvrir la vérité sur le projet Némésis,
        une IA qui menace de bouleverser l'ordre établi.

        ════════════════════════════════════════════════════════════════════════════════════
        Appuyez sur Entrée pour commencer votre aventure...
        """)
        input()
    
    def selection_personnage(self):
        while True:
            self.nettoyer_ecran()
            print("\nChoisissez votre personnage :")
            for i, (nom, data) in enumerate(PERSONNAGES.items(), 1):
                print(f"{i}. {nom} - {data['specialisation']}")
            print("Q. Quitter le jeu")
            
            choix = input("\nVotre choix (1-4 ou Q) : ").upper()
            if choix == 'Q':
                if self.confirmer_quitter():
                    exit()
                continue
            
            try:
                choix = int(choix)
                if choix < 1 or choix > len(PERSONNAGES):
                    print("\nChoix invalide. Veuillez choisir un numéro valide.")
                    input("\nAppuyez sur Entrée pour continuer...")
                    continue
                
                self.nettoyer_ecran()
                nom_perso = list(PERSONNAGES.keys())[choix-1]
                data = PERSONNAGES[nom_perso]
                
                print(f"\n=== {nom_perso} ===")
                print(f"Spécialisation : {data['specialisation']}")
                print(f"Background : {data['background']}")
                print("\nStatistiques :")
                for stat, valeur in data['stats'].items():
                    print(f"- {stat.capitalize()}: {valeur}")
                print("\nCapacités :")
                for capacite in data['capacites']:
                    print(f"- {capacite['nom']}: {capacite['description']}")
                
                confirmation = input("\nConfirmer ce choix ? (o/n) : ").lower()
                if confirmation == 'o':
                    stats = Stats(**data['stats'])
                    self.joueur = Personnage(nom_perso, data['background'], 
                                           data['specialisation'], stats)
                    
                    for cap in data['capacites']:
                        self.joueur.ajouter_capacite(Capacite(**cap))
                    
                    self.nettoyer_ecran()
                    print(f"\nVous avez choisi {nom_perso} !")
                    break
                
            except ValueError:
                print("\nVeuillez entrer un numéro valide.")
                input("\nAppuyez sur Entrée pour continuer...")

    def afficher_stats_personnage(self):
        print(f"\nStats de {self.joueur.nom}:")
        for attr, value in self.joueur.stats.__dict__.items():
            print(f"{attr.capitalize()}: {value}")

    def jouer_tour(self):
        chapitre = self.histoire.obtenir_chapitre_actuel()
        self.nettoyer_ecran()
        
        print(f"\n=== {chapitre['titre']} ===")
        print(chapitre['texte'])
        print("\nOptions disponibles :")
        
        for num, choix in chapitre['choix'].items():
            print(f"{num}. {choix['texte']}")
        print("Q. Quitter le jeu")
        
        while True:
            choix = input("\nVotre choix : ").upper()
            if choix == 'Q':
                if self.confirmer_quitter():
                    return False  # Indique qu'il faut quitter le jeu
                break
            elif choix in chapitre['choix']:
                if self.histoire.faire_choix(choix):
                    return True  # Continue le jeu
            print("Choix invalide. Veuillez réessayer.")

    def confirmer_quitter(self):
        while True:
            confirmation = input("\nÊtes-vous sûr de vouloir quitter le jeu ? (o/n) : ").lower()
            if confirmation == 'o':
                self.nettoyer_ecran()
                print("\nMerci d'avoir joué à CyberQuest 2142 !")
                return True
            elif confirmation == 'n':
                return False
            print("Veuillez répondre par 'o' ou 'n'")

    def boucle_principale(self):
        while True:
            if not self.jouer_tour():  # Si jouer_tour renvoie False, on quitte
                self.nettoyer_ecran()
                print("\nMerci d'avoir joué à CyberQuest 2142 !")
                break
            if self.histoire.est_fin_histoire():
                if not self.gerer_fin_partie():  # Si gerer_fin_partie renvoie False, on quitte
                    break

    def gerer_fin_partie(self):
        self.nettoyer_ecran()
        print("\nFin de l'histoire !")
        print("\nQue souhaitez-vous faire ?")
        print("1. Recommencer une nouvelle partie")
        print("2. Quitter le jeu")
        
        while True:
            choix = input("\nVotre choix (1-2) : ")
            if choix == "1":
                self.nettoyer_ecran()
                self.nouveau_jeu()
                return True
            elif choix == "2":
                self.nettoyer_ecran()
                print("\nMerci d'avoir joué à CyberQuest 2142 !")
                return False
            print("Choix invalide. Veuillez choisir 1 ou 2.")