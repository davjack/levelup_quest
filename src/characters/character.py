from dataclasses import dataclass
from typing import Dict, List
from .stats import Stats

@dataclass
class Capacite:
    nom: str
    description: str
    cout_energie: int
    effet: dict

class Personnage:
    def __init__(self, nom: str, background: str, specialisation: str, stats: Stats):
        self.nom = nom
        self.background = background
        self.specialisation = specialisation
        self.stats = stats
        self.inventaire: List[str] = []
        self.capacites: Dict[str, Capacite] = {}
        self.experience = 0
        self.niveau = 1
    
    def ajouter_capacite(self, capacite: Capacite):
        self.capacites[capacite.nom] = capacite
    
    def sauvegarder(self) -> dict:
        return {
            "nom": self.nom,
            "background": self.background,
            "specialisation": self.specialisation,
            "stats": self.stats.__dict__,
            "inventaire": self.inventaire,
            "experience": self.experience,
            "niveau": self.niveau
        } 