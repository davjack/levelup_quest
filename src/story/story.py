from .chapters import CHAPITRES_DEBUT
from .conditions import ConditionChecker

class Histoire:
    def __init__(self, joueur):
        self.joueur = joueur
        self.condition_checker = ConditionChecker(joueur)
        self.chapitre_actuel = "reveil"
        self.chapitres_visites = set()
        self.variables = {}  # Pour stocker l'état du jeu

    def obtenir_chapitre_actuel(self):
        try:
            chapitre = CHAPITRES_DEBUT[self.chapitre_actuel]
            choix_disponibles = self.condition_checker.obtenir_choix_disponibles(chapitre)
            
            return {
                "titre": chapitre["titre"],
                "texte": chapitre["texte"],
                "choix": choix_disponibles
            }
        except KeyError:
            print(f"\nErreur : Chapitre '{self.chapitre_actuel}' non trouvé.")
            return {
                "titre": "Erreur",
                "texte": "Une erreur est survenue dans l'histoire.",
                "choix": {"1": {"texte": "Retourner au début", "destination": "reveil", "condition": None}}
            }

    def faire_choix(self, choix):
        try:
            chapitre = CHAPITRES_DEBUT[self.chapitre_actuel]
            choix_disponibles = self.condition_checker.obtenir_choix_disponibles(chapitre)
            
            if choix not in choix_disponibles:
                return False
                
            nouvelle_destination = choix_disponibles[choix]["destination"]
            self.chapitres_visites.add(self.chapitre_actuel)
            self.chapitre_actuel = nouvelle_destination
            
            return True
        except KeyError:
            self.chapitre_actuel = "reveil"
            return False

    def est_fin_histoire(self):
        """Vérifie si le chapitre actuel est une fin"""
        chapitre = CHAPITRES_DEBUT[self.chapitre_actuel]
        return "=== FIN" in chapitre["texte"] or "=== VICTOIRE" in chapitre["texte"]