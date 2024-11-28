import random
from ..characters import Personnage

class Combat:
    def __init__(self, joueur: Personnage, ennemi: dict):
        self.joueur = joueur
        self.ennemi = ennemi
        self.ennemi_pv = ennemi['pv']
    
    def tour_joueur(self) -> bool:
        print("\nVos actions disponibles :")
        print("1. Attaque normale")
        print("2. Utiliser une capacité")
        print("3. Tenter de fuir")
        
        choix = input("\nVotre choix : ")
        
        if choix == "1":
            degats = self.joueur.stats.force * 2 + random.randint(1, 6)
            self.ennemi_pv -= degats
            print(f"\nVous infligez {degats} points de dégâts à {self.ennemi['nom']}")
        elif choix == "2":
            if not self.joueur.capacites:
                print("Vous n'avez pas de capacités disponibles !")
                return self.tour_joueur()
            self.utiliser_capacite()
        elif choix == "3":
            if random.random() < 0.3:  # 30% de chance de fuir
                print("Vous avez réussi à fuir !")
                return True
            print("Impossible de fuir !")
        
        return False

    def tour_ennemi(self):
        degats = self.ennemi['force'] + random.randint(1, 4)
        self.joueur.stats.pv -= degats
        print(f"\n{self.ennemi['nom']} vous inflige {degats} points de dégâts")

    def afficher_etat(self):
        print(f"\nVos PV : {self.joueur.stats.pv}")
        print(f"PV de l'ennemi : {self.ennemi_pv}") 