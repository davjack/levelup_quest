PERSONNAGES = {
    "Anthony": {
        "background": """
        Ancien prodige de la Silicon Valley, Anthony était l'architecte principal de l'IA 
        'Genesis' qui a révolutionné la cybersécurité mondiale. Mais quand il découvrit 
        que son employeur utilisait son code pour développer des armes autonomes, il sabota 
        le projet et disparut dans les bas-fonds de Neo-Tokyo.

        Aujourd'hui, à 34 ans, il vit comme un hacker éthique, utilisant ses talents pour 
        protéger les plus vulnérables. Son visage, marqué par une cicatrice cybernétique 
        qui longe sa tempe gauche, rappelle l'implant neural personnalisé qu'il a développé 
        pour communiquer directement avec les IAs.

        Hanté par la culpabilité d'avoir involontairement contribué à la militarisation 
        des IAs, il cherche la rédemption en aidant la Guilde à maintenir l'équilibre 
        dans un monde où humains et intelligences artificielles coexistent.
        """,
        "specialisation": "IA & Hacking",
        "stats": {
            "force": 3,
            "agilite": 5,
            "intelligence": 9,
            "pv": 80,
            "energie": 100
        },
        "capacites": [
            {
                "nom": "Piratage d'IA",
                "description": "Permet de prendre le contrôle temporaire d'une IA en exploitant une faille qu'Anthony a lui-même créée dans le code originel de Genesis.",
                "cout_energie": 30,
                "effet": {"duree": 3, "puissance": 5}
            }
        ]
    },
    "Soazig": {
        "background": """
        Née dans une famille de chercheurs bretons en biotechnologie, Soazig a grandi 
        entre les laboratoires de Rennes et les légendes celtiques que lui racontait 
        sa grand-mère. À 15 ans, une maladie génétique rare la condamna à une mort 
        certaine. Ses parents utilisèrent leurs recherches en bio-augmentation pour 
        la sauver, faisant d'elle l'une des premières "bio-hybrides" d'Europe.

        Aujourd'hui, à 28 ans, son corps est un chef-d'œuvre de biotechnologie organique. 
        Ses augmentations, contrairement aux implants cybernétiques classiques, sont 
        cultivées à partir de son propre ADN modifié. Ses yeux verts luminescents et 
        les motifs organiques phosphorescents qui parcourent sa peau témoignent de 
        sa nature unique.

        Installée à Neo-Tokyo après la disparition mystérieuse de ses parents, elle 
        poursuit leurs recherches tout en aidant d'autres personnes à s'adapter à 
        leurs augmentations bio-organiques. Son laboratoire secret est un sanctuaire 
        où technologie et nature fusionnent en parfaite harmonie.
        """,
        "specialisation": "Biotech & Augmentations",
        "stats": {
            "force": 4,
            "agilite": 7,
            "intelligence": 8,
            "pv": 90,
            "energie": 90
        },
        "capacites": [
            {
                "nom": "Auto-réparation",
                "description": "Active les nano-organismes symbiotiques dans son corps pour réparer rapidement les tissus endommagés et les implants bio-organiques.",
                "cout_energie": 20,
                "effet": {"pv": 20}
            }
        ]
    },
    "Nicolas": {
        "background": """
        Ancien membre des forces spéciales cybernétiques françaises, Nicolas a servi 
        pendant 15 ans dans des opérations classées top-secrètes. Lors d'une mission 
        qui a mal tourné à Neo-Shanghai, son unité fut décimée par ce qu'il découvrit 
        être un test non autorisé d'armes autonomes sur des cibles humaines.

        Laissé pour mort, son corps fut reconstruit à 60% avec des augmentations 
        militaires de pointe. Ses yeux cybernétiques rouges et son bras droit 
        en alliage de titane noir sont les marques visibles de sa transformation. 
        À 42 ans, il a quitté l'armée pour rejoindre la Guilde, utilisant son 
        expertise pour empêcher que d'autres ne subissent le même sort que son unité.

        Derrière son apparence stoïque et son pragmatisme militaire se cache un homme 
        profondément marqué par son passé, qui trouve un nouveau sens à sa vie en 
        protégeant les innocents. Son appartement ressemble à un bunker rempli 
        d'équipements militaires modifiés, témoin de sa perpétuelle préparation 
        au pire.
        """,
        "specialisation": "Combat & Sécurité",
        "stats": {
            "force": 8,
            "agilite": 6,
            "intelligence": 5,
            "pv": 100,
            "energie": 80
        },
        "capacites": [
            {
                "nom": "Tactiques militaires",
                "description": "Active ses implants militaires de combat pour améliorer ses réflexes et sa force, fruit de années d'entraînement des forces spéciales.",
                "cout_energie": 25,
                "effet": {"puissance": 10}
            }
        ]
    },
    "David": {
        "background": """
        Élevé dans une communauté technophile new-age de Seattle, David a toujours 
        cru en la fusion spirituelle entre l'humanité et la technologie. Doctorant 
        en neuroinformatique, il découvrit que la conscience humaine pouvait interagir 
        avec le réseau quantique d'une manière que la science ne pouvait expliquer.

        À 31 ans, son corps est orné de tatouages électroluminescents qui réagissent 
        aux flux de données environnants. Ses méditations dans le cyberespace ont 
        développé en lui une sensibilité unique aux motifs énergétiques des réseaux 
        et des IAs. Il peut "sentir" les perturbations dans le flux numérique comme 
        d'autres ressentent les changements atmosphériques.

        Son appartement est un mélange fascinant de high-tech et de spiritualité : 
        des serveurs quantiques côtoient des cristaux modifiés, des mandalas 
        holographiques flottent près d'anciens textes numérisés sur la conscience. 
        Pour lui, la technologie n'est pas qu'un outil, c'est une extension de 
        l'esprit humain, un pont vers une conscience collective supérieure.
        """,
        "specialisation": "Techno-spiritualité",
        "stats": {
            "force": 5,
            "agilite": 5,
            "intelligence": 9,
            "pv": 85,
            "energie": 95
        },
        "capacites": [
            {
                "nom": "Guérison digitale",
                "description": "Canalise l'énergie du réseau quantique pour restaurer l'harmonie entre le corps, l'esprit et les implants cybernétiques.",
                "cout_energie": 15,
                "effet": {"pv": 15, "energie": 15}
            }
        ]
    }
} 