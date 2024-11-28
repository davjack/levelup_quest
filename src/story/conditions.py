class ConditionChecker:
    def __init__(self, joueur):
        self.joueur = joueur

    def verifier_condition(self, condition):
        if condition is None:
            return True
            
        if "specialisation" in condition:
            return self.joueur.specialisation == condition["specialisation"]
            
        if "intelligence" in condition:
            return self.joueur.stats.intelligence >= condition["intelligence"]
            
        if "force" in condition:
            return self.joueur.stats.force >= condition["force"]
            
        if "agilite" in condition:
            return self.joueur.stats.agilite >= condition["agilite"]
            
        return False

    def obtenir_choix_disponibles(self, chapitre):
        choix_disponibles = {}
        for key, choix in chapitre["choix"].items():
            if self.verifier_condition(choix["condition"]):
                choix_disponibles[key] = choix
        return choix_disponibles 