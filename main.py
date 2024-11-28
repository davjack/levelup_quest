from src.core import CyberQuestGame

if __name__ == "__main__":
    try:
        jeu = CyberQuestGame()
        jeu.nouveau_jeu()
        jeu.boucle_principale()
    except KeyboardInterrupt:
        print("\nAu revoir !")
